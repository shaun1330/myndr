from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import password_validators_help_texts
from django.views.generic import CreateView, ListView, TemplateView
from django.shortcuts import render, redirect
from app.models import Task
from app.forms import LoginForm
import time


# Create your views here.


def home_view(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('app:login')
        else:
            return render(request, 'home.html')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:home')
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, "login.html", {"form": form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:login')


def tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'tasks/tasks.html', context=context)

