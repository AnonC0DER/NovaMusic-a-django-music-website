from django.contrib import admin
from music.models import Music

class MusicAdmin(admin.ModelAdmin):
    '''Music admin page'''
    list_display = ['title', 'get_album_name', 'published', 'id']
    search_fields = ['title']
    list_filter = ['published']
    readonly_fields = ['get_album_name', 'id']

admin.site.register(Music, MusicAdmin)