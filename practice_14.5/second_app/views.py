from django.shortcuts import render
from second_app.forms import GeeksForm

# handle uploaded file
def handle_uploaded_file(f):
      with open('second_app/static/uploaded_files/'+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                  print(chunk)
                  destination.write(chunk)

# Create your views here.
def blog2(request):
      if request.method == 'POST':
            form = GeeksForm(request.POST, request.FILES)
            if form.is_valid():
                  handle_uploaded_file(request.FILES['files'])
      else: 
            form = GeeksForm()
      return render(request, 'blog2.html', {'form': form})