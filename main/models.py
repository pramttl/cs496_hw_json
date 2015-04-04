from django.db import models


class JsonQuestion(models.Model):
    """
    Contains the JSON question
    """
    input_json = models.TextField()
    question = models.TextField()
    output_json = models.TextField()
