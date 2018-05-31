from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class ActiveImagerProfileManager(models.Manager):
    """Custom manager for only active profiles."""

    def get_queryset(self):
        """Limit the queryset to only profiles with active users."""
        all_profiles = super(ActiveImagerProfileManager, self).get_queryset()
        return all_profiles.filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    website = models.URLField(max_length=180, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    camera = models.CharField(
        max_length=180, blank=True, null=True, choices=(
            ('DSLR', 'Digital Single Lens Reflex'),
            ('M', 'Mirrorless'),
            ('AC', 'Advanced Compact'),
            ('SLR', 'Single Lens Reflex')))
    services = MultiSelectField(
        choices=(
            ('weddings', 'Weddings'),
            ('headshots', 'HeadShots'),
            ('landscape', 'LandScape'),
            ('portraits', 'Portraits'),
            ('art', 'Art')))
    photostyles = MultiSelectField(
        choices=(
            ('blackandwhite', 'Black and White'),
            ('night', 'Night'),
            ('macro', 'Macro'),
            ('3d', '3D'),
            ('artistic', 'Artistic'),
            ('underwater', 'Underwater')))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """String."""
        return self.user.username

    @property
    def is_active(self):
        """Whether the User of the profile is active or not."""
        return self.user.is_active

    objects = models.Manager()
    active = ActiveImagerProfileManager()


@receiver(models.signals.post_save, sender=User)
def create_profile(sender, **kwargs):
    """Create an empty profile anytime a new user is created."""
    if kwargs['created']:
        Token.objects.create(user=kwargs['instance'])
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
