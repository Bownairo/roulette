from django.urls import path

from .views import LanguageListView, LanguageDetailView, IdeaListView, IdeaDetailView, ProjectListView, ProjectDetailView

urlpatterns = [
    path('languages/', LanguageListView.as_view()),
    path('<int:pk>/', LanguageDetailView.as_view()),
    path('ideas/', IdeaListView.as_view()),
    path('<int:pk>/', IdeaDetailView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
]
