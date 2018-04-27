from django.shortcuts import render
from imager_images.models import Album, Photo
# from sorl.thumbnail import get_thumbnail


def library_view(request):
    username = request.user.get_username()
    total_albums = Album.objects.filter(user__username=username)
    total_photos = Photo.objects.filter(user__username=username)

    return render(request, 'imager_images/library.html', {'albums': total_albums, 'photos': total_photos})
