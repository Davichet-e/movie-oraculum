from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render
from webpage.use_cases.retrieve_movie import retrieve_movie


def movie_details(request: HttpRequest, movie_id: str):
    movie = retrieve_movie(movie_id)
    if movie is None:
        return HttpResponseNotFound("<h1>Movie not found</h1>")

    return render(request, "webpage/movie_details.html", {"movie": movie})
