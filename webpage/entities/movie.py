from dataclasses import dataclass
import datetime


@dataclass(frozen=True)
class RetrievedMovie:
    """Represent the movie extracted from the webpage."""

    imdb_id: str
    title: str
    poster_url: str
    release_year: int
    duration: datetime.timedelta | None
    rating: float | None
    plot: str

    directors: list[str]
    genres: list[str] | None

    # trending: bool # True if film is currently at https://www.imdb.com/chart/moviemeter/


@dataclass
class Movie:
    title: str
    release_year: int
    duration: datetime.timedelta
    rating: float
    plot: str

    directors: list[str]
    genres: list[str]
