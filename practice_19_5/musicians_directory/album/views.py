from django.shortcuts import render
from . import forms, models
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class AlbumCreateView(CreateView):
      model = models.Album
      template_name = 'add_album.html'
      form_class = forms.AlbumForm
      success_url = reverse_lazy('add_album')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            return response