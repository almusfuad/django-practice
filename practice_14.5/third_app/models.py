from django.db import models

# Create your models here.
class ExampleModel(models.Model):
      auto_field = models.AutoField(primary_key=True) #BigAutoField is same as autofield. But it can generate a larger integer value
      big_integer_field = models.BigIntegerField() # It can stores a large integer values
      binary_field = models.BinaryField() # Used to store raw binary data, such as images or files, in the database
      boolean_field = models.BooleanField() # Store True or False
      # comma_separated_integer = models.CharField(validators=[comma_separated_integer]) # This field is deprecated
      date_field = models.DateField() # Commonly used to represent date in database
      date_time_field = models.DateTimeField() # Commonly used to represent date and time in database
      decimal_field = models.DecimalField(max_digits=5, decimal_places=2) # Used to store decimal values. Where max digit before decimal can be 5 and after can be 2
      email_field = models.EmailField() # used to store email values
      file_field = models.FileField(upload_to='files/') # used to store file values. It saved to the file system and path
      # file_path = models.FilePathField(path='path/to/file')
      ip_address = models.GenericIPAddressField(protocol='both') # used  to store IP address
      image_field = models.ImageField(upload_to = 'images/') # used to store image
      json_field = models.JSONField() # stores JSON-encoded data, schema less storage of structured data
      positive_big_integer = models.PositiveIntegerField() # stores positive integer values
      positive_small_integer = models.PositiveSmallIntegerField() # stores positive small integer values
      slug_field = models.SlugField() # used to store a short label or identifier suitable for use in URLS
      time_field = models.TimeField() # stores time values (hours, minutes, seconds)
      url_field = models.URLField() # used to store url values
      uuid_field = models.UUIDField() # used to store UUID values
      
      
      

class ExampleModel2(models.Model):
      foreign_key = models.ForeignKey(ExampleModel, on_delete = models.CASCADE)
      # many_to_many = models.ManyToManyField(ExampleModel) # This represents many to many relationships
      # one_to_one = models.OneToOneField(ExampleModel, on_delete=models.CASCADE) # This represents one to one relationship


