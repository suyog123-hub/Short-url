from django.urls import path
from .views import *
from app_main.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',signin,name="signin"),
    path('signout/',signout,name='signout'),
    path('register/',register,name="register"),
    path("home/",home,name='home'),
]