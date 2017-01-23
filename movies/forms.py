from django import forms
from .models import Movie, Category
from django.forms import ModelForm

class CategoryForm(forms.ModelForm):
        class Meta:
                model = Category
                fields = ["name","description"]

class MoviesForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ["name","category", "year","rating", "comment"]
