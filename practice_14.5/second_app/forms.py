from django import forms
from second_app.models import GeeksModel


class GeeksForm(forms.ModelForm):
      class Meta:
            model = GeeksModel
            fields = { 'description','img', 'title',}
            required = {
                  'title': True,
                  'description': False,
            }
            help_texts = {
                  'description': 'Enter a brief of the image',
            }
            widgets = {
                  'title': forms.TextInput(attrs={'size': 50}),
                  'description': forms.Textarea(attrs={'rows': 2}),
            }
            labels = {
                  'img' : 'Image',
            }
      
      agree = forms.BooleanField(label='I agree to the terms and conditions',)
      duration = forms.DurationField(disabled=True, help_text='Input as DD HH:MM:SS',)
      upload_files = forms.FileField(label='Upload files')
      files_path = forms.FilePathField(path='second_app/')
      
      # ipaddress
      ipAddress = forms.GenericIPAddressField(label='IPv4 address', protocol='IPv4')
      
      # Null boolean field
      null_boolean = forms.NullBooleanField(label='Null boolean') 
      
      # regex field
      regex_field = forms.RegexField(label = 'regex field', regex = "G.*s")

      # slug field field is used for URL
      slug_field = forms.SlugField(label='slug field', max_length=200)
      
      # urls field
      url_field = forms.URLField(label='url field', max_length=200)
      # UUID field. It generates 128 bits as ids
      uuid_field = forms.UUIDField(label='uuid field', max_length=200)
      