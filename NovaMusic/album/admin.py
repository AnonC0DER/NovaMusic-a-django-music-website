from django.contrib import admin
from album.models import Album

class AlbumAdmin(admin.ModelAdmin):
    '''Album admin page'''
    list_display = ['title', 'published', 'id']
    search_fields = ['title']
    list_filter = ['published']

admin.site.register(Album, AlbumAdmin)