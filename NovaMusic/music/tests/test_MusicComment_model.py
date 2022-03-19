from django.test import TestCase
from django.contrib.auth import get_user_model
from music.models import Music, MusicComment

User = get_user_model()

class TestMusicCommentModel(TestCase):
    '''Tests to test MusicComment model'''
    def create_comment(self):
        '''Create and return comment object'''
        return MusicComment.objects.create(
            owner=self.user_obj,
            music=self.music_obj,
            body='Test comment',
        )

    def setUp(self):
        self.user_obj = User.objects.create(email='test@gmail.com', password='testpass123')
        self.user_obj_2 = User.objects.create(email='test2@gmail.com', password='testpass123')
        self.music_obj = Music.objects.create(title='Test music obj')

    def test_comment_on_music_obj(self):
        '''Test comment on a music object'''
        comment_obj = self.create_comment()
        filter_comment_obj = MusicComment.objects.filter(active=True)

        self.assertFalse(comment_obj.active)
        self.assertIsNone(comment_obj.reply)
        self.assertIsNotNone(comment_obj.body)
        self.assertIsNotNone(comment_obj.created)
        self.assertEqual(comment_obj.owner, User.objects.get(email='test@gmail.com'))
        self.assertIn(comment_obj.music, Music.objects.all())
        self.assertEqual(filter_comment_obj.count(), 0)

    def test_reply_comment(self):
        '''Test reply on a comment'''
        comment_obj = self.create_comment()
        reply_obj = MusicComment.objects.create(
            owner=self.user_obj_2,
            music=self.music_obj,
            body='Test reply',
            reply=comment_obj
        )

        self.assertEqual(comment_obj.replies.all().count(), 1)
        self.assertEqual(self.music_obj.musiccomment_set.all().count(), 2)
        self.assertIn(reply_obj, self.music_obj.musiccomment_set.all())
        self.assertEqual(reply_obj.owner, self.user_obj_2)
        self.assertEqual(reply_obj.body, comment_obj.replies.first().body)

    def test_reply_on_invalid_comment(self):
        '''Test reply on an invalid comment'''
        with self.assertRaises(ValueError):
            MusicComment.objects.create(
                owner=self.user_obj_2,
                music=self.music_obj,
                body='Test reply',
                reply=123
            )