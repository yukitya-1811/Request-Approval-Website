from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('approvals/', views.approvalPage, name='approvals'),
    path('approve/<str:pk>', views.approveRequest, name="approveRequest"),
    path('stats/', views.statsPage, name='stats'),
    path('apply/', views.applyPage, name="apply"),
    path('create/', views.createTemplate, name='create'),
    path('appview/<str:pk>', views.viewPage, name="appview"),
    path('delete/<str:pk>', views.deleteRequest, name="deleteRequest"),
    path('logout/', views.logoutPage, name='logout'),
]