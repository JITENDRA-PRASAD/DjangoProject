from django.contrib import admin
from .models import QuestionModel, ScoreModel

# Register your models here.


admin.site.register(ScoreModel)
admin.site.register(QuestionModel)