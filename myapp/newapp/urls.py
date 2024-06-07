from django.contrib import admin
from django.urls import path, include
from newapp import views

urlpatterns = [
    
    path('home/',views.home,name="home"),
    path('signup/',views.SaveEnquiry,name="signup"),
    
    
]