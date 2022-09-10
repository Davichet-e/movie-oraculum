from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from webpage.forms import RecommendForm
from webpage.use_cases.recommend_movie import recommend_movie
from webpage.use_cases.retrieve_movie import retrieve_movie


class RecommendAnalysisView(View):
    form_class = RecommendForm
    template_name = "webpage/recommend_movie.html"
    movies_recommended_template_name = "webpage/movies_recommended.html"

    def get(self, request: HttpRequest):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest):
        form = self.form_class(request.POST)
        if form.is_valid():
            film = form.cleaned_data["film"]
            movies_recommended = list(map(retrieve_movie, recommend_movie(film)))

            return render(
                request,
                self.movies_recommended_template_name,
                {"movies_recommended": movies_recommended},
            )
