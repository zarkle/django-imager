from django.urls import path
from .views import library_view, album_view, photo_view


urlpatterns = [
    path('library', library_view, name='library'),
    path('albums', album_view, name='albums'),
    path('photos', photo_view, name='photos'),
    # path('<str:username>', profile_view, name='named_profile'),

]
