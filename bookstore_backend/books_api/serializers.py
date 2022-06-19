from rest_framework import serializers
from .models import Book
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review', 'user_id', 'book_id')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name', 'price', 'publisher', 'publication_date', 'genre', 'cover_art', 'page_count', 'language', 'isbn', 'rating',)
        #depth = 1
