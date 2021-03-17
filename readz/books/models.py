from django.db import models


# Create your models here.

class posts(models.Model):
    Comment = models.TextField(blank=True)
    Name = models.CharField(max_length=100, blank=True)


class user_collection(models.Model):
    title = models.TextField(blank=True) 
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


    

    

