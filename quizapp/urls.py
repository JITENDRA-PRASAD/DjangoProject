from django.urls import path
from . import views


urlpatterns = [
    path("", views.KbcHome.as_view() , name="Home_page"),
    path("feature/",views.FeaturesView.as_view(), name="features"),
    path("kbc/<int:id>",views.QuestionShow.as_view(), name="question_show"),
    path("topranker/",views.AllScoreView.as_view(), name="top_ranker"),
    path("myscore/",views.MyScore.as_view(), name="my_score")
]
