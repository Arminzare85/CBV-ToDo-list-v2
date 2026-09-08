from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('register/',UserRegisterView.as_view(),name='register'),
]