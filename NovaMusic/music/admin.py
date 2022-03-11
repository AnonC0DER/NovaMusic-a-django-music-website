from django.contrib import admin
from music.models import Music

class MusicAdmin(admin.ModelAdmin):
    '''Music admin page'''
    list_display = ['title', 'published', 'id']
    search_fields = ['title']
    list_filter = ['published']

admin.site.register(Music, MusicAdmin)