from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from imager_images.models import Album, Photo
# from sorl.thumbnail import get_thumbnail


class LibraryView(ListView):
    """Library view class."""

    template_name = 'imager_images/library.html'

    context_object_name = 'library'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        username = self.request.user.get_username()
        total_albums = Album.objects.filter(user__username=username)
        total_photos = Photo.objects.filter(user__username=username)

        return [total_albums, total_photos]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = context['library'][0]
        context['photos'] = context['library'][1]
        del context['library']

        return context


def album_view(request):
    """Album view controller."""
    total_albums = Album.objects.filter(published='PUBLIC')

    return render(request, 'imager_images/album.html', {'albums': total_albums})


def photo_view(request):
    """Photo view controller."""
    total_photos = Photo.objects.filter(published='PUBLIC')

    return render(request, 'imager_images/photos.html', {'photos': total_photos})


def album_detail_view(request, id):
    """Album detail view controller."""
    album = Album.objects.filter(id=id).first()
    album = album.photos.filter(published='PUBLIC')
    return render(request, 'imager_images/album_detail.html', {'album': album})


def photo_detail_view(request, id):
    """Photo detail view controller."""
    photo = Photo.objects.filter(id=id).first()
    return render(request, 'imager_images/photo_detail.html', {'photo': photo})
