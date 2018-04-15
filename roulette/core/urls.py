from django.urls import path

from .views import LanguageListView, LanguageDetailView, IdeaListView, IdeaDetailView

urlpatterns = [
    path('languages/', LanguageListView.as_view()),
    path('<int:pk>/', LanguageDetailView.as_view()),
    path('ideas/', IdeaListView.as_view()),
    path('<int:pk>/', IdeaDetailView.as_view()),
]
