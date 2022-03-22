from django.shortcuts import render
from artist.models import Artist
from album.models import Album
from genre.models import Genre
from music.models import Music
from artist.utils import Search

def ArtistsPage(request):
    get_artists = Search(request)
    get_genres = Genre.objects.all()
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {
        'artists' : get_artists,
        'genres' : get_genres,
        'player' : new_song_for_player
    }

    return render(request, 'artist/artists.html', context)


def SignleArtistPage(request, pk, slug):
    get_artist = Artist.objects.get(id=pk, slug=slug)
    get_artist_albums = Album.objects.filter(artists=get_artist)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {
        'artist' : get_artist,
        'albums' : get_artist_albums,
        'player' : new_song_for_player
    }

    return render(request, 'artist/single-artist.html', context)