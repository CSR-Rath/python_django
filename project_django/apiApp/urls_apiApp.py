# from importlib.resources import path
from django.urls import path
from apiApp import views

urlpatterns = [
    path('', views.startup, name='startup'),
]
