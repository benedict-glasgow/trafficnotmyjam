from django.db import models
from traffic.multichoice import POST_CATEGORIES
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=30, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images', blank=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True, blank=True) 
    category = models.CharField(choices = POST_CATEGORIES, max_length=25, default = 'general-jams')
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title) + str( Posts.objects.filter(slug__regex=r'{}'.format(slugify(self.title)) ).count() )
        super(Posts, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,related_name = 'comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=300)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.content
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ## A Placeholder model in case we want to add more fields for users
    ## The username and password fields are handled by the built in User model
    def __str__(self):
        return self.user.username
    
class Reactions(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='reaction_images', blank=True)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
