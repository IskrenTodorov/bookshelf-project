from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Review
from .forms import ReviewForm, ReviewDeleteConfirmForm
from books.models import Book


class ReviewCreateView(View):
    def get(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        form = ReviewForm()
        return render(request, 'reviews/review_form.html', {'form': form, 'book': book})

    def post(self, request, book_pk):
        book = get_object_or_404(Book, pk=book_pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book-detail', pk=book.pk)
        return render(request, 'reviews/review_form.html', {'form': form, 'book': book})


class ReviewUpdateView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(instance=review)
        return render(request, 'reviews/review_form.html', {'form': form, 'book': review.book})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('book-detail', pk=review.book.pk)
        return render(request, 'reviews/review_form.html', {'form': form, 'book': review.book})


class ReviewDeleteView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = ReviewDeleteConfirmForm(initial={'confirm_title': review.title})
        return render(request, 'reviews/review_confirm_delete.html', {
            'review': review,
            'form': form
        })

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        book_pk = review.book.pk
        review.delete()
        return redirect('book-detail', pk=book_pk)


class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.select_related('book').all()
        return render(request, 'reviews/review_list.html', {'reviews': reviews})