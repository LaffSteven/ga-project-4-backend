from django.urls import path
from . import views

urlpatterns = [
    path('api/books', views.ContactList.as_view(), name='book_list'),
    path('api/books/<int:pk>', views.ContactDetail.as_view(), name='book_detail'),
]
