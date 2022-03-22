from django.db.models import Q 
from music.models import Music

def Search(reqeust):
    '''Search function view'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')
    
    only_published_music = Music.objects.filter(published=True)

    music = only_published_music.distinct().filter(
        Q(title__icontains=search_query)
    )

    return music