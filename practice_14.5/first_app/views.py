from django.shortcuts import render
from first_app.forms import OrdinaryCodersForm

# Create your views here.
def blog1(request):
      if request.method == 'POST':
            form = OrdinaryCodersForm(request.POST)
            if form.is_valid():
                  print(form.cleaned_data)
      else:
            form = OrdinaryCodersForm()           
      return render(request, 'blog1.html', {'form': form})