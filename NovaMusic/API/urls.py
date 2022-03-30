from django.urls import path
from API.views import AlbumViewset, MusicViewset, ArtistViewset, GenreViewset

urlpatterns = [
    path('genres/', GenreViewset.as_view()),
    path('artists/', ArtistViewset.as_view()),
    path('albums/', AlbumViewset.as_view()),
    path('songs/', MusicViewset.as_view())
]