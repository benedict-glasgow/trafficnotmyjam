from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='post_images', blank=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    dateandtime = models.DateTimeField(auto_now_add=True, blank=True)
    Category = models.CharField(max_length=30)
    #CharField(max_length=300)
    
    def __str__(self):
        return self.title
