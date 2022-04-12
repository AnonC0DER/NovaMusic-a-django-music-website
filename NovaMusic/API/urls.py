from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from API.views import (
    AllApisUrlsView, AlbumView, 
    MusicView, ArtistView, 
    GenreView, UploadMusicView,
    UploadAlbumView, CheckJWT
)

urlpatterns = [
    path('', AllApisUrlsView.as_view()),
    path('genres/', GenreView.as_view()),
    path('genres/search/<query>/', GenreView.as_view()),
    path('genre/<pk>/', GenreView.as_view()),
    path('artists/', ArtistView.as_view()),
    path('artists/search/<query>/', ArtistView.as_view()),
    path('artist/<pk>/', ArtistView.as_view()),
    path('albums/', AlbumView.as_view()),
    path('albums/search/<query>/', AlbumView.as_view()),
    path('album/<pk>/', AlbumView.as_view()),
    path('songs/', MusicView.as_view()),
    path('songs/search/<query>/', MusicView.as_view()),
    path('song/<pk>/', MusicView.as_view()),

    path('upload-music/', UploadMusicView.as_view()),
    path('upload-album/', UploadAlbumView.as_view()),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/check-token/', CheckJWT.as_view()),

    path('docs/', include_docs_urls(title='NovaMusic-APIs')),
]