from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('change/', views.change_password),
]