from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from django.test import TestCase
from album.models import Album
from genre.models import Genre
from artist.models import Artist
from music.models import Music

def sample_artist():
    '''Create a sample artist object'''
    return Artist.objects.create(title='Sample artist')

def sample_album():
    '''Create a sample album object'''
    return Album.objects.create(title='Sample album')

def sample_genre():
    '''Create a sample genre object'''
    return Genre.objects.create(title='Sample genre')

def sample_music():
    '''Create a sample music object'''
    return Music.objects.create(title='Sample music')


class TestApiAccesses(TestCase):
    '''Test unauthenticated recipe API access'''

    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        '''Test authentication is required to access songs and albums'''
        res = self.client.get('/api/songs/')
        res2 = self.client.get('/api/albums/')

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res2.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_not_required(self):
        '''Test authentication is not required to access genres and artists'''
        res = self.client.get('/api/genres/')
        res2 = self.client.get('/api/artists/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res2.status_code, status.HTTP_200_OK)


class TestAlbumApi(TestCase):
    '''Tests to test albums api'''

    def setUp(self):
        self.album = sample_album()
        
        self.client = APIClient()
        # Only admin users can use album api
        self.user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='testpass123'
        )

        self.client.force_authenticate(self.user)

    def test_albums_count(self):
        '''Test albums count'''
        res = self.client.get('/api/albums/').json()
        
        self.assertEqual(len(res), 1)
    
    def test_single_album_page(self):
        '''Test single album page'''
        res = self.client.get(f'/api/album/{self.album.pk}/').json()
        
        self.assertEqual(res['title'], self.album.title)


class TestArtistApi(TestCase):
    '''Tests to test artists api'''

    def setUp(self):
        self.artist = sample_artist()
        self.client = APIClient()

    def test_artists_count(self):
        '''Test artists count'''
        res = self.client.get('/api/artists/').json()
        
        self.assertEqual(len(res), 1)
    
    def test_single_artist_page(self):
        '''Test single artist page'''
        res = self.client.get(f'/api/artist/{self.artist.pk}/').json()
        
        self.assertEqual(res['title'], self.artist.title)


class TestGenreApi(TestCase):
    '''Tests to test genres api'''

    def setUp(self):
        self.genre = sample_genre()
        self.client = APIClient()

    def test_genres_count(self):
        '''Test genres count'''
        res = self.client.get('/api/genres/').json()
        
        self.assertEqual(len(res), 1)
    
    def test_single_genre_page(self):
        '''Test single genre page'''
        res = self.client.get(f'/api/genre/{self.genre.pk}/').json()
        
        self.assertEqual(res['title'], self.genre.title)


class TestSongApi(TestCase):
    '''Tests to test music api'''

    def setUp(self):
        self.song = sample_music()
        
        self.client = APIClient()
        # Only admin users can use album api
        self.user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='testpass123'
        )

        self.client.force_authenticate(self.user)

    def test_songs_count(self):
        '''Test songs count'''
        res = self.client.get('/api/songs/').json()
        
        self.assertEqual(len(res), 1)
    
    def test_single_song_page(self):
        '''Test single song page'''
        res = self.client.get(f'/api/song/{self.song.pk}/').json()
        
        self.assertEqual(res['title'], self.song.title)