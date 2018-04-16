from django.urls import path

from django.views.generic import TemplateView
from .views import LanguageListView, LanguageDetailView, LanguageCreateView, IdeaListView, IdeaDetailView, IdeaCreateView, ProjectListView, ProjectDetailView, ProjectCreateView

app_name = 'core'
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language'),
    path('languages/create/', LanguageCreateView.as_view(template_name='core/form.html'), name='language-add'),
    path('ideas/', IdeaListView.as_view(), name='ideas'),
    path('ideas/<int:pk>/', IdeaDetailView.as_view(), name='idea'),
    path('ideas/create/', IdeaCreateView.as_view(template_name='core/form.html'), name='idea-add'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project'),
    path('projects/create/', ProjectCreateView.as_view(template_name='core/form.html'), name='project-add'),
]
