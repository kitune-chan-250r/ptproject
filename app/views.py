from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm#UserCreationForm
    success_url = reverse_lazy('complete')
    template_name = 'create.html'

class SignUpComp(TemplateView):
	template_name = "registration/login.html"