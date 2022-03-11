from django.test import TestCase
from music.models import Music
from artist.models import Artist
from album.models import Album
from genre.models import Genre
from django.utils.text import slugify

class TestMusicModel(TestCase):

    def setUp(self):
        self.artist = Artist.objects.create(title='Test artist')
        self.genre = Genre.objects.create(title='Test genre')
        self.album = Album.objects.create(title='Test album')
        self.music = Music.objects.create(title='Test music', album=self.album)

        self.music.genres.set([self.genre])
        self.music.artists.set([self.artist])
        self.music.save()

    def test_music_album_object(self):
        '''Test music and album model relation'''
        self.assertEqual(self.album, self.music.album)
    
    def test_music_artist_object(self):
        '''Test music and artist model relation'''
        artists = Artist.objects.all()
        music_artist = self.music.artists.first()

        self.assertIn(music_artist, artists)
    
    def test_music_genre_object(self):
        '''Test music and genre model relation'''
        music_genre = self.music.genres.first()
        qs = Genre.objects.filter(title=music_genre.title)

        self.assertTrue(qs.exists())

    def test_get_album_name(self):
        '''Test get_album_name() method in Music model'''
        qs = self.music.get_album_name()
        
        self.assertEqual(qs, self.album.title)

    def test_music_object_exists(self):
        '''Test music object created and exists in the database'''
        self.assertTrue(Music.objects.filter(title=self.music.title).exists())

    def test_slug_field(self):
        '''Test slug field and slug signal'''
        title = self.music.title
        title_slug = slugify(title)

        self.assertEqual(title_slug, self.music.slug)

    def test_valid_title(self):
        '''Testing valid title'''
        title = 'Test music'
        qs = Music.objects.filter(title=title)

        self.assertTrue(qs.exists())

    def test_created_object_count(self):
        '''Test there's only one object that is created in database'''
        qs = Music.objects.all().count()

        self.assertEqual(qs, 1)

    def test_published_is_false(self):
        '''Test default object isn't published'''
        self.assertEqual(self.music.published, False)

    def test_created_datetime(self):
        '''Test created datetime is auto now added'''
        obj_datetime = self.music.created

        self.assertTrue(obj_datetime is not None)

    def test_object_id(self):
        '''Test object ID'''
        obj_id = self.music.id
        qs = Music.objects.filter(id=obj_id)

        self.assertTrue(qs.exists())