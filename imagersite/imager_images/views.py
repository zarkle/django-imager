from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from imager_images.models import Album, Photo
from imager_images.forms import AlbumForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LibraryView(LoginRequiredMixin, ListView):
    """Library view class."""

    template_name = 'imager_images/library.html'
    context_object_name = 'library'
    login_url = reverse_lazy('auth_login')

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


class AlbumView(LoginRequiredMixin, ListView):
    """Album view class."""

    template_name = 'imager_images/album.html'
    context_object_name = 'albums'
    login_url = reverse_lazy('auth_login')

    def get_queryset(self):
        """Get queryset."""
        return Album.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class PhotoView(LoginRequiredMixin, ListView):
    """Photo view class."""

    template_name = 'imager_images/photos.html'
    context_object_name = 'photos'
    login_url = reverse_lazy('auth_login')

    def get_queryset(self):
        """Get queryset."""
        return Photo.objects.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class AlbumDetailView(LoginRequiredMixin, ListView):
    """Album detail view class."""

    template_name = 'imager_images/album_detail.html'
    context_object_name = 'album'
    login_url = reverse_lazy('auth_login')

    def get_queryset(self):
        """Get queryset."""
        album = Album.objects.filter(id=self.kwargs['id']).first()
        return album.photos.filter(published='PUBLIC')

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class PhotoDetailView(LoginRequiredMixin, DetailView):
    """Photo detail view class."""

    template_name = 'imager_images/photo_detail.html'
    context_object_name = 'photo'
    login_url = reverse_lazy('auth_login')

    def get_object(self):
        """Get object."""
        return Photo.objects.filter(id=self.kwargs['id']).first()

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)
        return context


class AddPhotoView(LoginRequiredMixin, CreateView):
    """Add photo view."""

    template_name = 'imager_images/add_photo.html'
    model = Photo
    fields = ['image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddAlbumView(LoginRequiredMixin, CreateView):
    """Add album view."""

    template_name = 'imager_images/add_album.html'
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')

    def get_form_kwargs(self):
        """Get form kwargs."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.username})
        return kwargs

    def form_valid(self, form):
        """Validate form."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditAlbumView(LoginRequiredMixin, UpdateView):
    """Edit album view."""

    template_name = 'imager_images/edit_album.html'
    model = Album
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')
    slug_url_kwarg = 'id'
    slug_field = 'id'
    fields = ['photos', 'cover', 'title', 'description', 'published']

    def get(self, *args, **kwargs):
        """Get."""
        if self.request.user.get_username() != Album.objects.filter(id=kwargs['id']).first().user.username:
            return redirect('library')
        return super().get(*args, **kwargs)

    def get_form_kwargs(self):
        """Get form kwargs."""
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """Validate form."""
        return super().form_valid(form)


class EditPhotoView(LoginRequiredMixin, UpdateView):
    """Edit photo view."""

    template_name = 'imager_images/edit_photo.html'
    model = Photo
    success_url = reverse_lazy('library')
    login_url = reverse_lazy('auth_login')
    slug_url_kwarg = 'id'
    slug_field = 'id'
    fields = ['image', 'title', 'description', 'published']

    def get(self, *args, **kwargs):
        """Get."""
        if self.request.user.get_username() != Photo.objects.filter(id=kwargs['id']).first().user.username:
            return redirect('library')
        return super().get(*args, **kwargs)

    def get_form_kwargs(self):
        """Get form kwargs."""
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """Validate form."""
        return super().form_valid(form)
