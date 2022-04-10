import bs4
import httpx


URL = "https://www.imdb.com/title/tt5108870/"

response = httpx.get(URL)

soup = bs4.BeautifulSoup(response.content, "html.parser")

is_series = (
    soup.select_one('[data-testid="hero-subnav-bar-series-episode-count"]') is not None
)

title = soup.select_one('[data-testid="hero-title-block__title"]').string

metadata = soup.select_one('[data-testid="hero-title-block__metadata"]')
release_year = metadata.select_one("li:first-child a").get_text()
duration = metadata.select_one("li:nth-child(3)").get_text()

rating = float(
    soup.select_one(
        '[data-testid="hero-rating-bar__aggregate-rating__score"] span'
    ).string
)

plot = soup.select_one('[data-testid="plot-xl"]').string

directors = {
    tag.string
    for tag in soup.select('[data-testid="title-pc-principal-credit"]:first-child li')
}

genres = [tag.string for tag in soup.select('[data-testid="storyline-genres"] li')]


print(
    f"{is_series=}, {title=}, {release_year=}, {duration=}, {rating=}\n"
    f"{plot=}\n{directors=}, {genres=}"
)
