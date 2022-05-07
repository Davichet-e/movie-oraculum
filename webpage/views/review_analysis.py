from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from webpage.forms import ReviewForm
from webpage.use_cases.analyze_review_from_text import AnalyzeReviewFromText
from webpage.use_cases.analyze_review_from_url import analyze_review_from_url


class ReviewAnalysisView(View):
    form_class = ReviewForm
    template_name = "webpage/review_analysis.html"
    review_analysed_template_name = "webpage/review_analyzed.html"

    def get(self, request: HttpRequest):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data["url"]:
                text, is_review_positive = analyze_review_from_url(
                    form.cleaned_data["url"]
                )
            else:
                text = form.cleaned_data["message"]
                use_case = AnalyzeReviewFromText()
                is_review_positive = use_case.analyze(text)

            return render(
                request,
                self.review_analysed_template_name,
                {"text": text, "is_review_positive": is_review_positive},
            )
