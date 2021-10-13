from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

from .helpers import *
class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=models.TextField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)


