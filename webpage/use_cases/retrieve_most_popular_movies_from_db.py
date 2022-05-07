from webpage.repositories.sqlite_repository import SQLiteRepository


def retrieve_most_popular_movies_from_db(trending: bool):
    repository = SQLiteRepository()
    return repository.trending_movies()
