from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Language

class LanguageDetailView(generic.DetailView):
    model = Language

class LanguageListView(generic.ListView):
    model = Language
