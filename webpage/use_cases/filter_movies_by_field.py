from webpage.entities.movie import Movie
from webpage.repositories.sqlite_repository import SQLiteRepository
from webpage.use_cases.parse_model_to_entity import parse_model_to_entity_movie


def filter_movies_by_field(field: str, value: str) -> list[Movie]:
    repository = SQLiteRepository()
    movies = None
    if field == "release_year":
        movies = repository.filter_movies_by_int_field(field, int(value))

    if field in {"genres", "directors"}:
        movies = repository.filter_movies_by_many_to_many_field(field, value)
    if movies is not None:
        return [parse_model_to_entity_movie(movie) for movie in movies]
    return None
