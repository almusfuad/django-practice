from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from album.models import Album
from django.views.generic import ListView, CreateView

# Create your views here.
class HomeDetails(ListView):
      model = Album
      template_name = 'home.html'
      context_object_name = 'albums'

class UserRegisterView(CreateView):
      template_name = 'authentication.html'
      form_class = UserCreationForm
      success_url = reverse_lazy('login')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Registered successfully.')
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Register'
            return context
      
      
class UserLoginView(LoginView):
      template_name = 'authentication.html'
      form_class = AuthenticationForm
      
      def get_success_url(self):
            return reverse_lazy('home')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            messages.success(self.request, 'Logged in successfully.')
            return response
      
      def form_invalid(self, form):
            messages.error(self.request, 'Logged in Failed.')
            return super().form_valid(form)
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Login'
            return context
      
class UserLogoutView(LogoutView):
      def get_success_url(self):
            return reverse_lazy('home')