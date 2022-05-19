from webpage.entities.movie import Movie
from webpage.repositories import whoosh_repository
from webpage.repositories.sqlite_repository import SQLiteRepository


def filter_movies_by_field(field: str, value: str) -> list[Movie]:
    repository = SQLiteRepository()
    movies = None
    if field == "release_year":
        whoosh_movies_id = [
            movie["movie_id"]
            for movie in whoosh_repository.get_movies_from_release_year(value)
        ]
        movies = [repository.retrieve_movie_by_id(id) for id in whoosh_movies_id]

    if field in {"genres", "directors"}:
        movies = repository.filter_movies_by_many_to_many_field(field, value)
    if movies is not None:
        return movies
    return None
