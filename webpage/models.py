from __future__ import annotations
from django.db import models

from webpage.entities.movie import RetrievedMovie


class Director(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    # title = models.CharField(max_length=200)
    poster_url = models.URLField()
    # release_year = models.PositiveSmallIntegerField()
    duration = models.DurationField(null=True)
    rating = models.FloatField(null=True)
    # plot = models.TextField()

    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)

    @classmethod
    def from_retrieved_movie(cls, retrieved_movie: RetrievedMovie) -> Movie:
        new_movie = cls(
            id=retrieved_movie.movie_id,
            poster_url=retrieved_movie.poster_url,
            duration=retrieved_movie.duration,
            rating=retrieved_movie.rating,
        )

        new_movie.save()
        if retrieved_movie.directors:
            for director in retrieved_movie.directors:
                new_movie.directors.create(name=director)

        if retrieved_movie.genres:
            for genre in retrieved_movie.genres:
                new_movie.genres.create(name=genre)

        return new_movie
