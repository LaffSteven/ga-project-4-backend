from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Review(models.Model):
    review = models.TextField()
    user = models.CharField(max_length=32, unique=True)

    # def __str__(self):
    #     return(self.review, self.user)

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
    reviews = ArrayField(models.ForeignKey(Review, on_delete=models.CASCADE, null=True))




    #reviews = models.ManyToManyField(Review)

    # def __str__(self):
    #     return(self.title, self.author_name, self.price, self.publisher, self.publication_date, self.genre, self.cover_art, self.page_count, self.language, self.isbn, self.rating, self.reviews)


# #https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/
#
#
# def __str__(self):
#     return "%s %s" (self.review, self.user)
#
#
# def __str__(self):
#     return "%s %s %i %s % %s %s %i %s %s $i %" (self.)
