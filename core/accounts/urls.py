from django.contrib import admin
from django.urls import path 
from django.views.generic import TemplateView 
from .views import UserLoginView , UserLogoutView , UserSignupView
from .views import UserPasswordResetView , UserPasswordResetDoneView , UserPasswordResetConfirmView , UserPasswordResetCompleteView
from django.urls import include

app_name = 'accounts'

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('signup/',UserSignupView.as_view(),name='signup'),
    path('password_reset/',UserPasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',UserPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',UserPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset/complete/',UserPasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('api/v1/',include('accounts.api.v1.urls')),
]