from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

user = User()


def signUp(request):
    return render(request, 'registration\signUp.html')



def home(request):
    return render(request, 'empty.html')