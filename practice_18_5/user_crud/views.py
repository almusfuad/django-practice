from django.shortcuts import render
from . import forms
from django.contrib import messages

# Create your views here.
def home(request):
      return render(request, 'home.html')


def signup(request):
      if request.method == 'POST':
            signup_form = forms.SignUpForm(request.POST)
            if signup_form.is_valid():
                  signup_form.save()
                  messages.success(request, 'Account created successfully.')
                  messages.error(request, 'Error creating account.')         
      else:
            signup_form = forms.SignUpForm()
      return render(request, 'signup.html', {'form': signup_form})