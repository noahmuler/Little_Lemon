#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers
from restaurant.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'menu_item_description', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['first_name', 'reservation_date', 'reservation_slot', 'guest_count']
