from django import forms
from . import models

class MusicianForm(forms.ModelForm):
      class Meta:
            model = models.Musician
            fields = '__all__'
            widgets = {
                  'instrument_type': forms.Textarea(attrs ={'rows': 3})
            }