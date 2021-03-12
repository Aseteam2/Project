from django.db import models


# Create your models here.


class posts(models.Model):
    Comment = models.TextField(blank=True)
    