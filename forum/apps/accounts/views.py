from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


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
#Принимаем