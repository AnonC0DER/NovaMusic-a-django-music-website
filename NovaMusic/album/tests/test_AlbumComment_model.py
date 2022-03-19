from django.test import TestCase
from django.contrib.auth import get_user_model
from album.models import Album, AlbumComment

User = get_user_model()

class TestAlbumCommentModel(TestCase):
    '''Tests to test AlbumComment model'''
    def create_comment(self):
        '''Create and return comment object'''
        return AlbumComment.objects.create(
            owner=self.user_obj,
            album=self.album_obj,
            body='Test comment',
        )

    def setUp(self):
        self.user_obj = User.objects.create(email='test@gmail.com', password='testpass123')
        self.user_obj_2 = User.objects.create(email='test2@gmail.com', password='testpass123')
        self.album_obj = Album.objects.create(title='Test album obj')

    def test_comment_on_album_obj(self):
        '''Test comment on a album object'''
        comment_obj = self.create_comment()
        filter_comment_obj = AlbumComment.objects.filter(active=True)

        self.assertFalse(comment_obj.active)
        self.assertIsNone(comment_obj.reply)
        self.assertIsNotNone(comment_obj.body)
        self.assertIsNotNone(comment_obj.created)
        self.assertEqual(comment_obj.owner, User.objects.get(email='test@gmail.com'))
        self.assertIn(comment_obj.album, Album.objects.all())
        self.assertEqual(filter_comment_obj.count(), 0)

    def test_reply_comment(self):
        '''Test reply on a comment'''
        comment_obj = self.create_comment()
        reply_obj = AlbumComment.objects.create(
            owner=self.user_obj_2,
            album=self.album_obj,
            body='Test reply',
            reply=comment_obj
        )

        self.assertEqual(comment_obj.replies.all().count(), 1)
        self.assertEqual(self.album_obj.albumcomment_set.all().count(), 2)
        self.assertIn(reply_obj, self.album_obj.albumcomment_set.all())
        self.assertEqual(reply_obj.owner, self.user_obj_2)
        self.assertEqual(reply_obj.body, comment_obj.replies.first().body)

    def test_reply_on_invalid_comment(self):
        '''Test reply on an invalid comment'''
        with self.assertRaises(ValueError):
            AlbumComment.objects.create(
                owner=self.user_obj_2,
                Album=self.album_obj,
                body='Test reply',
                reply=123
            )