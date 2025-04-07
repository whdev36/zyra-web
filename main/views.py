from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Home
def home(request):
    return render(request, 'home.html', {})

# Login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            messages.warning(request, 'Check your username or password!')
    return render(request, 'main/login.html', {})
