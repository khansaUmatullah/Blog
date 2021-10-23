
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
   
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('form/',form,name="form"),
]








