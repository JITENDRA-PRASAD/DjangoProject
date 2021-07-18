

from quizapp.models import QuestionModel
from django import forms



class QuestionCreateForm(forms.ModelForm):
    
    
    class Meta:
        model = QuestionModel
        fields = "__all__"
