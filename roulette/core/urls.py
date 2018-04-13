from django.urls import path

from .views import LanguageListView, LanguageDetailView

urlpatterns = [
    path('', LanguageListView.as_view()),
    path('<int:pk>/', LanguageDetailView.as_view()),
]
