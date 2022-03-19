from django.contrib import admin
from album.models import Album, AlbumComment

class AlbumAdmin(admin.ModelAdmin):
    '''Album admin page'''
    list_display = ['title', 'published', 'id']
    search_fields = ['title']
    list_filter = ['published']


class AlbumCommentAdmin(admin.ModelAdmin):
    '''Music comment admin page'''
    list_display = ['comment_title', 'active', 'owner', 'album']
    search_fields = ['owner__email', 'owner__name', 'album__title']
    list_filter = ['active']


admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumComment, AlbumCommentAdmin)