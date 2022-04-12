from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import generics
from album.models import Album
from music.models import Music
from genre.models import Genre
from artist.models import Artist
from API.serializers import (
    AlbumSerializer, MusicSerializer,
    ArtistSerializer, GenreSerializer, 
    UploadMusicSerializer, UploadAlbumSerializer
)

class AllApisUrlsView(APIView):
    '''All Apis'''
    def get(self, request, format=None):
        Urls = {
            'GET' : {
                'Albums' : '/api/albums/',
                'Search albums' : '/api/albums/search/QUERY/',
                'Single album' : '/api/album/ID/',
                'Songs' : '/api/songs/',
                'Search Songs' : '/api/songs/search/QUERY/',
                'Single song' : '/api/song/ID/',
                'Artists' : '/api/artists/',
                'Search Artists' : '/api/artists/search/QUERY/',
                'Single artist' : '/api/artist/ID/',
                'Genres' : '/api/genres/',
                'Search Genres' : '/api/genres/search/QUERY/',
                'Single genre' : '/api/genre/ID/',
                'NovaMusic APIs documentation' : '/api/docs/'
            },

            'POST' : {
                'Upload album' : '/api/upload-album/',
                'Upload music' : '/api/upload-music/',
                'Check JWT token' : '/api/users/check-token/',
                'Get user token' : '/api/users/token/',
                'Refresh token' : '/api/users/token/refresh/',
            }
        }

        return Response(Urls)


class AlbumView(APIView):
    '''To get single album details, use this url : /album/ID/'''
    permission_classes = (IsAdminUser, )
    
    def get(self, request, pk=None, query=None, format=None):
        if query:
            albums = Album.objects.filter(published=True, title__icontains=query)
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)

        if pk:
            album = Album.objects.get(id=pk)
            serializer = AlbumSerializer(album, many=False)
            return Response(serializer.data)

        else:
            albums = Album.objects.filter(published=True)
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)

          
class GenreView(APIView):
    '''To get single genre details, use this url : /genre/ID/'''
    def get(self, request, pk=None, query=None, format=None):
        if query:
            genres = Genre.objects.filter(title__icontains=query)
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)

        if pk:
            genre = Genre.objects.get(id=pk)
            serializer = GenreSerializer(genre, many=False)
            return Response(serializer.data)

        else:
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return Response(serializer.data)


class ArtistView(APIView):
    '''To get single artist details, use this url : /artist/ID/'''
    def get(self, request, pk=None, query=None, format=None):
        if query:
            artists = Artist.objects.filter(title__icontains=query)
            serializer = ArtistSerializer(artists, many=True)
            return Response(serializer.data)

        if pk:
            artist = Artist.objects.get(id=pk)
            serializer = ArtistSerializer(artist, many=False)
            return Response(serializer.data)

        else:
            artists = Artist.objects.all()
            serializer = ArtistSerializer(artists, many=True)
            return Response(serializer.data)


class MusicView(APIView):
    '''To get single song details, use this url : /song/ID/'''
    permission_classes = (IsAdminUser, )
    
    def get(self, request, pk=None, query=None, format=None):
        if query:
            music = Music.objects.filter(title__icontains=query)
            serializer = MusicSerializer(music, many=True)
            return Response(serializer.data)

        if pk:
            music = Music.objects.get(id=pk)
            serializer = MusicSerializer(music, many=False)
            return Response(serializer.data)

        else:
            music = Music.objects.filter(published=True)
            serializer = MusicSerializer(music, many=True)
            return Response(serializer.data)


class UploadMusicView(generics.CreateAPIView):
    '''Upload music'''
    serializer_class = UploadMusicSerializer
    permission_classes = (IsAdminUser, )


class UploadAlbumView(generics.CreateAPIView):
    '''Upload Album'''
    serializer_class = UploadAlbumSerializer
    permission_classes = (IsAdminUser, )


class CheckJWT(APIView):
    '''Check JSON web token'''
    permission_classes = (IsAdminUser, )

    def post(self, request, format=None):
        return Response({'IsAuthenticated' : 'True'})