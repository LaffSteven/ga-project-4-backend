from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BookSerializer
from .serializers import ReviewSerializer
from .models import Book

import json
from django.http import JsonResponse


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


from .serializers import ReviewSerializer
from .models import Review

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer



#Choices are: book, book_id, id, review, user_id
def getBookReviews(request):
    if request.method=='GET':
        print(request.body)
        jsonRequest = json.loads(request.body)
        bookID = int(jsonRequest['bookID'])
        # print(bookID)
        reviewList = list(Review.objects.filter(book_id=bookID).values('id', 'review', 'user_id', 'book_id'))
        # #book_id==bookID
        # print(reviewList)
        # return JsonResponse({})
        return JsonResponse(reviewList, safe=False)
        # else:
        #     return JsonResponse({})
    else:
        return JsonResponse({})



# if Book.objects.get(id=book.id):
#     print(str(bookID) + " is the book id")
# #print(Review.objects.order_by('book_id'))

