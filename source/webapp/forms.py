from django import forms
from django.forms import widgets


class BookForm(forms.Form):
    name_author = forms.CharField(max_length=200, required=False, label='Name')
    mail_author = forms.CharField(max_length=200, required=False, label='Mail')
    entry = forms.CharField(max_length=3000, required=False, label='Entry', widget=widgets.Textarea)