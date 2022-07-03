from django.shortcuts import render
from django.views.generic import CreateView 
from .forms import CustomUserCreationForm 
from django.http import HttpResponse 
from django.urls import reverse_lazy 

def signupcomplete(request): 
    return HttpResponse("<p>sign up が完了しました。</p>")

class SignUpView(CreateView): 
    form_class = CustomUserCreationForm 
    template_name = 'signup.html' 
    success_url = reverse_lazy('complete') 

# Create your views here.
