from webpage.entities.movie import Movie
from webpage.repositories.sqlite_repository import SQLiteRepository
from webpage.use_cases.exceptions import RetrievalException
from webpage.use_cases.parse_model_to_entity import parse_model_to_entity_movie
from webpage.use_cases.retrieve_movie_from_web import retrieve_movie_from_web

def retrieve_movie(movie_id: str) -> Movie | None:
    repository = SQLiteRepository()
    movie = repository.retrieve_movie_by_id(movie_id)

    if movie is None:
        try:
            movie = retrieve_movie_from_web(movie_id)
        except RetrievalException:
            return None

        repository.create_movie_from_retrieved_movie(movie)
    
    else:

        movie = parse_model_to_entity_movie(movie)

    return movie


   