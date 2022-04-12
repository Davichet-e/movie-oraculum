from django.shortcuts import render

from webpage.use_cases.retrieve_most_popular_movies import retrieve_most_popular_movies


def index(request):
    most_popular_movies = retrieve_most_popular_movies()
    return render(
        request, "webpage/index.html", {"most_popular_movies": most_popular_movies}
    )
