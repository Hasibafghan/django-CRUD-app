from django.shortcuts import render
from django.contrib.auth import login , logout , authenticate

# Create your views here.
def home(request):
    return render(request , 'home.html' , {})


def login_user(request):
    return render(request , 'login_user.html' , {})

def logout_user(request):
    logout(request)
    return render(request , 'home.html' , {})

def signup_user(request):
    return render(request , 'signup_user.html' , {})

