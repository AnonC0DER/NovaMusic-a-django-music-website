import os
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
    return Album.objects.create(title='Sample album', published=True)

def sample_genre():
    '''Create a sample genre object'''
    return Genre.objects.create(title='Sample genre')

def sample_music():
    '''Create a sample music object'''
    return Music.objects.create(title='Sample music', published=True)


class TestApiAccesses(TestCase):
    '''Test unauthenticated recipe API access'''

    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        '''Test authentication is required to access songs and albums'''
        res = self.client.get('/api/songs/')
        res2 = self.client.get('/api/albums/')

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(res2.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_not_required(self):
        '''Test authentication is not required to access genres and artists'''
        res = self.client.get('/api/genres/')
        res2 = self.client.get('/api/artists/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res2.status_code, status.HTTP_200_OK)


class TestAlbumApi(TestCase):
    '''Tests to test albums api'''

    def setUp(self):
        '''Create a sample superuser and create an album object'''
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
    
    def test_search_albums(self):
        '''Test search albums'''
        res = self.client.get(f'/api/albums/search/Sample Album/').json()
        res2 = self.client.get(f'/api/albums/search/SAMPLE AlBUm/').json()
        
        self.assertEqual(res[0]['title'], self.album.title)
        self.assertEqual(res2[0]['title'], self.album.title)
        self.assertEqual(res[0], res2[0])
        

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
    
    def test_search_artists(self):
        '''Test search artists'''
        res = self.client.get(f'/api/artists/search/Sample artist/').json()
        res2 = self.client.get(f'/api/artists/search/SAMPLE ArTISt/').json()
        
        self.assertEqual(res[0]['title'], self.artist.title)
        self.assertEqual(res2[0]['title'], self.artist.title)
        self.assertEqual(res[0], res2[0])


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
    
    def test_search_genres(self):
        '''Test search genres'''
        res = self.client.get(f'/api/genres/search/Sample genre/').json()
        res2 = self.client.get(f'/api/genres/search/SAMPLE GeNRe/').json()
        
        self.assertEqual(res[0]['title'], self.genre.title)
        self.assertEqual(res2[0]['title'], self.genre.title)
        self.assertEqual(res[0], res2[0])


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
    
    def test_search_songs(self):
        '''Test search songs'''
        res = self.client.get(f'/api/songs/search/Sample music/').json()
        res2 = self.client.get(f'/api/songs/search/SAMPLE music/').json()
        
        self.assertEqual(res[0]['title'], self.song.title)
        self.assertEqual(res2[0]['title'], self.song.title)
        self.assertEqual(res[0], res2[0])


class TestUploadFile(TestCase):
    '''Tests to test upload files using APIs'''

    def setUp(self):
        '''Create a sample superuser'''
        self.client = APIClient()
        
        self.album = sample_album()
        self.genre = sample_genre()
        self.artist = sample_artist()
        
        self.user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='testpass123'
        )

        self.client.force_authenticate(self.user)
    
    def test_upload_song(self):
        '''Test upload a new song using REST API'''
        title = 'Sample Song using API'
        data = {
            'title' : title,
            'lyrics' : 'Sample lyrics',
            'album' : [self.album.pk],
            'genres' : [self.genre.pk],
            'artists' : [self.artist.pk]
        }

        with open('song.mp3', 'w') as f:
            song = f
        
        with open('thumbnail.jpg', 'w') as fp:
            thumbnail = fp

        files = {
            'song': song,
            'thumbnail': thumbnail,
        }

        res = self.client.post('/api/upload-music/', data=data, files=files)
        qs = Music.objects.filter(title=title)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(qs.exists())

        os.remove(song.name)
        os.remove(thumbnail.name)
    
    def test_upload_album(self):
        '''Test upload a new album using REST APIs'''
        title = 'Sample album using API'
        data = {
            'title' : title,
            'description' : 'Sample description',
            'artists' : [self.artist.pk]
        }

        with open('album_image.jpg', 'w') as fp:
            album_image = fp
        
        with open('album_file.zip', 'w') as f:
            album_file = f

        files = {
            'album_image' : album_image,
            'album_download_link_high_file' : album_file 
        }

        res = self.client.post('/api/upload-album/', data=data, files=files)
        qs = Album.objects.filter(title=title)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(qs.exists())

        os.remove(album_image.name)
        os.remove(album_file.name)