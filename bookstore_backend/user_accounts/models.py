from django.db import models

# Create your models here.
from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    staff = models.BooleanField()
    # cart = models.JSONField(encoder=None, null=True)
