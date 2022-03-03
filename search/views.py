from django.shortcuts import render

# Create your views here.
data = ['A Beautiful Mind', 'The Martian', 'Wonder', 'Interstellar', 'Passengers']


def search_view(request):
    search_input = request.session.get('searchbox')
    return render(request, 'search/search.html', context={'search_input':search_input, 'data':data})

