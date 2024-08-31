from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from allauth.account.views import LoginView, SignupView
from sushi.models import Sushi


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_sushi'] = Sushi.objects.order_by('-created_at')[:4]
        return context


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_sushi'] = Sushi.objects.order_by('-created_at')[:4]
        return context