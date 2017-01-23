from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
        list_display = ('name', 'author', 'year', 'read_date', 'category','comment')
        search_fields=['name']



admin.site.register(Book)
