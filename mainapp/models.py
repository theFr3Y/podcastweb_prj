from django.db import models

class PodcasterModel(models.Model):
    name = models.CharField(max_length=200)
    publish = models.BooleanField(default=True)
    pic = models.ImageField(upload_to='media/PodcasterProfile')
    slug = models.SlugField(max_length=200, unique=True)
    position = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class PodcastModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    url = models.URLField(max_length=500)
    pic = models.ImageField(upload_to='media/PodcastCover')
    publish = models.BooleanField(default=True)
    category = models.ManyToManyField(PodcasterModel, related_name='pods')
    
    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['-date']
        
        
class ContactModel(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sendtime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['-sendtime']