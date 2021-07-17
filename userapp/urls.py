from django.urls import path
from .views import UsersingupView



urlpatterns = [
    path('singup/',UsersingupView.as_view(),name="singup"),
]



