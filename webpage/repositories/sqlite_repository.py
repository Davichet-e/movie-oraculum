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

    def filter_movies_by_int_field(self, field: str, value: int) -> list[Movie]:
        return Movie.objects.filter(**{field: value})

    def filter_movies_by_many_to_many_field(
        self, field: str, value: str
    ) -> list[Movie]:
        return Movie.objects.filter(**{f"{field}__name": value})
