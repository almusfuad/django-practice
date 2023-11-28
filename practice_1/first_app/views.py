from django.shortcuts import render

# Create your views here.


def geeksfor(request):
      return render(request, 'geeksfor.html')

def earthly(request):
      return render(request, 'earthly.html')