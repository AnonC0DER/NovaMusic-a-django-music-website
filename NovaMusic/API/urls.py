from django.urls import path
from API.views import AlbumViewset, MusicViewset, ArtistViewset, GenreViewset

urlpatterns = [
    path('genres/', GenreViewset.as_view()),
    path('genre/<pk>/', GenreViewset.as_view()),
    path('artists/', ArtistViewset.as_view()),
    path('artist/<pk>/', ArtistViewset.as_view()),
    path('albums/', AlbumViewset.as_view()),
    path('album/<pk>/', AlbumViewset.as_view()),
    path('songs/', MusicViewset.as_view()),
    path('song/<pk>/', MusicViewset.as_view()),
]