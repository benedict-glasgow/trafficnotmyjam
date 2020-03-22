from django.db import models
from traffic.multichoice import POST_CATEGORIES
from django.template.defaultfilters import slugify

class Posts(models.Model):
    title = models.CharField(max_length=30, unique=False)
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
    date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=300)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.content
    
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username
    
class Reactions(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    Image = models.ImageField(upload_to='reaction_images', blank=True)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
