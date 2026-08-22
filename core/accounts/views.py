
from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView 
from django.urls import reverse_lazy
from .forms import UserSignupForm
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'



class UserLogoutView(LogoutView):
    template_name = 'accounts/login.html'

class UserSignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserSignupForm
    success_url = reverse_lazy('accounts:login')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/reset-password.html'
    success_url = reverse_lazy('accounts:password_reset_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/reset-password-sent.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset-password-confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password-changed.html'



    




