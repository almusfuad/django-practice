from django import forms 
from django.core import validators
from . import models
from datetime import datetime

class AlbumForm(forms.ModelForm):
      class Meta:
            model = models.Album
            fields = '__all__'
            
            widgets = {
                  'release_date': forms.DateInput(attrs={'type': 'date'}),
                  'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
            }
            
            validators = {
                  'rating': [
                        validators.MinValueValidator(1, message = 'Rating must be at least 1'),
                        validators.MaxValueValidator(1, message = 'Rating must be at most 5')
                  ]
            }