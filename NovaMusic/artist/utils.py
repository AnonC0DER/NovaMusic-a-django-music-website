from django.db.models import Q 
from artist.models import Artist

def Search(reqeust):
    '''Search function view'''
    search_query = ''

    if reqeust.GET.get('query'):
        search_query = reqeust.GET.get('query')
    
    artist = Artist.objects.distinct().filter(
        Q(title__icontains=search_query)
    )

    return artist