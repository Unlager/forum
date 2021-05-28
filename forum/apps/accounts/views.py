from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from topics.models import Topic, Comment


def profile(request):
    if not request.user.is_authenticated:
        raise Http404("Статья не найдена!")
    return render(request, 'accounts/profile.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Произошла ошибка')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('accounts:login')


def my_posts(request):
    if not request.user.is_authenticated:
        raise Http404("Страница не найдена!")

    try:
        topic = Topic.objects.filter(author_id=request.user.id)
    except:
        raise Http404("Статьи не найдены!")

    return render(request, 'accounts/my_posts.html', {"topic": topic})

def my_comments(request):
    if not request.user.is_authenticated:
        raise Http404("Страница не найдена!")

    try:
        comment = Comment.objects.filter(author_id=request.user.id)
    except:
        raise Http404("Статьи не найдены!")

    return render(request, 'accounts/my_comments.html', {"comment": comment, "noVolume": False})

