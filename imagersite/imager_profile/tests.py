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
