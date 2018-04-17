from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True)
    url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('core:language', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Idea(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    thumbnail = models.ImageField(blank=True)
    url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('core:idea', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    github_url = models.URLField()
    language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
    idea = models.ForeignKey(Idea, null=True, on_delete=models.SET_NULL)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('core:project', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
