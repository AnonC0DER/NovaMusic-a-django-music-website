from django.urls import path
from music import views

urlpatterns = [
    path('songs/', views.SongsPage, name='songs'),
    path('song/<slug>-ID-<pk>/', views.SingleSongPage, name='single-song'),
]