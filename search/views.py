from django.shortcuts import render

# Create your views here.
data = {'movies':['A Beautiful Mind', 'The Martian', 'Wonder', 'Interstellar', 'Passengers']}


def search_view(request):
    return render(request, 'search/search.html', context=data)

