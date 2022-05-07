from django.urls import path

from .views.index import index
from .views.review_analysis import ReviewAnalysisView
from .views.top_movies import top_movies


urlpatterns = [
    path("top-movies", top_movies, name="top_movies"),
    path("review-analysis", ReviewAnalysisView.as_view(), name="review_analysis"),
    path("", index, name="index"),
]
