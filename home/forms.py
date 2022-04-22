from django import forms


class searchForm(forms.Form):
    searchbox = forms.CharField(max_length=100, label='search_box')
    searchbox.widget = forms.TextInput(attrs={'id':'tags', 'class': 'search_box', 'title': 'Search',})