from django.shortcuts import render
from OOEngine import search

# Create your views here.

def search_view(request):
    search_input = request.session.get('searchbox')
    data = search.search(search_input)
    print(data)
    return render(request, 'search/search.html', context={'search_input':search_input, 'data':data})

