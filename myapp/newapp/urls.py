from django.contrib import admin
from django.urls import path, include
from newapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('homea/',views.home,name="home"),
    path('',views.index,name="index"),
    path('signup/',views.SaveEnquiry,name="signup"),
    path('home/',views.homea,name="homea"),
    path('search/', views.listing, name='search'),
    path('login/', views.LoginPage, name='login'),
    path('login/SignUp/',views.SaveEnquiry,name='signup'),
    path('logout/', views.LogoutPage, name='logout'),
    path('book/',views.book_venue,name='book'),
    path('home/list/',views.Register_Venue,name='Register_Venue')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)