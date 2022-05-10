from webpage import models
from webpage.entities.movie import Movie


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