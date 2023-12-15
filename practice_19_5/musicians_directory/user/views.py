from django.shortcuts import render, redirect
from . import forms
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class UserRegisterView(View):
      template_name = 'authentication.html'
      form_class = forms.RegisterForm
      
      def get(self, request, *args, **kwargs):
            register_form = self.form_class()
            return render(request, self.template_name, {'form': register_form, 'type': 'Register'})
      
      def post(self, request, *args, **kwargs):
            register_form = self.form_class(request.POST)
            if register_form.is_valid():
                  register_form.save()
                  return redirect('login')
            return render(request, self.template_name, {'form': register_form, 'type': 'Register'})
      
      
class UserLoginView(LoginView):
      template_name = 'authentication.html'
      form_class = AuthenticationForm
      
      def get_success_url(self):
            return reverse_lazy('login')
      
      def form_valid(self, form):
            messages.success(self.request, 'Logged in successfully.')
            return super().form_valid(form)
      
      def form_invalid(self, form):
            messages.error(self.request, 'Logged in Failed.')
            return super().form_valid(form)
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Login'
            return context