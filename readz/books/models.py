from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This file is used for creating models which are tables at backend in sqlite3 database

class posts(models.Model):

    Comment = models.TextField(blank=True)
    Name = models.TextField(blank=True)
    Title= models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    def __str__(self):
        return self.Title

class Comment(models.Model):
    
    name = models.CharField(max_length=255)
    body=  models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.posts.Title, self.name)

class user_collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_collection1", null=True)
    title = models.TextField(blank=True) 
    image = models.ImageField(upload_to='images')

    
    def __str__(self):
        self.title


class romantic(models.Model):
    book1_id = models.IntegerField()
    Name= models.TextField(max_length=50)
    
    image1 = models.ImageField()

    def __str__(self):
        return self.Name

class horror(models.Model):
    book1_id = models.IntegerField()
    Name= models.TextField(max_length=50)
    
    image1 = models.ImageField()

    def __str__(self):
        return self.Name

class travel(models.Model):
    book1_id = models.IntegerField()
    Name= models.TextField(max_length=50)
    
    image1 = models.ImageField()

    def __str__(self):
        return self.Name

class mystery(models.Model):
    book1_id = models.IntegerField()
    Name= models.TextField(max_length=50)
   
    image1 = models.ImageField()

    def __str__(self):
        return self.Name






class book_exchange(models.Model):
    request_type = models.TextField(blank=True)
    requester_name = models.TextField(blank= True)
    book_name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    address = models.TextField(blank=True)



    

    

