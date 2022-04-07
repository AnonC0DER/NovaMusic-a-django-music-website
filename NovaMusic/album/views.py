from django.shortcuts import render, redirect
from django.contrib import messages
from album.models import Album, AlbumComment
from genre.models import Genre
from music.models import Music
from album.utils import Search
from album.forms import AlbumCommentForm 
from core.tasks import send_email_task

def AlbumsPage(request):
    '''Releases albums view page'''
    get_published_albums = Search(request)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    get_genres = Genre.objects.all()
    context = {'albums' : get_published_albums, 'genres' : get_genres, 'player' : new_song_for_player}
    
    return render(request, 'album/albums.html', context)


def SingleAlbumPage(request, pk, slug):
    '''Signle album page view'''
    get_album = Album.objects.get(id=pk, slug=slug)
    form = AlbumCommentForm()

    if request.method == 'POST':
        form = AlbumCommentForm(request.POST)
        if form.is_valid():
            
            # comment.save()

            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            
            if reply_id:
                reply_obj = AlbumComment.objects.get(id=reply_id)

            if reply_obj:
                comment = form.save(commit=False)
                comment.album = get_album
                comment.owner = request.user
                comment.reply = reply_obj
                comment.save()
            
            else:
                comment = form.save(commit=False)
                comment.album = get_album
                comment.owner = request.user
                comment.save()

            messages.success(request, 'Successfully Submitted. Your comment will be available after review.')
            # Send email to user using celery
            send_email_task.delay(comment.owner.email)
            return redirect('single-album', slug=get_album.slug, pk=get_album.id)

    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    get_album_songs = Music.objects.filter(album=get_album, published=True)
    artist_albums = Album.objects.filter(artists=get_album.artists.first(), published=True)[:6]
    songs_count = get_album_songs.count()
    album_comments_count = get_album.albumcomment_set.filter(active=True).count()
    
    context = {
        'album' : get_album, 
        'songs' : get_album_songs, 
        'count' : songs_count,
        'artist_albums' : artist_albums,
        'player' : new_song_for_player, 
        'form' : form,
        'comments_count' : album_comments_count 
    }
    
    return render(request, 'album/single-album.html', context)