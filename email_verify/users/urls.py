from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'users'
urlpatterns = [
	path('', views.home, name='home'),
	path('', views.home, name='link'),
	path('', views.home, name='users'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('activate/<str:uid>/<str:token>/', views.activate, name='activate'),
]