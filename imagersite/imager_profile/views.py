from django.shortcuts import redirect, get_object_or_404
from imager_images.models import Album, Photo
from .models import ImagerProfile
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """Profile view."""

    template_name = 'imager_profile/profile.html'

    def get_context_data(self, **kwargs):
        owner = False

        if 'username' not in self.kwargs:
            username = self.request.user.get_username()
            owner = True
            if username == '':
                return redirect('home')
        else:
            username = self.kwargs['username']

        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(ImagerProfile, user__username=username)
        context['albums'] = Album.objects.filter(user__username=username)
        context['photos'] = Photo.objects.filter(user__username=username)
        context['albums_private'] = context['albums'].filter(published='PRIVATE').count()
        context['albums_public'] = context['albums'].filter(published='PUBLIC').count()
        context['photos_private'] = context['photos'].filter(published='PRIVATE').count()
        context['photos_public'] = context['photos'].filter(published='PUBLIC').count()

        if not owner:
            context['photos'] = Photo.objects.filter(published='PUBLIC', user__username=username)
            context['albums'] = Album.objects.filter(published='PUBLIC', user__username=username)
            context['albums_private'] = context['photos_private'] = 0

        return context
