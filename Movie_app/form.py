from django import forms
from .models import Movie_data

class Movie_form(forms.ModelForm):
    class Meta:
        model = Movie_data
        fields = ['name', 'desc', 'release_date', 'actors', 'youtube_link', 'poster']