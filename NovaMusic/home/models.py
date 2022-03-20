from django.db import models

class HomePagePoster(models.Model):
    '''Home page model'''
    title = models.CharField(max_length=220)
    description = models.TextField(null=True, blank=True, max_length=350)
    poster = models.ImageField(upload_to='Posters/')
    albums_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title