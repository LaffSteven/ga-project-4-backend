from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, null=True)
    author_name = models.CharField(max_length=128, null=True)
    price = models.FloatField(null = True)
    publisher = models.CharField(max_length=128, null=True)
    publication_date = models.DateField(null = True)
    genre = models.CharField(max_length=128, null=True)
    cover_art = models.TextField(null=True)
    page_count = models.IntegerField(null = True)
    language = models.CharField(max_length=128, null=True)
    isbn = models.CharField(max_length=128, null=True)
    rating = models.FloatField(null = True)
    pass

class Review(models.Model):
    review = models.TextField(Book)
    user = models.CharField(max_length=32, unique=True)
