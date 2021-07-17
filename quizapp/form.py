


from django.forms import fields
from quizapp.models import QuestionModel, ScoreModel
from django import forms



class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = "__all__"
