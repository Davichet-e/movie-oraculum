from django.core.exceptions import ObjectDoesNotExist
from webpage.entities.movie import RetrievedMovie
from webpage.entities.movie_repository import MovieRepository
from webpage.models import Movie


class SQLiteRepository(MovieRepository):
    def retrieve_movie_by_id(self, movie_id: str) -> Movie | None:
        try:
            return Movie.objects.get(pk=movie_id)
        except ObjectDoesNotExist:
            return None

    def create_movie_from_retrieved_movie(
        self, retrieved_movie: RetrievedMovie
    ) -> None:
        Movie.from_retrieved_movie(retrieved_movie)
