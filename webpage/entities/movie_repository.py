import abc
from webpage.entities.movie import RetrievedMovie

from webpage.models import Movie


class MovieRepository(abc.ABC):
    @abc.abstractmethod
    def retrieve_movie_by_id(self, movie_id: str) -> Movie:
        ...

    @abc.abstractmethod
    def create_movie_from_retrieved_movie(
        self, retrieved_movie: RetrievedMovie
    ) -> None:
        ...

    @abc.abstractmethod
    def filter_movies_by_int_field(self, field: str, value: int) -> list[Movie]:
        ...

    @abc.abstractmethod
    def filter_movies_by_many_to_many_field(
        self, field: str, value: str
    ) -> list[Movie]:
        ...
