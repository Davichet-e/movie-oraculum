from django.urls import path

from webpage.views.movie_details import movie_details

from .views.index import index
from .views.review_analysis import ReviewAnalysisView
from .views.top_movies import top_movies


urlpatterns = [
    path("movies/<movie_id>", movie_details, name="movie_details"),
    path("top-movies", top_movies, name="top_movies"),
    path("review-analysis", ReviewAnalysisView.as_view(), name="review_analysis"),
    path("", index, name="index"),
]
