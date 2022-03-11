from django.contrib import admin
from genre.models import Genre

class GenreAdmin(admin.ModelAdmin):
    '''Genre admin page'''
    list_display = ['title', 'id']
    search_fields = ['title']

admin.site.register(Genre, GenreAdmin)