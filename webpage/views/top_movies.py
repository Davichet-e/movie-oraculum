from django.http import HttpRequest
from django.shortcuts import render

from webpage.use_cases.retrieve_most_popular_movies import retrieve_most_popular_movies


def top_movies(request: HttpRequest):
    most_popular_movies = retrieve_most_popular_movies(trending=False)
    return render(
        request, "webpage/top_movies.html", {"most_popular_movies": most_popular_movies}
    )
