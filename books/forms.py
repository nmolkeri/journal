from django import forms
from .models import Book
from django.forms import ModelForm

class BookForm(forms.ModelForm):
        class Meta:
                model = Book
                fields = ["name", "author", "year", "read_date", "category", "comment"]
