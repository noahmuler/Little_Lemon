from django.urls import path
from .views import *


urlpatterns = [

    # GUI ROUTES

    path('', home, name="home"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('reservations/', reservations, name="reservations"),
    path('menu/', menu, name="menu"),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),  
    path('bookings/', bookings, name='bookings'), 
]
