from django.contrib import admin

# Register your models here.
from .models import Language, Idea, Project

admin.site.register(Language)
admin.site.register(Idea)
admin.site.register(Project)
