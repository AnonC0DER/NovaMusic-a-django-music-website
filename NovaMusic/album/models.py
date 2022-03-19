from django.db import models
from django.contrib.auth import get_user_model
from artist.models import Artist
from core.models import Comment

class Album(models.Model):
    '''Album model'''
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    artists = models.ManyToManyField(Artist)
    album_image = models.ImageField(upload_to='AlbumsImages/', default='AlbumsImages/default.jpg')
    album_download_link_high = models.CharField(max_length=350, null=True, blank=True)
    album_download_link_high_file = models.FileField(upload_to='AlbumsZipHigh/', null=True, blank=True)
    album_download_link_medium = models.CharField(max_length=350, null=True, blank=True)
    album_download_link_medium_file = models.FileField(upload_to='AlbumsZipMedium/', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    release_time = models.DateField(null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AlbumComment(Comment):
    '''Album comment model inherit from main Comment model'''
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def comment_title(self):
        return f'Comment on {self.album} by {self.owner.name if self.owner.name else self.owner.email}'