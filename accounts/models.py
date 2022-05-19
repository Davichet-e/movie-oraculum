from django.contrib.auth.models import AbstractUser
from django.db import models
from webpage.models import Movie


class User(AbstractUser):
    """Movie Oraculum user"""

    liked_movies = models.ManyToManyField(Movie)
