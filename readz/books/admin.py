from django.contrib import admin
from books.models import posts
from books.models import user_collection


# Register your models here.
admin.site.register(posts)

admin.site.register(user_collection)