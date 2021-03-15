from django.db import models


# Create your models here.


class posts(models.Model):
    Comment = models.TextField(blank=True)
<<<<<<< HEAD


class user_collection(models.Model):
    title = models.TextField(blank=True) 
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


    
=======
    Name = models.CharField(max_length=1000, blank=True)
>>>>>>> 45266788720e949fc56c763242d611f71c27f84c
