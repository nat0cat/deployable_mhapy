from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def MinValueValidator(value):
    """
    A function that validates if a value is greater than 0 
    """
    if value < 0:
        raise ValidationError(
            ("%(value)s is not an greater than 0"),
            params={"value": value},
        )

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(validators=[MinValueValidator])
    gender = models.CharField(max_length=40)
    issue = models.IntegerField(default=1)

class Assessments(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    assessment_title = models.CharField(max_length=100)
    scale = models.IntegerField(validators=[MinValueValidator])
    num_questions = models.IntegerField(validators=[MinValueValidator])

class UserStats(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessments, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator])
    count = models.IntegerField(default=0, validators=[MinValueValidator])
    num_questions = models.IntegerField(validators=[MinValueValidator])

    class Meta:
        # Constraint
        unique_together = ('user', 'assessment', 'count')

class Questions(models.Model):
    assessment = models.ForeignKey(Assessments, on_delete=models.CASCADE)
    question_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=500)

class Responses(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    num = models.IntegerField(default=0, validators=[MinValueValidator])
    count = models.IntegerField(default=0, validators=[MinValueValidator])

    class Meta:
        # Constraint 
        unique_together = ('user', 'question', 'count')
