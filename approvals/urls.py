from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('approvals/', views.approvalPage, name='approvals'),
    path('stats/', views.statsPage, name='stats'),
]