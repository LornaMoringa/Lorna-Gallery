from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',views.index,name='home'),
  path('school/',views.school_images,name='school'),
  path('nairobi/',views.nairobi_images,name='nairobi'),
  path('coast/',views.coast_images,name='coast'),
  path('kericho/',views.kericho_images,name='kericho'),
  path('image_details/<int:image_id>',views.image_details,name='image.detail'),
  path('search_category/',views.search_images, name='search_images')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)