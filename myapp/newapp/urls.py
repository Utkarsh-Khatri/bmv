from django.contrib import admin
from django.urls import path
from newapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminbookings/',views.admin_bookings,name='adminbookings'),
    path('homea/', views.home, name="home"),
    path('', views.index, name="index"),
    path('signup/', views.SaveEnquiry, name="signup"),
    path('home/', views.homea, name="homea"),
    path('search/', views.listing, name='search'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('home/book/', views.book_venue, name='book'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('home/list/', views.Register_Venue, name='Register_Venue'),
    path('home/list/register', views.Register_Confirmation, name='Register_confirmation'),
    path('hall/<int:venue_id>/', views.book_venue, name='hall_detail'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
