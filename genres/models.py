from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[MinLengthValidator(2)],
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def book_count(self):
        return self.books.count()