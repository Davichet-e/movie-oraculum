import bs4
import httpx


def obtain_review_from_url(url: str) -> str:
    response = httpx.get(url, follow_redirects=True)
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    return soup.select_one(".content .text").text
