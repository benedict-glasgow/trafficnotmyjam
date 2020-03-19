from django import forms
from traffic.models import Posts
from traffic.multichoice import POST_CATEGORIES

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=300, help_text='Search the site')
    
class PostsForm(forms.ModelForm):
    title = forms.CharField(max_length=30, 
                            help_text="Please enter the title of your post :")
    photo = forms.ImageField(help_text= "Upload an Image :",required=False)
    description = forms.CharField(max_length=300, 
                            help_text="Describe your jam :")
    location = forms.CharField(max_length=3, 
                            help_text="Enter up to the first three characters of a post code :")
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    category = forms.ChoiceField(choices = POST_CATEGORIES, widget=forms.Select(),help_text= "Select a Category :", required=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categorySlug =forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Posts
        fields=('title','photo','description','location','category')
