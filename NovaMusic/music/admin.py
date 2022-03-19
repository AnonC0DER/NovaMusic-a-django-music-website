from django.contrib import admin
from music.models import Music, MusicComment

class MusicAdmin(admin.ModelAdmin):
    '''Music admin page'''
    list_display = ['title', 'get_album_name', 'published', 'id']
    search_fields = ['title']
    list_filter = ['published']
    readonly_fields = ['get_album_name', 'id']


class MusicCommentAdmin(admin.ModelAdmin):
    '''Music comment admin page'''
    list_display = ['comment_title', 'active', 'owner', 'music']
    search_fields = ['owner__email', 'owner__name', 'music__title']
    list_filter = ['active']


admin.site.register(Music, MusicAdmin)
admin.site.register(MusicComment, MusicCommentAdmin)