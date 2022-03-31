from django.urls import path
from API.views import (
    AllApisUrlsView, AlbumView, 
    MusicView, ArtistView, 
    GenreView, UploadMusicView,
    UploadAlbumView
)

urlpatterns = [
<<<<<<< Updated upstream
    path('genres/', GenreViewset.as_view()),
    path('artists/', ArtistViewset.as_view()),
    path('albums/', AlbumViewset.as_view()),
    path('songs/', MusicViewset.as_view())
=======
    path('', AllApisUrlsView.as_view()),
    path('genres/', GenreView.as_view()),
    path('genre/<pk>/', GenreView.as_view()),
    path('artists/', ArtistView.as_view()),
    path('artist/<pk>/', ArtistView.as_view()),
    path('albums/', AlbumView.as_view()),
    path('album/<pk>/', AlbumView.as_view()),
    path('songs/', MusicView.as_view()),
    path('song/<pk>/', MusicView.as_view()),

    path('upload-music/', UploadMusicView.as_view()),
    path('upload-album/', UploadAlbumView.as_view()),
>>>>>>> Stashed changes
]