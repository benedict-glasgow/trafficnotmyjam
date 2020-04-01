from django import forms
from traffic.models import Posts, Comments, User, UserProfile
from traffic.multichoice import POST_CATEGORIES

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=300, help_text='Search the site')
    
class PostsForm(forms.ModelForm):
    title = forms.CharField(max_length=30, 
                            help_text="Please enter the title of your post :")
    photo = forms.ImageField(help_text= "Upload an Image :",required=False)
    description = forms.CharField(max_length=300, 
                            help_text="Describe your jam :")
    location = forms.CharField(max_length=50, 
                            help_text="Enter up to the first three characters of a post code :", required=False)
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    category = forms.ChoiceField(choices = POST_CATEGORIES, widget=forms.Select(),help_text= "Select a Category :", required=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Posts
        fields=('title','photo','description','location','category')
        
class CommentsForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    content = forms.CharField(max_length=300, 
                             help_text="Add a Comment :" ) 
    
    class Meta:
        model = Comments
        fields=('content',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', )


class UserProfileForm(forms.ModelForm):
    ## Placeholder if we need to add additional fields
    class Meta:
        model = UserProfile
        fields = tuple()


class ChangePasswordForm(forms.Form):
    oldPassword = forms.CharField(label='Old password', widget=forms.PasswordInput)
    newPassword = forms.CharField(label='New password', widget=forms.PasswordInput)
    repeatNewPassword = forms.CharField(label='Repeat new password',widget=forms.PasswordInput)

    class Meta:
        fields = ('oldPassword', 'newPassword', 'RepeatNewPassword',)