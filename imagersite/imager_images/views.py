from django.shortcuts import render
from imager_images.models import Album, Photo
# from sorl.thumbnail import get_thumbnail


def library_view(request):
    """Library view controller."""
    username = request.user.get_username()
    total_albums = Album.objects.filter(user__username=username)
    total_photos = Photo.objects.filter(user__username=username)

    return render(request, 'imager_images/library.html', {'albums': total_albums, 'photos': total_photos})


def album_view(request):
    """Album view controller."""
    total_albums = Album.objects.filter(published='PUBLIC')

    return render(request, 'imager_images/album.html', {'albums': total_albums})


def photo_view(request):
    """Photo view controller."""
    total_photos = Photo.objects.filter(published='PUBLIC')

    return render(request, 'imager_images/photos.html', {'photos': total_photos})
