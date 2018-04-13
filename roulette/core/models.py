from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    description = models.TextField()
    thumbnail = models.ImageField(height_field=500,width_field=500)
