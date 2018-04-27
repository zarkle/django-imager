from django.shortcuts import render, redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile


def profile_view(request, username=None):
    """Profile view controller."""
    owner = False

    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('home')

    profile = get_object_or_404(ImagerProfile, user__username=username)
    total_albums = Album.objects.filter(user__username=username)
    total_photos = Photo.objects.filter(user__username=username)
    albums_private = total_albums.filter(published='PRIVATE').count()
    albums_public = total_albums.filter(published='PUBLIC').count()
    photos_private = total_photos.filter(published='PRIVATE').count()
    photos_public = total_photos.filter(published='PUBLIC').count()

    if not owner:
        total_photos = Photo.objects.filter(published='PUBLIC', user__username=username)
        total_albums = Album.objects.filter(published='PUBLIC', user__username=username)
        albums_private = albums_public = photos_private = photos_public = 0

    context = {
        'profile': profile,
        'albums': total_albums,
        'photos': total_photos,
        'albums_private': albums_private,
        'albums_public': albums_public,
        'photos_private': photos_private,
        'photos_public': photos_public,


    }

    return render(request, 'imager_profile/profile.html', context)
