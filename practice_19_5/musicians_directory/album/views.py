from django.shortcuts import render
from . import forms, models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class AlbumCreateView(CreateView):
      model = models.Album
      template_name = 'album.html'
      form_class = forms.AlbumForm
      success_url = reverse_lazy('home')
      
      def form_valid(self, form):
            response = super().form_valid(form)
            return response
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Add'
            return context
      
@method_decorator(login_required, name = 'dispatch')
class AlbumUpdateView(UpdateView):
      model = models.Album
      form_class = forms.AlbumForm
      template_name = 'album.html'
      success_url = reverse_lazy('home')
      pk_url_kwargs = 'pk'
      
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['type'] = 'Update'
            return context

@method_decorator(login_required, name = 'dispatch')
class AlbumDeleteView(DeleteView):
      model = models.Album
      success_url = reverse_lazy('home')
      pk_url_kwargs = 'pk'
      template_name = 'delete_confirmation.html'
      
      def delete(self, request, *args, **kwargs):
            return super().delete(request, *args, **kwargs)