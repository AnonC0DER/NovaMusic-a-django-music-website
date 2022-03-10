from django.db import models

class Album(models.Model):
    '''Album model'''
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    album_image = models.ImageField(upload_to='AlbumsImages/', default='AlbumsImages/default.jpg')
    album_download_link_high = models.CharField(max_length=350, null=True, blank=True)
    album_download_link_medium = models.CharField(max_length=350, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    release_time = models.DateField(null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title