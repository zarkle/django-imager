from django.shortcuts import render
from imager_images.models import Photo
import random


# Create your views here.
def home_view(request):
    all_photos = Photo.objects.filter(published='PUBLIC')
    try:
        one_photo = random.choice(all_photos)
        image_url = one_photo.image.url
    except IndexError:
        image_url = 'static/windows.jpg'
    return render(request, 'generic/home.html', {'image': image_url})
