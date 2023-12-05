from django.shortcuts import render
from first_app.forms import UserForm

# Create your views here.
def home(request):
      form = UserForm()
      return render(request, 'home.html', {'form': form})