from django.db import models

# Create your models here.

class LibaryBook(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    available = models.BooleanField(default=True)