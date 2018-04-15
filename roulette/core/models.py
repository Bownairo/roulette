from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField()
    url = models.URLField()

class Idea(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField()
    url = models.URLField()

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    github_url = models.URLField()
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    idea = models.ForeignKey(Idea, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
