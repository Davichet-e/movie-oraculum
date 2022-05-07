import datetime
import bs4
import httpx

from webpage.entities.movie import RetrievedMovie
from webpage.use_cases.exceptions import RetrievalException


def retrieve_movie(url: str) -> RetrievedMovie:
    response = httpx.get(url)

    if not response.is_success:
        raise RetrievalException(response.status_code)
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    imdb_id = url.split("/")[
        4
    ]  # URL format: https://www.imdb.com/title/imdb_id_of_movie/

    title = soup.select_one('[data-testid="hero-title-block__title"]').string

    poster_url = soup.select_one(".ipc-poster__poster-image img")["src"]

    metadata = soup.select_one('[data-testid="hero-title-block__metadata"]')

    release_year = int(metadata.select_one("li:first-child a").text)

    duration_element = metadata.select_one("li:nth-child(3)")
    if duration_element is None:
        duration = None
    else:
        duration = parse_duration(duration_element.text)

    rating_element = soup.select_one(
        '[data-testid="hero-rating-bar__aggregate-rating__score"] span'
    )
    if rating_element is None:
        rating = None
    else:
        rating = float(rating_element.string)

    plot = soup.select_one('[data-testid="plot-xl"]').string

    directors = list(
        {
            tag.string
            for tag in soup.select(
                '[data-testid="title-pc-principal-credit"]:first-child li'
            )
        }
    )

    genres = [tag.string for tag in soup.select('[data-testid="storyline-genres"] li')]
    if (
        len(genres) == 0
        and soup.select_one("[data-testid='storyline-loader']") is not None
    ):
        genres = None
    # pylint: disable=too-many-function-args
    return RetrievedMovie(
        imdb_id,
        title,
        poster_url,
        release_year,
        duration,
        rating,
        plot,
        directors,
        genres,
    )


def parse_duration(duration: str) -> datetime.timedelta:
    try:
        date = datetime.datetime.strptime(duration, "%Hh %Mm")
        return datetime.timedelta(hours=date.hour, minutes=date.minute)

    except ValueError:
        try:
            date = datetime.datetime.strptime(duration, "%Mm")
            return datetime.timedelta(minutes=date.minute)

        except ValueError:
            date = datetime.datetime.strptime(duration, "%Hh")
            return datetime.timedelta(hours=date.hour)
