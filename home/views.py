from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import searchForm
# Create your views here.
def home_view(request):
    if request.method == 'POST':
       form = searchForm(request.POST)
       if form.is_valid():
            # Store the search keyword in sessions to retrive it in the search view
            input_text = form.cleaned_data['searchbox']
            request.session['searchbox'] = input_text
            # redirect to a new URL:
            #print(request.POST)
            return HttpResponseRedirect('/search/') 
    else:
        form = searchForm()
    return render(request, 'home/homepage.html', {'form': form})