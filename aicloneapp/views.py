from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login




def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'aicloneapp/home.html', {})


def register_request(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if len(first_name) < 3 and len(last_name) < 3:
            messages.add_message(request, messages.INFO, "First and last name must be at least 3 characters long")
            return render(request, 'aicloneapp/register.html')
        if password == request.POST['confirm_password'] and len(password) > 7:
            username = first_name + "_" + last_name
            user = User.objects.create_user(username=username,email=email, first_name=first_name, last_name=last_name, password=password)
            user.save()
            return redirect('login')
        else:
            messages.add_message(request, messages.INFO, "Password must be at least 8 characters long and match the confirm password")
            return render(request, 'aicloneapp/register.html')
    else:
        return render(request, 'aicloneapp/register.html', {})



def login_request(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, "Username or password is incorrect")
            return render(request, 'aicloneapp/login.html')
    else:
        return render(request, 'aicloneapp/login.html', {})


def logout_request(request):
    logout(request)
    return redirect('login')