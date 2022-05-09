from webpage.entities.movie import Movie
from webpage.repositories.sqlite_repository import SQLiteRepository
from webpage.use_cases.exceptions import RetrievalException
from webpage.use_cases.retrieve_movie_from_web import retrieve_movie_from_web
from webpage import models
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
        def parse_model_to_entity_movie(movie: models.Movie) -> Movie:
            return Movie(
                movie.id,
                movie.title,
                movie.poster_url,
                movie.release_year,
                movie.duration,
                movie.rating,
                movie.plot,

                [director.name for director in movie.directors.all()],
                [genre.name for genre in movie.genres.all()],
            )
        movie = parse_model_to_entity_movie(movie)

    return movie


   