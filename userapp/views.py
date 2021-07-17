from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class UsersingupView(CreateView):
    template_name = 'userapp/singup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("Home_page")
