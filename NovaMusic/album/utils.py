from django.db.models import Q 
from album.models import Album

def Search(reqeust):
    '''Search function view'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')
    
    only_published_albums =  Album.objects.filter(published=True)

    album = only_published_albums.distinct().filter(
        Q(title__icontains=search_query)
    )

    return album