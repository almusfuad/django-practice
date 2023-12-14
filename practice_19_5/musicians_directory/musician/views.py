from django.shortcuts import render, redirect
from . import forms
from django.views import View

# Create your views here.
class AddMusicianView(View):
      template_name = 'add_musician.html'
      form_class = forms.MusicianForm
      
      def get(self, request, *args, **kwargs):
            musician_form = self.form_class()
            return render(request, self.template_name, {'form': musician_form})
      
      
      def post(self, request, *args, **kwargs):
            musician_form = self.form_class(request.POST)
            if musician_form.is_valid():
                  musician_form.save(commit = False)
                  return redirect('add_musician')
            return render(request, self.template_name, {'form': musician_form})