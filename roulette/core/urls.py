from django.urls import path

from django.views.generic import TemplateView
from .views import LanguageListView, LanguageDetailView, IdeaListView, IdeaDetailView, ProjectListView, ProjectDetailView

app_name = 'core'
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html')),
    path('languages/', LanguageListView.as_view()),
    path('languages/<int:pk>/', LanguageDetailView.as_view()),
    path('ideas/', IdeaListView.as_view()),
    path('ideas/<int:pk>/', IdeaDetailView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
]
