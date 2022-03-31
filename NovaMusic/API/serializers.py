from rest_framework.serializers import ModelSerializer
from artist.models import Artist
from genre.models import Genre
from album.models import Album
from music.models import Music

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
    

class AlbumSerializer(ModelSerializer):
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'


class MusicSerializer(ModelSerializer):
    artists = ArtistSerializer(many=True)
    genres = GenreSerializer(many=True)
    album = AlbumSerializer(many=False)

    class Meta:
        model = Music
        fields = '__all__'


class UploadMusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = ['title', 'thumbnail', 'song', 'lyrics', 'single_track', 'album', 'artists', 'genres']


class UploadAlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'description', 'album_image', 
                'album_download_link_high', 'album_download_link_high_file',
                'album_download_link_medium', 'album_download_link_medium_file', 
                'release_time', 'artists']