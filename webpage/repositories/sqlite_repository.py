from django.core.exceptions import ObjectDoesNotExist
from webpage.entities.movie import Movie, RetrievedMovie
from webpage.entities.movie_repository import MovieRepository
from webpage import models
from webpage.repositories import whoosh_repository
from webpage.repositories.whoosh_repository import get_movie
from django.db.models import QuerySet


class SQLiteRepository(MovieRepository):
    def retrieve_movie_by_id(self, movie_id: str) -> models.Movie | None:
        try:
            movie = models.Movie.objects.get(pk=movie_id)
            return Movie.from_model_and_whoosh_movie(movie, get_movie(movie.id))
        except ObjectDoesNotExist:
            return None

    def create_movie_from_retrieved_movie(
        self, retrieved_movie: RetrievedMovie
    ) -> None:
    
        whoosh_repository.write_movie(
            retrieved_movie.movie_id,
            retrieved_movie.title,
            retrieved_movie.plot,
            retrieved_movie.release_year,
        )
        models.Movie.from_retrieved_movie(retrieved_movie)

    def filter_movies_by_int_field(self, field: str, value: int) -> list[Movie]:
        return self._parse_models_to_movies(
            models.Movie.objects.filter(**{field: value})
        )

    def filter_movies_by_many_to_many_field(
        self, field: str, value: str
    ) -> list[Movie]:
        return self._parse_models_to_movies(
            models.Movie.objects.filter(**{f"{field}__name": value})
        )

    @staticmethod
    def _parse_models_to_movies(movie_models: QuerySet) -> list[Movie]:
        return [
            Movie.from_model_and_whoosh_movie(movie, get_movie(movie.id))
            for movie in movie_models
        ]
