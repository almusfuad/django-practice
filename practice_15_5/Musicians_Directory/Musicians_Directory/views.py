from django.shortcuts import render
from musician.models import Musician


def home(request):
      datas = Musician.objects.all()
      return render(request, 'home.html', {'datas': datas})