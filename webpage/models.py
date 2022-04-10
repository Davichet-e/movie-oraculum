from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    rating = models.FloatField()
    plot = models.TextField()

    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)
