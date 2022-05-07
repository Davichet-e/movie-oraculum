from webpage.use_cases.analyze_review_from_text import (
    AnalyzeReviewFromText,
)
from webpage.use_cases.obtain_review_from_url import obtain_review_from_url


def analyze_review_from_url(url: str) -> tuple[str, bool]:
    "Return the text of the review and whether the review is positive or not"
    review = obtain_review_from_url(url)
    use_case = AnalyzeReviewFromText()
    return review, use_case.analyze(review)
