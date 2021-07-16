from django.shortcuts import render,get_object_or_404,redirect
from .models import Image,Location,Category
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt

# Create your views here.
def index(request):
  images =Image.objects.all()
  location = Location.objects.all()
  return render(request,'index.html',{'images':images, 'location':location})

def search_images(request):
  if 'image' in request.GET and request.GET["image"]:
    search_term = request.GET.get("image")
    searched_images = Image.find_category(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message,"images":searched_images})

  else:
    message = 'You have not searched for any term'
    return render(request, 'search.html', {"message":message})