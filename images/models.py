from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
  name = models.CharField(max_length =100)

class Category(models.Model):
  name = models.CharField(max_length =100)

class Image(models.Model):
  name = models.CharField(max_length=60)
  description = models.TextField()
  image = CloudinaryField('image')
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)