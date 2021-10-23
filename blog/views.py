from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.method=='POST':
        
        
        subscribe.email=request.POST["my_email"]
        subscribe.objects.create(email=subscribe.email)
        


















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


def form(request):
    if request.method=='POST':
        
        Form.first=request.POST["1st"]
        Form.second=request.POST["2nd"]
        Form.third=request.POST["3rd"]
        Form.fourth=request.POST["4th"]
        Form.fifth=request.POST["5th"]
        Form.sixth=request.POST["6th"]
        Form.seven=request.POST["7th"]
        Form.eight=request.POST["8th"]
        Form.ninth=request.POST["9th"]
        Form.tenth=request.POST["10th"]
        Form.eleven=request.POST["11th"]

        Form.objects.create(first=Form.first,second=Form.second,third=Form.third,fourth=Form.fourth,fifth=Form.fifth,sixth=Form.sixth,seven=Form.seven,eight=Form.eight,ninth=Form.ninth,tenth=Form.tenth,eleven=Form.eleven)
       
        
        return render(request, 'submit.html')

    return render(request, 'form.html')