from django.contrib import admin
from django.urls import path, include
from newapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('homea/',views.home,name="home"),
    path('signup/',views.SaveEnquiry,name="signup"),
    path('home/',views.homea,name="homea"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)