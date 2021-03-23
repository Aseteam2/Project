from django.contrib import admin
from books.models import posts
from books.models import user_collection
from books.models import book_exchange


# Register your models here.
admin.site.register(posts)

admin.site.register(user_collection)

admin.site.register(book_exchange)
