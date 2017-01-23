from django.contrib import admin
from music.models import Musician, Album

class AlbumAdmin(admin.ModelAdmin):
        list_display = ('artist', 'name', 'release_date', 'num_stars')
        search_fields=['artist']



admin.site.register(Musician)
admin.site.register(Album)
