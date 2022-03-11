from django.apps import AppConfig


class GenreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'genre'

    def ready(self):
        import genre.signals