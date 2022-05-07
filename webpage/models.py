from django.db import models

from webpage.entities.movie import RetrievedMovie


class Director(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_url = models.URLField()
    release_year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    rating = models.FloatField()
    plot = models.TextField()

    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)

    trending = models.BooleanField()

    @classmethod
    def from_retrieved_movie(cls, retrieved_movie: RetrievedMovie) -> "Movie":
        new_movie = cls(
            title=retrieved_movie.title,
            poster_url=retrieved_movie.poster_url,
            release_year=retrieved_movie.release_year,
            duration=retrieved_movie.duration,
            rating=retrieved_movie.rating,
            plot=retrieved_movie.plot,

            trending=retrieved_movie.trending
        )
        new_movie.id = retrieved_movie.imdb_id
        for director in retrieved_movie.directors:
            new_movie.directors.add(Director.objects.create(name=director.name))

        for genre in retrieved_movie.genres:
            new_movie.genres.add(Genre.objects.create(name=genre.name))

        return new_movie
