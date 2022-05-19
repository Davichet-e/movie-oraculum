from webpage.entities.movie import Movie
from webpage.repositories import whoosh_repository
from webpage.repositories.sqlite_repository import SQLiteRepository


def search_movies(
    title: str | None, plot: str | None, until_release_year: int | None
) -> list[Movie]:
    repository = SQLiteRepository()
    whoosh_movies_id = [
        movie["movie_id"]
        for movie in whoosh_repository.search_movies(title, plot, until_release_year)
    ]
    return [repository.retrieve_movie_by_id(id) for id in whoosh_movies_id]
