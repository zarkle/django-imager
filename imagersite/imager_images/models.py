"""."""
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.utils import timezone


class Photo(models.Model):
    """Photo model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    image = ImageField(upload_to='images')
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=7,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """String."""
        return '{}'.format(self.title)


class Album(models.Model):
    """Album model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    photos = models.ManyToManyField(Photo, related_name='albums')
    cover = models.ForeignKey(
        'Photo', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=7,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """String."""
        return '{}'.format(self.title)


@receiver(models.signals.post_save, sender=Photo)
def set_photo_published_date(sender, instance, **kwargs):
    """Set photo published date when made public."""
    if instance.published == 'PUBLIC' and not instance.date_published:
        instance.date_published = timezone.now()
        instance.save()


@receiver(models.signals.post_save, sender=Album)
def set_album_published_date(sender, instance, **kwargs):
    """Set album published date when made public."""
    if instance.published == 'PUBLIC' and not instance.date_published:
        instance.date_published = timezone.now()
        instance.save()
