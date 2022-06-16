from django.urls import path
from . import views

urlpatterns = [

    path('api/books', views.BookList.as_view(), name='book_list'),
    path('api/books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),

    path('api/books/reviews', views.ReviewList.as_view(), name='review_list'),
    path('api/books/reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),

]
