from django.shortcuts import render
from genre.models import Genre
from music.models import Music

def GenrePage(request, slug, pk):
    '''Filter songs by each genre page view'''
    get_genre = Genre.objects.get(slug=slug, id=pk)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    fitler_songs = Music.objects.filter(published=True, genres=get_genre)
    context = {'genre' : get_genre, 'songs' : fitler_songs, 'player' : new_song_for_player}

    return render(request, 'genre/genre.html', context)