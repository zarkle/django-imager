from django.urls import path
from .views import (
    LibraryView,
    AlbumView,
    PhotoView,
    AlbumDetailView,
    PhotoDetailView,
    AddPhotoView,
    AddAlbumView,
    EditAlbumView,
    EditPhotoView,
    )


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('albums/', AlbumView.as_view(), name='albums'),
    path('photos/', PhotoView.as_view(), name='photos'),
    path('albums/<int:id>', AlbumDetailView.as_view(), name='album_detail'),
    path('photos/<int:id>', PhotoDetailView.as_view(), name='photo_detail'),
    path('albums/add/', AddAlbumView.as_view(), name='add_album'),
    path('photos/add/', AddPhotoView.as_view(), name='add_photo'),
    path('albums/<int:id>/edit', EditAlbumView.as_view(), name='edit_album'),
    path('photos/<int:id>/edit', EditPhotoView.as_view(), name='edit_photo'),
]
