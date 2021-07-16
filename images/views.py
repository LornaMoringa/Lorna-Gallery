from django.shortcuts import render,get_object_or_404,redirect
from .models import Photo,Location,Category
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt

# Create your views here.
def index(request):
  images =Photo.objects.all()
  location = Location.objects.all()
  return render(request,'index.html',{'images':images, 'location':location})
