from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs}
    return render(request, 'home.html', context)
def blog_detail(request , slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)


def index(request):
    if request.method=='POST':
        
        
        subscribe.email=request.POST["email"]
        
        Contact=subscribe.objects.create(email=subscribe)
        
    return render(request,'home.html')