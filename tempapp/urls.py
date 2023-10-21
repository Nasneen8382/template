from django.contrib import admin
from django.urls import path
from tempapp import views

urlpatterns = [
    path('', views.loginpage,name='loginpage'),
    path('admin', views.admin,name='admin'),
    path('index', views.index,name='index'),
    path('login', views.login,name='login'),
    path('signuppage', views.signuppage,name='signuppage'),
    path('signup', views.signup,name='signup'),
    path('logout', views.logout,name='logout'),
    path('themechange/<str:nam>', views.themechange,name='themechange'),
]