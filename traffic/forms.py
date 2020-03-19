from django import forms
from traffic.models import Posts

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=300, help_text='Search the site')
    
class PostsForm(forms.ModelForm):
    title = forms.CharField(max_length=30, 
                            help_text="Please enter the title of your post.")
    photo = forms.ImageField(required=False)
    description = forms.CharField(max_length=300, 
                            help_text="Describe your jam.")
    location = forms.CharField(max_length=3, 
                            help_text="Enter the first three characters of a post code")
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    category = forms.CharField(max_length=300,help_text="Enter a category.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categorySlug =forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Posts
        fields=('title','photo','description','location','category')
