from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['reviewer_name', 'rating', 'title', 'content']
        labels = {
            'reviewer_name': 'Твоето име',
            'rating': 'Оценка (1–5)',
            'title': 'Заглавие на рецензията',
            'content': 'Текст на рецензията',
        }

        widgets = {
            'reviewer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван Петров'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

        error_messages = {
            'rating': {
                'min_value': 'Оценката трябва да е поне 1.',
                'max_value': 'Оценката не може да надвишава 5.',
            },
            'content': {
                'min_length': 'Рецензията трябва да е поне 20 символа.',
            }
        }


class ReviewDeleteConfirmForm(forms.Form):
    confirm_title = forms.CharField(
        label='Заглавие на рецензията',
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False
    )