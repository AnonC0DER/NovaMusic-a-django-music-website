from django.db.models import Q 
from music.models import Music
from artist.models import Artist
from album.models import Album
from genre.models import Genre

def Search(reqeust):
    '''Search function view (music, albums, artists and genres)'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')
    
    music = Music.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(lyrics__icontains=search_query)
    )
    artist = Artist.objects.distinct().filter(
        Q(title__icontains=search_query)
    )
    album = Album.objects.distinct().filter(
        Q(title__icontains=search_query)
    )
    genre = Genre.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return music, artist, album, genre