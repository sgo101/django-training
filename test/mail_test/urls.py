from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'mail'

urlpatterns = [
	path('', views.home, name='home'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='mail_test/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='mail_test/logout.html'), name='logout'),
	path('user201/', views.user201, name='user201'),
	path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
]