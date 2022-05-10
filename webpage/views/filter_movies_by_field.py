from django.http import HttpRequest
from django.shortcuts import render

from webpage.use_cases.filter_movies_by_field import filter_movies_by_field


def filter_movies_by_field_view(request: HttpRequest, field: str, value: str):
    movies = filter_movies_by_field(field, value)

    return render(
        request,
        "webpage/filter_movies_by_field.html",
        {"movies": movies, "field": field, "value": value},
    )
