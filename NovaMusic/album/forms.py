from core.forms import CommentForm
from album.models import AlbumComment

class AlbumCommentForm(CommentForm):
    class Meta:
        model = AlbumComment
        fields = ['body']

        labels = {
            'body' : 'Add a comment'
        }