from typing import Iterator

import bs4
import httpx
from webpage.entities.movie import RetrievedMovie
from webpage.use_cases.retrieve_movie import retrieve_movie
from webpage.utils.constants import BASE_URL


def retrieve_most_popular_movies() -> Iterator[RetrievedMovie]:
    url = BASE_URL + "/chart/moviemeter/"
    response = httpx.get(url)

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    links = [BASE_URL + tag["href"] for tag in soup.select("td.titleColumn a")[:10]]
    return map(retrieve_movie, links)
