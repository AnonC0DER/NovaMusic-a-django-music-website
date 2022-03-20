from core.forms import CommentForm
from music.models import MusicComment

class MusicCommentForm(CommentForm):
    class Meta:
        model = MusicComment
        fields = ['body']

        labels = {
            'body' : 'Add a comment'
        }