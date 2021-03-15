from django.db import models


# Create your models here.


class posts(models.Model):
    Comment = models.TextField(blank=True)


class user_collection(models.Model):
    book_name = models.TextField(blank=True) 
    photo = models.ImageField(upload_to='cars')
    