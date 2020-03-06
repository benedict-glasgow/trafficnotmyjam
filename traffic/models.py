from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to='post_images', blank=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    dateandtime = models.DateTimeField(auto_now_add=True, blank=True)
    Category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    
    #CharField(max_length=300)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
