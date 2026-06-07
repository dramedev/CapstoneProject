from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .serializers import UserSerializer
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer


def index(request):
    return render(request, 'index.html', {})


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 