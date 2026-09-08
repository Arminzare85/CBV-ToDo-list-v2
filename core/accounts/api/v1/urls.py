from django.urls import path
from .views import *

urlpatterns = [
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path("verify-email/", UserVerifyView.as_view(), name="verify-email"),
    path("verify-email/<uid>/<token>/", VerifyEmailView.as_view(), name="confirm-email"),
]