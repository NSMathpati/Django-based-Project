from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from .models import MenuItems, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.
class MenuitemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'pk'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]