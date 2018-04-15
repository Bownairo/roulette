from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Language, Idea, Project

class LanguageListView(generic.ListView):
    model = Language

class LanguageDetailView(generic.DetailView):
    model = Language

class IdeaListView(generic.ListView):
    model = Idea

class IdeaDetailView(generic.DetailView):
    model = Idea

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project
