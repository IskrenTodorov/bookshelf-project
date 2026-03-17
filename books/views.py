from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Book, Author
from .forms import BookForm, AuthorForm, BookSearchForm


class HomeView(View):
    def get(self, request):
        latest_books = Book.objects.select_related('author').prefetch_related('genres')[:6]
        total_books = Book.objects.count()
        total_authors = Author.objects.count()
        return render(request, 'books/home.html', {
            'latest_books': latest_books,
            'total_books': total_books,
            'total_authors': total_authors,
        })


class BookListView(View):
    def get(self, request):
        form = BookSearchForm(request.GET)
        books = Book.objects.select_related('author').prefetch_related('genres')

        if form.is_valid():
            query = form.cleaned_data.get('query')
            genre = form.cleaned_data.get('genre')
            if query:
                books = books.filter(title__icontains=query)
            if genre:
                books = books.filter(genres__id=genre)

        return render(request, 'books/book_list.html', {'books': books, 'form': form})


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        reviews = book.reviews.all()
        return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})


class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'books/book_form.html', {'form': form, 'action': 'Добави книга'})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        return render(request, 'books/book_form.html', {'form': form, 'action': 'Добави книга'})


class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'books/book_form.html', {'form': form, 'action': 'Редактирай книга'})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=book.pk)
        return render(request, 'books/book_form.html', {'form': form, 'action': 'Редактирай книга'})


class BookDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_confirm_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book-list')


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.prefetch_related('books').all()
        return render(request, 'books/author_list.html', {'authors': authors})


class AuthorDetailView(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        books = author.books.all()
        return render(request, 'books/author_detail.html', {'author': author, 'books': books})


class AuthorCreateView(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'books/author_form.html', {'form': form, 'action': 'Добави автор'})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
        return render(request, 'books/author_form.html', {'form': form, 'action': 'Добави автор'})

def custom_404(request, exception):
    return render(request, '404.html', status=404)