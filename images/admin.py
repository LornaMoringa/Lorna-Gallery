from django.contrib import admin
from .models import Category, Location, Image

# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)