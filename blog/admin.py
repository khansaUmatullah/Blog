from django.contrib import admin

# Register your models here.
from .models import BlogModel, subscribe
admin.site.register(BlogModel)
admin.site.register(subscribe)