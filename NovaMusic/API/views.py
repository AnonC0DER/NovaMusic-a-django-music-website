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
                'Single album' : '/api/album/ID/',
                'Songs' : '/api/songs/',
                'Single song' : '/api/song/ID/',
                'Artists' : '/api/artists/',
                'Single artist' : '/api/artist/ID/',
                'Genres' : '/api/genres/',
                'Single genre' : '/api/genre/ID/',
            },

            'POST' : {
                'Upload album' : '/api/upload-album/',
                'Upload music' : '/api/upload-music/',
            }
        }

        return Response(Urls)


class AlbumView(APIView):
    '''To get single album details, use this url : /album/ID/'''
    permission_classes = (IsAdminUser, )
    
    def get(self, request, pk=None, format=None):
        if pk:
            album = Album.objects.get(id=pk)
            serializer = AlbumSerializer(album, many=False)
            return Response(serializer.data)

        else:
            albums = Album.objects.all()
            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)

          
class GenreView(APIView):
    '''To get single genre details, use this url : /genre/ID/'''
    def get(self, request, pk=None, format=None):
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
    def get(self, request, pk=None, format=None):
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
    
    def get(self, request, pk=None, format=None):
        if pk:
            music = Music.objects.get(id=pk)
            serializer = MusicSerializer(music, many=False)
            return Response(serializer.data)

        else:
            music = Music.objects.all()
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