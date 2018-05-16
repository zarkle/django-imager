from rest_framework import serializers
from imager_images.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Serialize photo instances."""

    class Meta:
        """Cast as Photo objects with all fields."""

        model = Photo
        fields = (
            'id',
            'user',
            'image',
            'title',
            'description',
            'date_uploaded',
            'date_modified',
            'date_published',
            'published',
            )
