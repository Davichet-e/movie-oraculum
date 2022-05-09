from dataclasses import dataclass
import datetime


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
