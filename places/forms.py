from django import forms
from .models import Place 
from django.forms import ModelForm

class PlaceForm(forms.ModelForm):
        class Meta:
                model = Place
                fields = ["name", "country", "reason","international_domestic", "visit_date", "attraction", "description"]

