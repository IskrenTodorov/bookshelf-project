from django import forms
from .models import Book, Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio', 'birth_year']
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'bio': 'Биография',
            'birth_year': 'Година на раждане',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Вазов'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'birth_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'published_year', 'description', 'cover_image']
        labels = {
            'title': 'Заглавие',
            'author': 'Автор',
            'genres': 'Жанрове',
            'published_year': 'Година на издаване',
            'description': 'Описание',
            'cover_image': 'Корица (снимка)',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'genres': forms.CheckboxSelectMultiple(),
            'published_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Заглавието трябва да е поне 2 символа.")
        return title


class BookSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='Търсене',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Търси книга...'})
    )
    genre = forms.ChoiceField(
        required=False,
        label='Жанр',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    def __init__(self, *args, **kwargs):
        from genres.models import Genre
        super().__init__(*args, **kwargs)
        genres = [('', 'Всички жанрове')] + [(g.id, g.name) for g in Genre.objects.all()]
        self.fields['genre'].choices = genres