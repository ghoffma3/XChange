# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login as djLogin, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm
# Create your views here.

def index(request):
    return render(request, 'XChange/index.html')

def login(request):
    if request.method == 'POST' and request.POST.get('submit') == "register":
        login_form = AuthenticationForm()
        reg_form = SignUpForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            raw_password = reg_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            djLogin(request, user)
            return redirect('home')
    
    elif request.method == 'POST' and request.POST.get('submit') == "login": 
        login_form =  AuthenticationForm(request.POST)
        reg_form = SignUpForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            djLogin(request, user)
            return redirect("home")
        else:
            return render(request, 'XChange/login.html', {'login_form': login_form, 'reg_form': reg_form, 'error': 'Login Failed'})
    else:
        login_form = LoginForm()
        reg_form = SignUpForm()
    return render(request, 'XChange/login.html', {'login_form': login_form, 'reg_form': reg_form})
    
def settings(request):
    return render(request, 'XChange/settings.html')
    
def search(request):
    return render(request, 'XChange/search.html')    

def bookmarks(request):
    return render(request, 'XChange/bookmarks.html')
    
def home(request):
    return render(request, 'XChange/home.html')
    
def myPortfolio(request):
    return render(request, 'XChange/myPortfolio.html')    

