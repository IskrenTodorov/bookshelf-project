from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review-list'),
    path('book/<int:book_pk>/add/', views.ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
]