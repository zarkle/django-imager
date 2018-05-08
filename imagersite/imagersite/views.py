from django.views.generic import TemplateView
from imager_images.models import Photo
import random


class HomeView(TemplateView):
    """Home view class."""

    template_name = 'generic/home.html'

    def get_context_data(self, **kwargs):
        """Get context."""
        context = super().get_context_data(**kwargs)

        all_photos = Photo.objects.filter(published='PUBLIC')
        if all_photos.count():
            one_photo = random.choice(all_photos)
            image_url = one_photo.image.url
        else:
            image_url = 'static/windows.jpg'

        context['image_url'] = image_url

        return context
