from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

# Home
def home(request):
    return render(request, 'home.html', {})

# Login user
def login_user(request):
    return render(request, 'main/login.html', {})
