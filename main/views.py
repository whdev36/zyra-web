from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Home
def home(request):
    return render(request, 'home.html', {})

# Login user
def login_user(request):
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_active:
                messages.error(request, 'This account is inactive.', extra_tags='danger')
            else:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                next_page = request.GET.get('next', 'home')
                return redirect(next_page)
        else:
            messages.error(request, 'Invalid username or password', extra_tags='danger')
    return render(request, 'main/login.html', {'username': username})
