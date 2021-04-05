from django.contrib import admin
from books.models import posts
from books.models import user_collection
from books.models import book_exchange
from books.models import Comment
from books.models import horror
from books.models import travel
from books.models import romantic
from books.models import mystery




# Register your models here.
admin.site.register(posts)
admin.site.register(user_collection)


admin.site.register(book_exchange)
admin.site.register(Comment)
admin.site.register(romantic)
admin.site.register(horror)
admin.site.register(mystery)
admin.site.register(travel)
