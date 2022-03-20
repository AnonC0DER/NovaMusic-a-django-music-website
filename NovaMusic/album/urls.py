from django.urls import path
from album import views

urlpatterns = [
    path('albums/', views.AlbumsPage, name='albums'),
    path('album/<slug>-ID-<pk>/', views.SingleAlbumPage, name='single-album')
]