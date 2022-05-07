from django import forms


class ReviewForm(forms.Form):
    url = forms.URLField(label="Url of the IMDb review", required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
