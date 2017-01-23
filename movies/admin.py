from django.contrib import admin
from movies.models import Movie, Category

class MovieAdmin(admin.ModelAdmin):
	prepopulated_fields = {'comment':('name',)}
	list_display = ('name', 'year', 'category')
	search_fields=['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
# Register your models here.
