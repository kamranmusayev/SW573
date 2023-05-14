from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import get_user_model
# Create your views here.

user = get_user_model()


def signUp(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        return redirect('home')


    else:
        form = SignUpForm()
    return render(request, 'registration\signUp.html', {"form":form})



def home(request):
    return render(request, 'empty.html')