from django.test import TestCase
from .models import Photo, Album, User
import factory
from random import choice
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
import os


class UserFactory(factory.django.DjangoModelFactory):
    """Test user."""

    class Meta:
        """Meta class."""

        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class PhotoFactory(factory.django.DjangoModelFactory):
    """Test photo."""

    class Meta:
        """Meta class."""

        model = Photo

    image = SimpleUploadedFile(
        name='image.jpg',
        content=open(
            os.path.join(settings.BASE_DIR, 'imagersite/static/windows.jpg'), 'rb'
        ).read(),
        content_type="image/jpeg"
    )
    title = factory.Faker('name')
    description = factory.Faker('sentence')
    date_uploaded = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    published = choice(['private', 'shared', 'public'])


class AlbumFactory(factory.django.DjangoModelFactory):
    """Test album."""

    class Meta:
        """Meta class."""

        model = Album

    title = factory.Faker('name')
    description = factory.Faker('sentence')
    date_created = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    published = choice(['private', 'shared', 'public'])


class PhotoUnitTests(TestCase):
    """Unit test photo."""

    @classmethod
    def setUpClass(cls):
        """Set up test database with one user who has 5 photos over 2 albums."""
        super(TestCase, cls)
        user = UserFactory.create()
        user.set_password(factory.Faker('password'))
        user.save()

        album = AlbumFactory.create(user=user)
        album.save()
        for _ in range(2):
            photo = PhotoFactory.create(user=user)
            photo.save()
            album.photos.add(photo)

        album2 = AlbumFactory.create(user=user)
        album2.save()
        for _ in range(3):
            photo = PhotoFactory.create(user=user)
            photo.save()
            album2.photos.add(photo)

    @classmethod
    def tearDownClass(cls):
        """Tear down test database."""
        User.objects.all().delete()
        super(TestCase, cls)

    def test_one_photo(self):
        """Test photo exists."""
        one_photo = Photo.objects.first()
        self.assertIsNotNone(one_photo)

    def test_photo_image(self):
        """Test photo has image."""
        image = Photo.objects.first()
        self.assertIsInstance(image.image, object)

    def test_photo_title(self):
        """Test photo has title."""
        image = Photo.objects.first()
        self.assertIsInstance(image.title, str)

    def test_photo_description(self):
        """Test photo has description."""
        image = Photo.objects.first()
        self.assertIsInstance(image.description, str)

    def test_photo_date_uploaded(self):
        """Test photo upload date."""
        image = Photo.objects.first()
        self.assertIsInstance(image.date_uploaded, object)

    def test_photo_date_modified(self):
        """Test photo modified date."""
        image = Photo.objects.first()
        self.assertIsInstance(image.date_modified, object)

    def test_photo_date_published(self):
        """Test photo published date."""
        image = Photo.objects.first()
        self.assertIsInstance(image.date_published, object)

    def test_photo_published(self):
        """Test photo published."""
        image = Photo.objects.first()
        self.assertIsInstance(image.published, str)

    def test_one_album(self):
        """Test album exists."""
        one_album = Album.objects.first()
        self.assertIsNotNone(one_album)

    def test_two_album(self):
        """Test all albums exist."""
        two_albums = Album.objects.all()
        self.assertEqual(2, len(two_albums))

    def test_album_title(self):
        """Test album title."""
        album = Album.objects.first()
        self.assertIsInstance(album.title, str)

    def test_album_description(self):
        """Test album description."""
        album = Album.objects.first()
        self.assertIsInstance(album.description, str)

    def test_album_date_created(self):
        """Test album created date."""
        album = Album.objects.first()
        self.assertIsInstance(album.date_created, object)

    def test_album_date_modified(self):
        """Test album modified date."""
        album = Album.objects.first()
        self.assertIsInstance(album.date_modified, object)

    def test_album_date_published(self):
        """Test album published date."""
        album = Album.objects.first()
        self.assertIsInstance(album.date_published, object)

    def test_album_published(self):
        """Test album published."""
        album = Album.objects.first()
        self.assertIsInstance(album.published, str)

    def test_album_lengths(self):
        """Test album has correct number of photos."""
        album = Album.objects.all()
        album, album2 = album[0], album[1]
        self.assertEqual(2, album.photos.count())
        self.assertEqual(3, album2.photos.count())
