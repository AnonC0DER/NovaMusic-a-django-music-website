from django.urls import path
from artist import views

urlpatterns = [
    path('artists/', views.ArtistsPage, name='artists'),
    path('artist/<slug>-ID-<pk>/', views.SignleArtistPage, name='single-artist')
]