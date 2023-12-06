from django import forms
from third_app.models import ExampleModel

class ExampleForm(forms.ModelForm):
      class Meta:
            model = ExampleModel
            fields = '__all__'