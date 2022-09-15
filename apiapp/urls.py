from django.urls import path
from .views import PodcastListView, PodcasterDetailView
urlpatterns = [
    path('', PodcastListView.as_view()),
    path('<int:pk>', PodcasterDetailView.as_view()),
]