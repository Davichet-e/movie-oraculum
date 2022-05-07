from webpage.models import Movie
from webpage.entities.movie_repository import MovieRepository


class SQLiteRepository(MovieRepository):
    def trending_movies(self) -> list[Movie]:
        return list(Movie.objects.filter(trending=True))
