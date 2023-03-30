from rest_framework import serializers
from .models import MenuItems, Booking
from django.contrib.auth.models import User

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']