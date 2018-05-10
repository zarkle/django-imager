from django.urls import path
from .views import ProfileView, EditProfileView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('<str:username>', ProfileView.as_view(), name='named_profile'),
    path('/edit/<str:username>', EditProfileView.as_view(), name='edit_profile'),
]
