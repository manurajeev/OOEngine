from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import searchForm


def home_view(request):
    if request.method == 'POST':
        print(request.POST['search'])
        request.session['searchbox'] = request.POST['search']
        return HttpResponseRedirect('/search/')
    else:
        form = searchForm()
    return render(request, 'home/homepage.html', {'form': form})