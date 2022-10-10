from django.db import models

# Create your models here.

class MusicPlayer(models.Model):
    name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
