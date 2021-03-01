from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-label-group', 'class': 'form-control', 'placeholder': 'Псевдоним'}))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-label-group', 'class': 'form-control', 'placeholder': 'Пароль'}))

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-label-group', 'class': 'form-control', 'placeholder': 'Псевдоним'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-label-group', 'class': 'form-control', 'placeholder': 'Пароль'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-label-group', 'class': 'form-control', 'placeholder': 'Повтор пароля'}))
