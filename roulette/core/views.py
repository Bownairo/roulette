from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
from .models import Language, Idea, Project

class LanguageListView(generic.ListView):
    model = Language

class LanguageDetailView(generic.DetailView):
    model = Language

class LanguageCreateView(generic.edit.CreateView):
    model = Language
    fields = '__all__'

class LanguageUpdateView(generic.edit.UpdateView):
    model = Language
    fields = '__all__'

class LanguageDeleteView(generic.edit.DeleteView):
    model = Language
    success_url = reverse_lazy('language-list')

class IdeaListView(generic.ListView):
    model = Idea

class IdeaDetailView(generic.DetailView):
    model = Idea

class IdeaCreateView(generic.edit.CreateView):
    model = Idea
    fields = '__all__'

class IdeaUpdateView(generic.edit.UpdateView):
    model = Idea
    fields = '__all__'

class IdeaDeleteView(generic.edit.DeleteView):
    model = Idea
    success_url = reverse_lazy('idea-list')

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

class ProjectCreateView(generic.edit.CreateView):
    model = Project
    fields = '__all__'

class ProjectUpdateView(generic.edit.UpdateView):
    model = Project
    fields = '__all__'

class ProjectDeleteView(generic.edit.DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')
