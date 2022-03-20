from django.shortcuts import render
from genre.models import Genre
from album.models import Album
from music.models import Music
from home.models import HomePagePoster as Poster
from artist.models import Artist
from home.utils import Search

def HomePage(request):
    '''Home page view'''
    posters = Poster.objects.all()
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    get_genres = Genre.objects.all()
    get_songs = Music.objects.filter(published=True).order_by('-created')[:5]
    get_single_songs = Music.objects.filter(published=True, single_track=True).order_by('-created')[:5]
    get_top_songs = Music.objects.filter(published=True).order_by('page_view')[:5]
    get_newest_albums = Album.objects.filter(published=True).order_by('-created')[:6]
    get_artists = Artist.objects.all().order_by('-created')[:12]

    context = {
        'new_albums' : get_newest_albums,
        'genres' : get_genres,
        'artists' : get_artists,
        'songs' : get_songs,
        'singles' : get_single_songs,
        'top_songs' : get_top_songs,
        'player' : new_song_for_player,
        'posters' : posters
    }
    return render(request, 'home/home.html', context)


def SearchPage(request):
    '''Search page view'''
    music, artist, album, genre = Search(request)
    context = {
        'songs' : music[:12],
        'artists' : artist[:12],
        'albums' : album[:12],
        'genres' : genre[:12],
        'query' : request.GET.get('query')
    }
    return render(request, 'home/search.html', context)