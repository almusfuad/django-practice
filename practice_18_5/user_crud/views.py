from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
def home(request):
      return render(request, 'home.html')


def signup(request):
      if request.method == 'POST':
            signup_form = forms.SignUpForm(request.POST)
            if signup_form.is_valid():
                  signup_form.save()
                  messages.success(request, 'Account created successfully.')
                  messages.info(request, 'Error creating account.')         
      else:
            signup_form = forms.SignUpForm()
      return render(request, 'signup.html', {'form': signup_form})


def user_login(request):
      if request.method == 'POST':
            login_form = AuthenticationForm(request = request, data = request.POST)
            if login_form.is_valid():
                  username = login_form.cleaned_data['username']
                  userpass = login_form.cleaned_data['password']
                  user = authenticate(username = username, password = userpass)
                  if user is not None:
                        login(request, user)
                        messages.success(request, 'Logged in successfully.')
                        return redirect('profile')
                  else:
                        messages.info(request, 'Error logging in account.')
      else:
            login_form = AuthenticationForm()
      return render(request, 'login.html', {'form': login_form})


def profile(request):
      if request.user.is_authenticated:
            infos = User.objects.filter(username = request.user)
            return render(request, 'profile.html', {'infos': infos})
      else:
            return redirect('login')
      

def user_logout(request):
      if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Logged out successfully.')
            return redirect('home')
      

