"""
Module containing the possible exceptions occurred
"""


class RetrievalException(Exception):
    """Represent an error during the retrieval of a resource"""

    def __init__(self, status_code: int) -> None:
        super().__init__(
            "During retrieval of a resource, "
            f"a response with status code {status_code} ocurred."
        )
