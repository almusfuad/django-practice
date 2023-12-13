from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

# Create your views here.
def home(request):
      if not request.user.is_authenticated:
            return render(request, 'home.html')


def signup(request):
      if not request.user.is_authenticated:
            if request.method == 'POST':
                  signup_form = forms.SignUpForm(request.POST)
                  if signup_form.is_valid():
                        signup_form.save()
                        messages.success(request, 'Account created successfully.')
                        return redirect('login')        
            else:
                  signup_form = forms.SignUpForm()
            return render(request, 'signup.html', {'form': signup_form})
      else:
            return redirect('profile')


def user_login(request):
      if not request.user.is_authenticated:
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
                              messages.error(request, 'Error logging in account.')
            else:
                  login_form = AuthenticationForm()
            return render(request, 'login.html', {'form': login_form})
      else:
            redirect('profile')


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
      

def update_user_pass(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  pass_form = PasswordChangeForm(user = request.user, data = request.POST)
                  if pass_form.is_valid():
                        pass_form.save()
                        update_session_auth_hash(request, pass_form.user)
                        messages.warning(request, 'Password updated successfully.')
                        return redirect('profile')
            else:
                  pass_form = PasswordChangeForm(user = request.user)
            return render(request, 'pass_change.html', {'form': pass_form, 'type': 'Update Password'})
      else:
            return redirect('login')
      

def set_user_pass(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  pass_form = SetPasswordForm(user = request.user, data = request.POST)
                  if pass_form.is_valid():
                        pass_form.save()
                        update_session_auth_hash(request, pass_form.user)
                        messages.warning(request, 'Password set successfully.')
                        return redirect('profile')
            else:
                  pass_form = SetPasswordForm(user = request.user)
            return render(request, 'pass_change.html', {'form': pass_form, 'type': 'Set Password'})
      else:
            return redirect('login')