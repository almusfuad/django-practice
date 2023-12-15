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
      
      # def get(self, request, *args, **kwargs):
      #       musician_form = self.form_class()
      #       return render(request, self.template_name, {'form': musician_form})
      
      
      # def post(self, request, *args, **kwargs):
      #       musician_form = self.form_class(request.POST)
      #       if musician_form.is_valid():
      #             musician_form.save(commit = False)
      #             return redirect('add_musician')
      #       return render(request, self.template_name, {'form': musician_form})