import joblib


class AnalyzeReviewFromText:
    model = None

    def __init__(self):
        if AnalyzeReviewFromText.model is None:
            AnalyzeReviewFromText.model = joblib.load("model.joblib")

    def analyze(self, text: str) -> bool:
        return bool(AnalyzeReviewFromText.model.predict([text])[0])
