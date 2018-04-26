from django.shortcuts import render
from imager_images.models import Photo
import random


# Create your views here.
def home_view(request):
    all_photos = Photo.objects.all()
    # if not all_photos
    one_photo = random.choice(all_photos)
    image_url = one_photo.image.url
    return render(request, 'generic/home.html', {'image': image_url})
