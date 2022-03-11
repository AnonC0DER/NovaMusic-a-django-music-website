from django.test import TestCase
from artist.models import Artist
from django.utils.text import slugify

class TestArtistModel(TestCase):
    '''Test artist model'''

    def setUp(self):
        self.artist = Artist.objects.create(title='Test artist')

    def test_artist_object_exists(self):
        '''Test artist object created and exists in the database'''
        self.assertTrue(Artist.objects.filter(title=self.artist.title).exists())

    def test_slug_field(self):
        '''Test slug field and slug signal'''
        title = self.artist.title
        title_slug = slugify(title)

        self.assertEqual(title_slug, self.artist.slug)

    def test_valid_title(self):
        '''Testing valid title'''
        qs = Artist.objects.filter(title=self.artist.title)

        self.assertTrue(qs.exists())

    def test_created_object_count(self):
        '''Test there's only one object that is created in database'''
        qs = Artist.objects.all().count()

        self.assertEqual(qs, 1)

    def test_created_datetime(self):
        '''Test created datetime is auto now added'''
        obj_datetime = self.artist.created

        self.assertTrue(obj_datetime is not None)

    def test_object_id(self):
        '''Test object ID'''
        obj_id = self.artist.id
        qs = Artist.objects.filter(id=obj_id)

        self.assertTrue(qs.exists())