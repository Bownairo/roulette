from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Language, Idea

class LanguageDetailView(generic.DetailView):
    model = Language

class LanguageListView(generic.ListView):
    model = Language

class IdeaDetailView(generic.DetailView):
    model = Idea

class IdeaListView(generic.ListView):
    model = Idea
