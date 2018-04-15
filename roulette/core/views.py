from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Language, Idea

class LanguageListView(generic.ListView):
    model = Language

class LanguageDetailView(generic.DetailView):
    model = Language

class IdeaListView(generic.ListView):
    model = Idea

class IdeaDetailView(generic.DetailView):
    model = Idea
