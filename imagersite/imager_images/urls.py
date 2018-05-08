from django.urls import path
from .views import LibraryView, album_view, photo_view, album_detail_view, photo_detail_view


urlpatterns = [
    path('library/', LibraryView.as_view(), name='library'),
    path('albums/', album_view, name='albums'),
    path('photos/', photo_view, name='photos'),
    path('albums/<int:id>', album_detail_view, name='album_detail'),
    path('photos/<int:id>', photo_detail_view, name='photo_detail'),
]
