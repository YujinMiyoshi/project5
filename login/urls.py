from django.urls import path 
from .views import SignUpView, signupcomplete

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('complete/', signupcomplete, name='complete'), 
] 