from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_year']
    search_fields = ['first_name', 'last_name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year']
    list_filter = ['genres', 'published_year']
    search_fields = ['title', 'author__last_name']