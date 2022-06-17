from django.urls import path
from . import views

urlpatterns =[
    path('api/cart', views.CartList.as_view(), name='cart')
]
