from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=300, help_text='Search the site')

