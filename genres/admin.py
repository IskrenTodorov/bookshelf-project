from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']