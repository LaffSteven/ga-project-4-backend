from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer
import json


# Create your views here.
class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer
