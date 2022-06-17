from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)

from .models import Review
admin.site.register(Review)
