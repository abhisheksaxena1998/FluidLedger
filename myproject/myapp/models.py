from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    bloodgroup = models.CharField(max_length=30)
    preference = models.CharField(max_length=30)
    recent  =	models.CharField(max_length=30)
    frequent = models.CharField(max_length=30)
    monetary = models.CharField(max_length=30)
    times = models.CharField(max_length=30)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
