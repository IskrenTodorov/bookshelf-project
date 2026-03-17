from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreListView.as_view(), name='genre-list'),
    path('add/', views.GenreCreateView.as_view(), name='genre-create'),
    path('<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre-delete'),
]