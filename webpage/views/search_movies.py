from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from webpage.forms import SearchForm
from webpage.repositories import whoosh_repository
from webpage.use_cases.search_movies import search_movies


class SearchMovieView(View):
    form_class = SearchForm
    template_name = "webpage/search_movies.html"
    review_analysed_template_name = "webpage/search_results.html"

    def get(self, request: HttpRequest):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest):
        form = self.form_class(request.POST)
        if form.is_valid():
            movies = search_movies(
                form.cleaned_data["title"],
                form.cleaned_data["plot"],
                form.cleaned_data["until_release_year"],
            )

            return render(
                request,
                self.review_analysed_template_name,
                {"movies": movies},
            )
