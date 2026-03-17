from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from genres.models import Genre


class Author(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    bio = models.TextField(blank=True, null=True)
    birth_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(2)])
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='books',
        blank=True
    )
    published_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None