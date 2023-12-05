from django.db import models

# Create your models here.
class User(models.Model):
      name = models.CharField(max_length=20)
      email = models.EmailField(max_length=20)
      contact = models.IntegerField(max_length=11)
      exp = models.IntegerField(max_length=2)