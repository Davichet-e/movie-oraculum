import abc
from webpage.models import Movie

class MovieRepository(abc.ABC):
    @abc.abstractmethod
    def trending_movies(self) -> list[Movie]:
        ...