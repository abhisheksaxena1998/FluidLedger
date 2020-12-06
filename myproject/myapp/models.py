from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    

class UserFeedback(models.Model):
    subject = models.CharField(max_length=100)
    feedback = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)


class Favourite(models.Model):
    username = models.CharField(max_length=100)
    pid = models.IntegerField()
    posttitle = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


class DetailedUser(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    age = models.IntegerField()
    bloodgroup = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    recent = models.CharField(max_length=100)
    frequent = models.CharField(max_length=100)
    monetary = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    