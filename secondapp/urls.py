from django.contrib import admin
from django.urls import path

from secondapp import views

urlpatterns = [
    path('f3/', views.f3),
    path('f4/', views.f4),
]
