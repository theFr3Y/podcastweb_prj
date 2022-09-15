from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import PodcastSerializer, PodcasterSerializer
from mainapp.models import PodcastModel, PodcasterModel

# display podcasts api
class PodcastListView(ListCreateAPIView):
    queryset = PodcastModel.objects.all()
    serializer_class = PodcastSerializer
    permission_class = IsAdminUser

# display Podcasters api
class PodcasterDetailView(RetrieveDestroyAPIView):
    queryset = PodcasterModel.objects.all()
    serializer_class = PodcasterSerializer
    permission_class = IsAdminUser