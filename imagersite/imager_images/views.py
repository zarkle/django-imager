from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from imager_images.models import Album, Photo
from imager_images.forms import AlbumForm
from django.urls import reverse_lazy


class LibraryView(ListView):
    """Library view class."""

    template_name = 'imager_images/library.html'

    context_object_name = 'library'

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get queryset."""
        username = self.request.user.get_username()
        total_albums = Album.objects.filter(user__username=username)
        total_photos = Photo.objects.filter(user__username=username)

        return [total_albums, total_photos]

    def get_context_data(self, **kwargs):
        """Get context data."""
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
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get queryset."""
        return Album.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class PhotoView(ListView):
    """Photo view class."""

    template_name = 'imager_images/photos.html'

    context_object_name = 'photos'

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get queryset."""
        return Photo.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class AlbumDetailView(ListView):
    """Album detail view class."""

    template_name = 'imager_images/album_detail.html'

    context_object_name = 'album'

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get queryset."""
        album = Album.objects.filter(id=self.kwargs['id']).first()
        return album.photos.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class PhotoDetailView(DetailView):
    """Photo detail view class."""

    template_name = 'imager_images/photo_detail.html'

    context_object_name = 'photo'

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_object(self):
        """Get object."""
        return Photo.objects.filter(id=self.kwargs['id']).first()

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class AddPhotoView(CreateView):
    """Add photo view."""

    template_name = 'imager_images/add_photo.html'
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Post."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().post(*args, **kwargs)

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAlbumView(CreateView):
    """Add album view."""

    template_name = 'imager_images/add_album.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Post."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        """Get form kwargs."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)
