from django.views.generic import ListView, DetailView
from imager_images.models import Album, Photo


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


class AlbumView(ListView):
    """Album view class."""

    template_name = 'imager_images/album.html'

    context_object_name = 'albums'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Album.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhotoView(ListView):
    """Photo view class."""

    template_name = 'imager_images/photos.html'

    context_object_name = 'photos'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        return Photo.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AlbumDetailView(ListView):
    """Album detail view class."""

    template_name = 'imager_images/album_detail.html'

    context_object_name = 'album'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        album = Album.objects.filter(id=self.kwargs['id']).first()
        return album.photos.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhotoDetailView(DetailView):
    """Photo detail view class."""

    template_name = 'imager_images/photo_detail.html'

    context_object_name = 'photo'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_object(self):
        return Photo.objects.filter(id=self.kwargs['id']).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
