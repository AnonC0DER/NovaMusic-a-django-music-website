from django.test import TestCase
from genre.models import Genre
from django.utils.text import slugify

class TestGenreModel(TestCase):
    '''Test artist model'''

    def setUp(self):
        self.genre = Genre.objects.create(title='Test genre')

    def test_artist_object_exists(self):
        '''Test genre object created and exists in the database'''
        self.assertTrue(Genre.objects.filter(title=self.genre.title).exists())

    def test_slug_field(self):
        '''Test slug field and slug signal'''
        title = self.genre.title
        title_slug = slugify(title)

        self.assertEqual(title_slug, self.genre.slug)

    def test_valid_title(self):
        '''Testing valid title'''
        qs = Genre.objects.filter(title=self.genre.title)

        self.assertTrue(qs.exists())

    def test_created_object_count(self):
        '''Test there's only one object that is created in database'''
        qs = Genre.objects.all().count()

        self.assertEqual(qs, 1)

    def test_created_datetime(self):
        '''Test created datetime is auto now added'''
        obj_datetime = self.genre.created

        self.assertTrue(obj_datetime is not None)

    def test_object_id(self):
        '''Test object ID'''
        obj_id = self.genre.id
        qs = Genre.objects.filter(id=obj_id)

        self.assertTrue(qs.exists())