from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('api/books', views.BookList.as_view(), name='book_list'),
    path('api/books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
=======
    path('api/books', views.ContactList.as_view(), name='book_list'),
    path('api/books/<int:pk>', views.ContactDetail.as_view(), name='book_detail'),
>>>>>>> 24b12cd8a200c0ae803212d05ea996717e194f2e
]
