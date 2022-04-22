from django.shortcuts import render
from OOEngine import search
from django.core.paginator import Paginator


def search_view(request):
    search_input = request.session.get('searchbox')
    data = search.search(search_input)
    print(data)

    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(data, '5') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    return render(request, 'search/search.html', context={'search_input':search_input, 'data':page_obj})


