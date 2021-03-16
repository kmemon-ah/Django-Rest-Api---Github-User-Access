from django.urls import path
from django.shortcuts import render
from .views import *

from . import views

app_name = 'githubapi'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile', views.profile, name = 'User-profile')
]
