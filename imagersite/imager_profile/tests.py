from django.test import TestCase
from .models import ImagerProfile, User
import factory
from random import uniform, choice


class UserFactory(factory.django.DjangoModelFactory):
    """test user"""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """test profile"""
    class Meta:
        model = ImagerProfile

    bio = factory.Faker('paragraph')
    phone = factory.Faker('phone_number')
    location = factory.Faker('city')
    website = factory.Faker('url')
    fee = uniform(0.00, 5.00)
    camera = choice(['DSLR', 'M', 'AC', 'SLR'])
    services = choice(['weddings', 'headshots', 'landscape'])
    photostyles = choice(['night', 'macro', '3d'])


class ProfileUnitTests(TestCase):
    """unit test profile"""
    @classmethod
    def setUpClass(cls):
        """set up test database"""
        super(TestCase, cls)
        for _ in range(50):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            profile = ProfileFactory.create(user=user)
            profile.save()

    @classmethod
    def tearDownClass(cls):
        """tear down test database"""
        User.objects.all().delete()
        super(TestCase, cls)

    def test_user_can_see_its_profile(self):
        """test to see if user has profile"""
        one_user = User.objects.first()
        self.assertIsNotNone(one_user.profile)

    def test_delete_user_will_delete_profile(self):
        """test that profile is deleted when user is deleted"""
        one_user = User.objects.first()
        self.assertIsNotNone(ImagerProfile.objects.filter(user=one_user))
        one_user.delete()
        self.assertFalse(ImagerProfile.objects.filter(user=one_user).exists())

    def test_imager_profile_bio(self):
        """test profile has bio"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.bio, str)

    def test_imager_profile_phone(self):
        """test profile has phone"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.phone, str)

    def test_imager_profile_location(self):
        """test profile has location"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.location, str)

    def test_imager_profile_website(self):
        """test profile has website"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.website, str)

    def test_imager_profile_fee(self):
        """test profile has fee"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.fee, float)

    def test_imager_profile_camera(self):
        """test profile has camera"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.camera, str)

    def test_imager_profile_services(self):
        """test profile has services"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.services, list)

    def test_imager_profile_photostyles(self):
        """test profile has photostyles"""
        prof = ImagerProfile.objects.first()
        self.assertIsInstance(prof.photostyles, list)
