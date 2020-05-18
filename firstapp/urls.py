from django.contrib import admin
from django.urls import path

from firstapp import views

urlpatterns = [
    path('f1/', views.f1),
    path('f2/', views.f2),
]
