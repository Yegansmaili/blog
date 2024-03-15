from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


class SignupVie(generic.CreateView):
    form_class = UserCreationForm
    context_object_name = 'form'
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
