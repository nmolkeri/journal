from django import forms
from .models import Album, Musician
from django.forms import ModelForm

class MusicianForm(forms.ModelForm):
        class Meta:
                model = Musician
                fields = ["first_name","last_name", "instrument"]

class AlbumForm(forms.ModelForm):
        class Meta:
                model = Album
                fields = ["name","artist", "release_date","num_stars"]

