from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from froala_editor.fields import FroalaField
from .helpers import *
class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content = FroalaField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)


class subscribe(models.Model):
    
    email=models.EmailField()
class Form(models.Model):
    first=models.TextField()
    second=models.TextField()
    third=models.TextField()
    fourth=models.TextField()
    fifth=models.TextField()
    sixth=models.TextField()
    seven=models.TextField()
    eight=models.TextField()
    ninth=models.TextField()
    tenth=models.TextField()
    eleven=models.TextField()