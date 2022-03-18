from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import SignUpForm



def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'aicloneapp/home.html', {})


def register_request(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Successfully registered")
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'aicloneapp/register.html', {'form': form})




def login_request(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, "Successfully Signed in")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Username or password is incorrect")
            return render(request, 'aicloneapp/login.html')
    else:
        return render(request, 'aicloneapp/login.html', {})


def logout_request(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Successfully Loged out")
    return redirect('login')