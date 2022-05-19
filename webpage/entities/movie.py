from __future__ import annotations
from dataclasses import dataclass
import datetime

from webpage import models
from webpage.repositories.whoosh_repository import WhooshMovie


@dataclass(frozen=True)
class RetrievedMovie:
    """Represent the movie extracted from the webpage."""

    movie_id: str
    title: str
    poster_url: str
    release_year: int
    duration: datetime.timedelta | None
    rating: float | None
    plot: str

    directors: list[str]
    genres: list[str] | None

    # trending: bool # True if film is currently at https://www.imdb.com/chart/moviemeter/


@dataclass(frozen=True)
class Movie:
    movie_id: str
    title: str
    poster_url: str
    release_year: int
    duration: datetime.timedelta | None
    rating: float | None
    plot: str

    directors: list[str]
    genres: list[str] | None

    def __str__(self) -> str:
        return self.title

    @classmethod
    def from_model_and_whoosh_movie(
        cls, model: models.Movie, whoosh_movie: WhooshMovie
    ) -> Movie:
        """Given a the data stored both in the DB and in whoosh, create a Movie"""
        return cls(
            model.id,
            whoosh_movie["title"],
            model.poster_url,
            whoosh_movie["release_year"],
            model.duration,
            model.rating,
            whoosh_movie["plot"],
            [director.name for director in model.directors.all()],
            [genre.name for genre in model.genres.all()],
        )
