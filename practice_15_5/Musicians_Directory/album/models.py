from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
      album_name = models.CharField(max_length=20)
      album_release_date = models.DateField()
      rating = models.IntegerField()
      musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
      
      
      def __str__(self):
            return f'Album: {self.album_name}  ({self.album_release_date.strftime("%m/%d/%Y")})'