from django import forms

class searchForm(forms.Form):
    searchbox = forms.CharField(max_length=100, label='')
    searchbox.widget = forms.TextInput(attrs={'class': 'search_box', 'title': 'Search',})