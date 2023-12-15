from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class AddMusicianView(CreateView):
      template_name = 'add_musician.html'
      form_class = forms.MusicianForm
      success_url = reverse_lazy('add_musician')
      model = models.Musician
      
      def form_valid(self, form):
            response = super().form_valid(form)
            return response