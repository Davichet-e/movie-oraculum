from django.urls import path
from webpage.views.filter_movies_by_field import filter_movies_by_field_view

from webpage.views.movie_details import movie_details
from webpage.views.recommend_movie import RecommendAnalysisView
from webpage.views.search_movies import SearchMovieView

from .views.index import index
from .views.review_analysis import ReviewAnalysisView
from .views.top_movies import top_movies


urlpatterns = [
    path("recommend-movies", RecommendAnalysisView.as_view(), name="recommend_movies"),
    path("search", SearchMovieView.as_view(), name="search"),
    path(
        "movies/<field>/<value>/",
        filter_movies_by_field_view,
        name="filter_movies_by_field",
    ),
    path("movies/<movie_id>/", movie_details, name="movie_details"),
    path("top-movies", top_movies, name="top_movies"),
    path("review-analysis", ReviewAnalysisView.as_view(), name="review_analysis"),
    path("", index, name="index"),
]
