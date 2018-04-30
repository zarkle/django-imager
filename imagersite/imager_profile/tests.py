from django.test import TestCase
from .models import ImagerProfile, User
import factory
from random import uniform, choice
from django.urls import reverse_lazy


class UserFactory(factory.django.DjangoModelFactory):
    """Test user."""

    class Meta:
        """Meta."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


def populate_profile(user, **kwargs):
    """Populate profile."""
    user.profile.bio = kwargs['bio'] if 'bio' in kwargs else factory.Faker('paragraph')
    user.profile.phone = kwargs['phone'] if 'phone' in kwargs else factory.Faker('phone_number')
    user.profile.location = kwargs['location'] if 'location' in kwargs else factory.Faker('city')
    user.profile.website = kwargs['website'] if 'website' in kwargs else factory.Faker('url')
    user.profile.fee = kwargs['fee'] if 'fee' in kwargs else uniform(0.00, 5.00)
    user.profile.camera = kwargs['camera'] if 'camera' in kwargs else choice(
        ['DSLR', 'M', 'AC', 'SLR'])
    user.profile.services = kwargs['services'] if 'services' in kwargs else choice(
        ['weddings', 'headshots', 'landscape'])
    user.profile.photostyles = kwargs['photostyles'] if 'photostyles' in kwargs else choice(
        ['night', 'macro', '3d'])


class ProfileUnitTests(TestCase):
    """Unit test profile."""

    @classmethod
    def setUpClass(cls):
        """Set up test database."""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()
            populate_profile(user, phone='1234567')
            user.profile.save()

    @classmethod
    def tearDownClass(cls):
        """Tear down test database."""
        User.objects.all().delete()
        super(TestCase, cls)

    def test_user_can_see_its_profile(self):
        """Test to see if user has profile."""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_delete_user_will_delete_profile(self):
        """Test that profile is deleted when user is deleted."""
        one_user = User.objects.first()
        self.assertIsNotNone(ImagerProfile.objects.filter(user=one_user))
        one_user.delete()
        self.assertFalse(ImagerProfile.objects.filter(user=one_user).exists())

    def test_imager_profile_bio(self):
        """Test profile has bio."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.bio, str)

    def test_imager_profile_phone(self):
        """Test profile has phone."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.phone, str)

    def test_imager_profile_location(self):
        """Test profile has location."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.location, str)

    def test_imager_profile_website(self):
        """Test profile has website."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.website, str)

    def test_imager_profile_fee(self):
        """Test profile has fee."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.fee, float)

    def test_imager_profile_camera(self):
        """Test profile has camera."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.camera, str)

    def test_imager_profile_services(self):
        """Test profile has services."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.services, list)

    def test_imager_profile_photostyles(self):
        """Test profile has photostyles."""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.photostyles, list)

    def test_string_profile(self):
        """Test string magic method on Profile class."""
        self.assertIsNotNone(str(ImagerProfile.objects.first()))

    def test_profile_not_logged_in(self):
        """Test profile route."""
        response = self.client.get(reverse_lazy('profile'))
        self.assertEqual(response.status_code, 302)


