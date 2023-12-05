# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = '/Users/thoanguyen/4800/Team-Base-Project/FMFF/accounts/templates/registration/login.html'
   