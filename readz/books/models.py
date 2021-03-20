from django.db import models


# Create your models here.

class posts(models.Model):
    Comment = models.TextField(blank=True)
    Name = models.TextField(blank=True)
    def __str__(self):
        return self.Name



class user_collection(models.Model):
    title = models.TextField(blank=True) 
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class book_exchange(models.Model):
    request_type = models.TextField(blank=True)
    requester_name = models.TextField(blank= True)
    book_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    address = models.TextField(blank=True)



    

    

