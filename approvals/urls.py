from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('approvals/', views.approvalPage, name='approvals'),
    path('stats/', views.statsPage, name='stats'),
    path('apply/', views.applyPage, name="apply")
]