from django.db import models

class Genre(models.Model):
    '''Genre model'''
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to='GenrePosters/', default='GenrePosters/default.jpg')
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title