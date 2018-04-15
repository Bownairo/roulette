from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    description = models.TextField()
    thumbnail = models.ImageField()

class Idea(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField()
    url = models.URLField()
