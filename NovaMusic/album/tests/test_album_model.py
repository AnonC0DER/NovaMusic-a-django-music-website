from django.test import TestCase
from album.models import Album
from django.utils.text import slugify

class TestAlbumModel(TestCase):

    def setUp(self):
        self.album = Album.objects.create(title='Test album')

    def test_album_object_exists(self):
        '''Test album object created and exists in the database'''
        self.assertTrue(Album.objects.filter(title=self.album.title).exists())

    def test_slug_field(self):
        '''Test slug field and slug signal'''
        title = self.album.title
        title_slug = slugify(title)

        self.assertEqual(title_slug, self.album.slug)

    def test_valid_title(self):
        '''Testing valid title'''
        title = 'Test album'
        qs = Album.objects.filter(title=title)

        self.assertTrue(qs.exists())

    def test_created_object_count(self):
        '''Test there's only one object that is created in database'''
        qs = Album.objects.all().count()

        self.assertEqual(qs, 1)

    def test_published_is_false(self):
        '''Test default object isn't published'''
        self.assertEqual(self.album.published, False)

    def test_created_datetime(self):
        '''Test created datetime is auto now added'''
        obj_datetime = self.album.created

        self.assertTrue(obj_datetime is not None)

    def test_object_id(self):
        '''Test object ID'''
        obj_id = self.album.id
        qs = Album.objects.filter(id=obj_id)

        self.assertTrue(qs.exists())