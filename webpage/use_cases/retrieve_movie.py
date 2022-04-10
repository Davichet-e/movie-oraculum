import datetime
import bs4
import httpx

from webpage.entities.movie import RetrievedMovie


def retrieve_movie(url: str) -> RetrievedMovie:

    response = httpx.get(url)

    soup = bs4.BeautifulSoup(response.content, "html.parser")

    # is_series = (
    #     soup.select_one('[data-testid="hero-subnav-bar-series-episode-count"]')
    #     is not None
    # )

    title = soup.select_one('[data-testid="hero-title-block__title"]').string

    metadata = soup.select_one('[data-testid="hero-title-block__metadata"]')
    release_year = metadata.select_one("li:first-child a").text
    duration_as_str = metadata.select_one("li:nth-child(3)").text

    def parse_duration(duration: str) -> datetime.timedelta:
        try:
            date = datetime.datetime.strptime(duration, "%Hh %Mm")
            return datetime.timedelta(hours=date.hour, minutes=date.minute)
        except ValueError:
            try:
                date = datetime.datetime.strptime(duration, "%Mm")
                return datetime.timedelta(minutes=date.minute)
            except ValueError:
                datetime.datetime.strptime(duration, "%Hh")
                return datetime.timedelta(hours=date.hour)

    duration = parse_duration(duration_as_str)

    rating = float(
        soup.select_one(
            '[data-testid="hero-rating-bar__aggregate-rating__score"] span'
        ).string
    )

    plot = soup.select_one('[data-testid="plot-xl"]').string

    directors = {
        tag.string
        for tag in soup.select(
            '[data-testid="title-pc-principal-credit"]:first-child li'
        )
    }

    genres = [tag.string for tag in soup.select('[data-testid="storyline-genres"] li')]

    return RetrievedMovie(
        title, release_year, duration, rating, plot, directors, genres
    )
