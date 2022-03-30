from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from album.models import Album
from music.models import Music
from genre.models import Genre
from artist.models import Artist
from API.serializers import AlbumSerializer, MusicSerializer, ArtistSerializer, GenreSerializer

class AlbumViewset(APIView):
    '''Album view set'''
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


class GenreViewset(APIView):
    '''Genre view set'''
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class ArtistViewset(APIView):
    '''Artist view set'''
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)


class MusicViewset(APIView):
    '''Music view set'''
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        music = Music.objects.all()
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data)