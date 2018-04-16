from django.urls import path

from django.views.generic import TemplateView
from .views import LanguageListView, LanguageDetailView, IdeaListView, IdeaDetailView, ProjectListView, ProjectDetailView

app_name = 'core'
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='index'),
    path('languages/', LanguageListView.as_view(), name='languages'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language'),
    path('ideas/', IdeaListView.as_view(), name='ideas'),
    path('ideas/<int:pk>/', IdeaDetailView.as_view(), name='idea'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project'),
]
