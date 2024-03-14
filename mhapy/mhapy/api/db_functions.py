"""functions"""
import psycopg2 as pg
from datetime import datetime
from .models import * 
from django.db.models import F

def update_userstats(user_id, assessment_id, count):
    """
    Function that updates the userstats when response object is created 
    """
    try:
        # Get the total number of answered questions and sum of responses
        num_questions, total_score = Responses.objects.filter(user_id=user_id, count=count, question__assessment_id=assessment_id).aggregate(num_questions=models.Count('question_id', distinct=True), total_score=models.Sum('num')).values()

        # Update or create the UserStats instance
        user_stats, created = UserStats.objects.get_or_create(user_id=user_id, assessment_id=assessment_id, count=count, defaults={'score': total_score, 'num_questions': num_questions})

        if not created:
            # Update the existing UserStats instance
            user_stats.num_questions = num_questions
            user_stats.score = total_score
            user_stats.save()

        return True

    except Exception as e:
        # Handle exceptions
        print(f"Error updating user stats: {e}")
        return False

