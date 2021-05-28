from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
	path('register/', views.register, name = 'register'),
	path('login/', views.user_login, name = 'login'),
	path('logout/', views.user_logout, name = 'logout'),
	path('profile/', views.profile, name = 'profile'),
	path('my_posts/', views.my_posts, name = 'my_posts'),
	path('my_comments/', views.my_comments, name = 'my_comments'),
]

