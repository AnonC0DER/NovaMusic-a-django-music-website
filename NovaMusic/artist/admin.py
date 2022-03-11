from django.contrib import admin
from artist.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    '''Artist admin page'''
    list_display = ['title', 'id']
    search_fields = ['title']

admin.site.register(Artist, ArtistAdmin)