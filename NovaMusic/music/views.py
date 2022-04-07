from django.shortcuts import render, redirect
from django.contrib import messages
from music.models import Music, MusicComment
from album.models import Album
from music.forms import MusicCommentForm
from music.utils import Search
from core.tasks import send_email_task 

def SongsPage(request):
    '''Songs page view'''
    songs = Search(request)
    new_song_for_player = Music.objects.filter(published=True).order_by('-created').first()
    context = {'songs' : songs, 'player' : new_song_for_player}

    return render(request, 'music/songs.html', context)


def SingleSongPage(request, slug, pk):
    '''Single song page view'''
    song = Music.objects.get(slug=slug, pk=pk)
    form = MusicCommentForm()

    if request.method == 'POST':
        form = MusicCommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            
            if reply_id:
                reply_obj = MusicComment.objects.get(id=reply_id)

            if reply_obj:
                comment = form.save(commit=False)
                comment.music = song
                comment.owner = request.user
                comment.reply = reply_obj
                comment.save()
            
            else:
                comment = form.save(commit=False)
                comment.music = song
                comment.owner = request.user
                comment.save()

            messages.success(request, 'Successfully Submitted. Your comment will be available after review.')
            # Send email to user using celery
            send_email_task.delay(comment.owner.email)
            return redirect('single-song', slug=song.slug, pk=song.id)

    # Songs from this artist
    artist_albums = Album.objects.filter(artists=song.artists.first())[:6]
    music_comments_count = song.musiccomment_set.filter(active=True).count()
    context = {
        'song' : song, 
        'player' : song,
        'artist_albums' : artist_albums,
        'form' : form,
        'comments_count' : music_comments_count
    }

    return render(request, 'music/single-song.html', context)