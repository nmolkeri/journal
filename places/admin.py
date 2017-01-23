from django.contrib import admin
from places.models import Place

class PlaceAdmin(admin.ModelAdmin):
        list_display = ('name', 'country', 'reason','international_domestic', 'visit_date', 'attraction', 'description')
        search_fields=['name']



admin.site.register(Place)

