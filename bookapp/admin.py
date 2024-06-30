from django.contrib import admin

from bookapp.models import Author,Publisher,Language, Category,Book

admin.site.register(Author)

admin.site.register(Publisher)

admin.site.register(Language)

admin.site.register(Category)

admin.site.register(Book)


