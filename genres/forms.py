from django import forms
from .models import Genre


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ['name', 'description']
        labels = {
            'name': 'Наименование на жанра',
            'description': 'Описание',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Въведи жарн', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

        error_messages = {
            'name': {
                'unique': 'Жанр с това име вече съществува.',
                'min_length': 'Името трябва да е поне 2 символа.',
            }
        }