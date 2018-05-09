from django.forms import ModelForm
from .models import Album, Photo


class AlbumForm(ModelForm):
    """Add photo form."""

    class Meta:
        """Meta."""
        model = Album
        fields = ['photos', 'cover', 'title', 'description', 'published']

    def __init__(self, *args, **kwargs):
        """Init."""
        username = kwargs.pop('username')
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(user__username=username)
        self.fields['photos'].queryset = Photo.objects.filter(user__username=username)
