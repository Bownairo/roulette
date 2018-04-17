from django.urls import path

from django.views.generic import TemplateView
from .views import *

app_name = 'core'
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language'),
    path('languages/create/', LanguageCreateView.as_view(template_name='core/form.html'), name='language-add'),
    path('languages/update/<int:pk>/', LanguageUpdateView.as_view(template_name='core/form.html'), name='language-update'),
    path('languages/delete/<int:pk>/', LanguageDeleteView.as_view(template_name='core/delete.html'), name='language-delete'),
    path('ideas/', IdeaListView.as_view(), name='ideas'),
    path('ideas/<int:pk>/', IdeaDetailView.as_view(), name='idea'),
    path('ideas/create/', IdeaCreateView.as_view(template_name='core/form.html'), name='idea-add'),
    path('ideas/update/<int:pk>/', IdeaUpdateView.as_view(template_name='core/form.html'), name='idea-update'),
    path('ideas/delete/<int:pk>/', IdeaDeleteView.as_view(template_name='core/delete.html'), name='idea-delete'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project'),
    path('projects/create/', ProjectCreateView.as_view(template_name='core/form.html'), name='project-add'),
    path('projects/update/<int:pk>/', ProjectUpdateView.as_view(template_name='core/form.html'), name='project-update'),
    path('projects/delete/<int:pk>/', ProjectDeleteView.as_view(template_name='core/delete.html'), name='project-delete'),
]
