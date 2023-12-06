from django.shortcuts import render
from third_app.forms import ExampleForm

# Create your views here.
def blog3(request):
      if request.method == 'POST':
            form = ExampleForm(request.POST, request.Files)
            if form.is_valid():
                  print(form)
                  form.save()
      else:
            form = ExampleForm()
      return render(request, 'blog3.html', {'form': form})