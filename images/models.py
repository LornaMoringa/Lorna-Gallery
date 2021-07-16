from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length =100)

class Category(models.Model):
  name = models.CharField(max_length =100)