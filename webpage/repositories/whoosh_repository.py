import os.path
from typing import TypedDict

from whoosh.fields import ID, TEXT, Schema, NUMERIC
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser


class WhooshMovie(TypedDict):
    movie_id: str
    title: str
    plot: str
    release_year: int


schema = Schema(
    movie_id=ID(stored=True),
    title=TEXT(stored=True),
    plot=TEXT(stored=True),
    release_year=NUMERIC(stored=True),
)
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
    ix = create_in("indexdir", schema)
else:
    ix = open_dir("indexdir")


def get_movie(movie_id: str) -> WhooshMovie:
    parser = QueryParser("movie_id", schema=schema)
    query = parser.parse(movie_id)
    with ix.searcher() as searcher:
        return dict(searcher.search(query, limit=1)[0])


def search_movies(
    title: str | None, plot: str | None, until_release_year: int | None
) -> list[WhooshMovie]:
    """Return the WhoosMovies that accomplish all conditions represented by each parameter."""
    parser = QueryParser("title", schema=schema)

    query_string = ""
    if title:
        query_string = f"{title} "
    if plot:
        query_string += f"plot:{plot} "
    if until_release_year:
        query_string += f"release_year:[TO {until_release_year}]"

    query = parser.parse(query_string)
    with ix.searcher() as searcher:
        return list(map(dict, searcher.search(query)))


def write_movie(movie_id: str, title: str, plot: str, release_year: int) -> None:
    writer = ix.writer()

    writer.add_document(
        movie_id=movie_id, title=title, plot=plot, release_year=release_year
    )
    writer.commit()


def get_movies_from_release_year(release_year: str) -> list[WhooshMovie]:
    parser = QueryParser("release_year", schema=schema)
    query = parser.parse(release_year)
    with ix.searcher() as searcher:
        return list(map(dict, searcher.search(query, limit=None)))
