from django import forms
from first_app.models import User
import datetime

FAVORITE_COLORS_CHOICES = [
      ('black', 'Black'),
      ('white', 'White'),
      ('green', 'Green'),
      ('blue', 'Blue'),
      ('red', 'Red'),
]

class ExampleForm(forms.Form):
      # class Meta:
      #       model = User
      #       fields = '__all__'
            
      #       widgets = {
      #             'address': forms.CharField(widget=forms.Textarea),
                  
      #       }
      
      # common field with core arguments
      name = forms.CharField(
            max_length=20,
            label = "Please enter your name",
            required=True,
                        
      )
      message = forms.CharField(
            widget=forms.Textarea(attrs={'rows': 2}), 
            max_length=200
      )
      email = forms.EmailField(
            required=True,
            label="Please enter your email address",     
      )
      agree = forms.BooleanField(
            initial=False,
      )
      date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
      birth_year = forms.DateField(
            widget = forms.SelectDateWidget(years=range(1990, 2099)),
            initial=datetime.date.today,
      )
      value = forms.DecimalField() 
      
      
      # choiceField, MultipleChoiceField, ModelChoiceField and ModelMultipleChoiceField
      favorite_color = forms.ChoiceField(
            choices = FAVORITE_COLORS_CHOICES,
      )
      
      # choiceField with RadioSelect
      favorite_color = forms.ChoiceField(
            widget = forms.RadioSelect,
            choices= FAVORITE_COLORS_CHOICES,
      )
      
      # multiple choiceField with box select
      colors = forms.MultipleChoiceField(
            widget = forms.CheckboxSelectMultiple,
            choices= FAVORITE_COLORS_CHOICES,
      )
      
      

