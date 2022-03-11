from django.db import models

class Artist(models.Model):
    '''Artist model'''
    title = models.CharField(max_length=220)
    picture = models.ImageField(upload_to='ArtistsPictures/', default='ArtistsPictures/default.jpg')
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title