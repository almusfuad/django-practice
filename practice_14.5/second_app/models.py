from django.db import models

# Create your models here.
class GeeksModel(models.Model):
      title = models.CharField(max_length=20)
      description = models.TextField(max_length=100)
      last_modified = models.DateTimeField(auto_now_add=True)
      img = models.ImageField(upload_to='images/')

      def __str__(self):
            return f'Title: {self.title} \n Last Modified: {self.last_modified}'