from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    name_author = forms.CharField(max_length=200, required=True, label='Name')
    mail_author = forms.EmailField(max_length=200, required=True, label='Mail')
    entry = forms.CharField(max_length=3000, required=True, label='Entry', widget=widgets.Textarea)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=True, label='search')