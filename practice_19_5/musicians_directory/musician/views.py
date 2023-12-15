from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class AddMusicianView(CreateView):
      template_name = 'musician.html'
      form_class = forms.MusicianForm
      success_url = reverse_lazy('add_album')
      model = models.Musician
      
      def form_valid(self, form):
            response = super().form_valid(form)
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Add'
            return context
      
      
class MusicianUpdateView(UpdateView):
      model = models.Musician
      form_class = forms.MusicianForm
      template_name = 'musician.html'
      success_url = reverse_lazy('home')
      pk_url_kwargs = 'pk'
      
      def form_valid(self, form):
            response = super().form_valid(form)
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Update'
            return context