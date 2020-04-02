from django.db import models
from traffic.multichoice import POST_CATEGORIES
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=30, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='postImages/', blank=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50, unique=False)
    date = models.DateTimeField(auto_now_add=True, blank=True) 
    category = models.CharField(choices = POST_CATEGORIES, max_length=25, default = 'general-jams')
    greenCount =  models.IntegerField(default = 0, blank=True)
    yellowCount =  models.IntegerField(default = 0, blank=True)
    redCount =  models.IntegerField(default = 0, blank=True)
    stopCount =  models.IntegerField(default = 0, blank=True)
    slug = models.SlugField()
    
    
    def save(self, *args, **kwargs):
        
        if self.greenCount < 0:
            self.greenCount = 0
            
        if self.yellowCount <0:
            self.yellowCount =0
            
        if self.redCount < 0:
            self.redCount = 0
            
        if self.stopCount < 0:
            self.stopCount = 0

        if self.slug == '':
            ## If there is no slug, create the slug using the Posts title and the Posts id
            ## To use the id, the Posts must have been saved to the db first

            if self.id == None:
                super(Posts, self).save(*args, **kwargs)
                self.save()
            else:
                self.slug = slugify(self.title) + str(self.id)
                super(Posts, self).save(*args, **kwargs)

        else:
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
    

    
