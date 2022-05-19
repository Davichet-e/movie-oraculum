from django import forms


class ReviewForm(forms.Form):
    url = forms.URLField(label="Url of the IMDb review", required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)


class SearchForm(forms.Form):
    title = forms.CharField(required=False)
    plot = forms.CharField(widget=forms.Textarea, required=False)
    until_release_year = forms.IntegerField(required=False, min_value=1)
