from django.shortcuts import render
from first_app.forms import ExampleForm

# Create your views here.
def blog1(request):
      if request.method == 'POST':
            form = ExampleForm(request.POST)
            if form.is_valid():
                  print(form.cleaned_data)
      else:
            form = ExampleForm()           
      return render(request, 'blog1.html', {'form': form})