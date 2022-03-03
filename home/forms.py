from django import forms

class searchForm(forms.Form):
    searchbox = forms.CharField(max_length=100)