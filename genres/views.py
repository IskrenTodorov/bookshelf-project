from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Genre
from .forms import GenreForm


class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'genres/genre_list.html', {'genres': genres})


class GenreDetailView(View):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        return render(request, 'genres/genre_detail.html', {'genre': genre})


class GenreCreateView(View):
    def get(self, request):
        form = GenreForm()
        return render(request, 'genres/genre_form.html', {'form': form, 'action': 'Добави'})

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre-list')
        return render(request, 'genres/genre_form.html', {'form': form, 'action': 'Добави'})


class GenreUpdateView(View):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        form = GenreForm(instance=genre)
        return render(request, 'genres/genre_form.html', {'form': form, 'action': 'Редактирай'})

    def post(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre-list')
        return render(request, 'genres/genre_form.html', {'form': form, 'action': 'Редактирай'})


class GenreDeleteView(View):
    def get(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        return render(request, 'genres/genre_confirm_delete.html', {'genre': genre})

    def post(self, request, pk):
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return redirect('genre-list')