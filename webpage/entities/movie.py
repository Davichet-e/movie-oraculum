from dataclasses import dataclass
import datetime


@dataclass
class RetrievedMovie:
    """Represent the movie extracted from the webpage."""
    title: str
    release_year: int
    duration: datetime.timedelta
    rating: float
    plot: str

    directors: list[str]
    genres: list[str]


@dataclass
class Movie:
    title: str
    release_year: int
    duration: datetime.timedelta
    rating: float
    plot: str

    directors: list[str]
    genres: list[str]
