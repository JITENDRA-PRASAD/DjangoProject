from django.db import models
from django.db.models.base import Model

# Create your models here.


class QuestionModel(models.Model):
    question = models.CharField(max_length=500)
    optiona = models.CharField(max_length=200)
    optionb = models.CharField(max_length=200)
    optionc = models.CharField(max_length=200)
    optiond = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.question)

class ScoreModel(models.Model):
    name = models.CharField(max_length=200)
    marks = models.CharField(max_length=4)
    lifeline = models.CharField(max_length=2, default='0', editable=True)

    def __str__(self):
        return "{}({})".format(self.name, self.marks)
    