from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    blogs = BlogModel.objects.all()
    context = {'blogs': blogs}
    return render(request, 'home.html', context)