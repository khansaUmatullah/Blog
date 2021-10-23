from django.contrib import admin

# Register your models here.
from .models import BlogModel, Form, subscribe
admin.site.register(BlogModel)
admin.site.register(subscribe)
admin.site.register(Form)