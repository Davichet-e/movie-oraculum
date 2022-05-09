import bs4
import httpx
from webpage.entities.movie import RetrievedMovie
from webpage.use_cases.retrieve_movie_from_web import retrieve_movie_from_web
from webpage.utils.constants import BASE_URL


def retrieve_most_popular_movies(*, trending: bool) -> list[RetrievedMovie]:
    """Return most popular movies from IMDb.

    :param trending: if true, return the most popular movies of the moment (trending), if false, return the most popular movies of all time.
    """
    # movies_from_db = retrieve_most_popular_movies_from_db(trending)
    # if movies_from_db is not None:
    #     return movies_from_db

    url = f"{BASE_URL}/chart/{'moviemeter' if trending else 'top'}/"
    response = httpx.get(url)

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    def get_movie_id_from_href(href: str) -> str:
        return href.split("/", maxsplit=3)[2]  # /title/<movie_id>/ -> <movie_id>

    links = [
        get_movie_id_from_href(tag["href"])
        for tag in soup.select("td.titleColumn a")[:5]
    ]
    return [retrieve_movie_from_web(link) for link in links]
