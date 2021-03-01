from django.urls import path

from . import views

app_name = 'topics'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('post/', views.post, name = 'post'),
	path('<int:topic_id>/delete_post/', views.delete_post, name = 'delete_post'),
	path('create_post/', views.create_post, name = 'create_post'),
	path('<int:topic_id>/', views.detail, name = 'detail'),
	path('<int:topic_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
	path('<int:topic_id>/delete_comment/<int:c_id>', views.delete_comment, name = 'delete_comment'),
]

