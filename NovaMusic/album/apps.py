from django.apps import AppConfig


class AlbumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'album'

    def ready(self):
        import album.signals