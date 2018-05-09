from django.shortcuts import redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile
from django.views.generic import ListView


class ProfileView(ListView):
    """Profile view."""

    template_name = 'imager_profile/profile.html'

    context_object_name = 'one_profile'

    def get(self, *args, **kwargs):
        """Get."""
        if not self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)

    def get_queryset(self):
        """Get queryset."""
        owner = False
        if 'username' not in self.kwargs:
            username = self.request.user.get_username()
            owner = True
        else:
            username = self.kwargs['username']

        profile = get_object_or_404(ImagerProfile, user__username=username)
        if not owner:
            photos = Photo.objects.filter(published='PUBLIC', user__username=username)
            albums = Album.objects.filter(published='PUBLIC', user__username=username)
        else:
            albums = Album.objects.filter(user__username=username)
            photos = Photo.objects.filter(user__username=username)
        return [profile, albums, photos]

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context['profile'] = context['one_profile'][0]
        context['albums'] = context['one_profile'][1]
        context['photos'] = context['one_profile'][2]
        context['albums_private'] = context['albums'].filter(published='PRIVATE').count()
        context['albums_public'] = context['albums'].filter(published='PUBLIC').count()
        context['photos_private'] = context['photos'].filter(published='PRIVATE').count()
        context['photos_public'] = context['photos'].filter(published='PUBLIC').count()

        return context
