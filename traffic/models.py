from django.db import models
from traffic.multichoice import POST_CATEGORIES
from django.template.defaultfilters import slugify

class Posts(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='post_images', blank=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add=True, blank=True) ## Changed to date to stay consitent 
    category = models.IntegerField(choices = POST_CATEGORIES, default = 6) ## fixed lowercase
    slug = models.SlugField()#unique=True
    categorySlug = models.SlugField(unique=False, default = '')
    
    #CharField(max_length=300)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.categorySlug = slugify(self.category)
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
    
