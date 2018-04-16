from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Language, Idea, Project

class LanguageListView(generic.ListView):
    model = Language

class LanguageDetailView(generic.DetailView):
    model = Language

class LanguageCreateView(generic.edit.CreateView):
    model = Language
    fields = '__all__'

class IdeaListView(generic.ListView):
    model = Idea

class IdeaDetailView(generic.DetailView):
    model = Idea

class IdeaCreateView(generic.edit.CreateView):
    model = Idea
    fields = '__all__'

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreateView(generic.edit.CreateView):
    model = Project
    fields = '__all__'
