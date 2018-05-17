from rest_framework import generics
from .serializers import PhotoSerializer
from imager_images.models import Photo


class PhotoListApi(generics.ListAPIView):
    """Serialize data."""

    serializer_class = PhotoSerializer

    def get_queryset(self):
        """Get all users photos."""
        return Photo.objects.filter(user=self.request.user)
