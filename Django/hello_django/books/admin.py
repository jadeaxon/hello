from books.models import Publisher
from books.models import Book
from books.models import Author

from django.contrib import admin

# Register these data model classes with the Django admin interface.
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)

