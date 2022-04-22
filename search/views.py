from django.shortcuts import render
from OOEngine import search_temp


def search_view(request):
    search_input = request.session.get('searchbox')
    data = search_temp.search(search_input)
    return render(request, 'search/search.html', context={'search_input':search_input, 'data':data})
