from django.shortcuts import render
from .db_functions import * 
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Users, Assessments, UserStats, Questions, Responses
from .serializers import UserSerializer, AssessmentsSerializer, UserStatsSerializer, QuestionsSerializer, ResponsesSerializer
from .AnalyzeUserInput import * 


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    

class AssessmentsViewSet(viewsets.ModelViewSet):
    queryset = Assessments.objects.all()
    serializer_class = AssessmentsSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def list(self, request):
        """
        Handles GET requests and returns a list of all Questions instances.
        """
        questions = Questions.objects.all()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)


class UserStatsViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with UserStats instances.

    Provides CRUD operations for UserStats instances.
    """
    queryset = UserStats.objects.all()
    serializer_class = UserStatsSerializer

    def list(self, request, user_id=None):
        """
        Handles GET requests and returns a list of all UserStats instances whose user_id is specified in the url.
        """
        # filter out all the userstats instance and return it as json 
        queryset = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response({"message": "No user found"})


class ResponsesViewSet(viewsets.ModelViewSet):
    """
    A viewset for interacting with Responses instances.

    Provides CRUD operations for Responses instances.
    """
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

    def create(self, request, question_id, *args, **kwargs):
        """
        Handles POST requests to create a new Response instance.

        Serializes and saves the request data to create a new Response object.
        Returns the serialized data of the newly created object if the request data is valid.
        If the data is not valid, returns an error response.
        """
        # get all the data passed in as request body 
        user_id = request.data.get('user_id')
        response = request.data.get('response')

        # convert free text into num -> nlp 
        int_choice = AnalyzeUserInput(response, 1)

        # Call the insert_responses function
        user_instance = Users.objects.get(pk=user_id)
        question_instance = Questions.objects.get(pk=question_id)
        assessment_id = question_instance.assessment.assessment_id

        response_exists = Responses.objects.filter(question_id=question_id, user_id=user_id).exists()
        # check in order to update the count value 
        if response_exists: 
            count = Responses.objects.filter(question_id=question_id, user_id=user_id).last().count 
        else:
            count = 0 

        # update the userstats model as user responds 
        try:
            # create a response instance 
            response_instance = Responses.objects.create(
                user=user_instance,
                question=question_instance,
                num=int_choice,
                count=count + 1 
            )
            serializer = self.get_serializer(response_instance)

            # after creating a response instance check if userstats instance exist 
            userstats_update = update_userstats(user_id, assessment_id, count+1)
            
            if not userstats_update:
                # user update was not done 
                return Response({"message": "Error updating user stats"})
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


