from django.db import models

"""
Quizz Questions and Responses
"""
class question_and_response(models.Model):
    question = models.CharField(max_length=500)
    responses = models.CharField(max_length=700)
    correct_response = models.CharField(max_length=1)