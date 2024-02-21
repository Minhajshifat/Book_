from django.urls import path
from . import views

urlpatterns = [
    path("all_books/", views.all_books, name="all_books"),
    path("details/<int:id>/", views.ShowDetails.as_view(), name="book_details"),
    path("comment/<int:id>/", views.ShowDetails.as_view(), name="comment_page"),
    path(
        "category_wise_book/<slug:category_slug>/",
        views.all_books,
        name="category_wise_book",
    ),
]
