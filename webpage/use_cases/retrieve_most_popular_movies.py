import bs4
import httpx
from webpage.entities.movie import RetrievedMovie
from webpage.use_cases.retrieve_most_popular_movies_from_db import (
    retrieve_most_popular_movies_from_db,
)
from webpage.use_cases.retrieve_movie import retrieve_movie
from webpage.utils.constants import BASE_URL


def retrieve_most_popular_movies(*, trending: bool) -> list[RetrievedMovie]:
    """Return most popular movies from IMDb.

    :param trending: if true, return the most popular movies of the moment (trending), if false, return the most popular movies of all time.
    """
    # movies_from_db = retrieve_most_popular_movies_from_db(trending)
    # if movies_from_db is not None:
    #     return movies_from_db

    url = BASE_URL + f"/chart/{'moviemeter' if trending else 'top'}/"
    response = httpx.get(url)

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    links = [BASE_URL + tag["href"] for tag in soup.select("td.titleColumn a")[:5]]
    return [retrieve_movie(link) for link in links]
