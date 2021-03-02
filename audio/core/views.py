from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Song, Audiobook, Podcast, Participants
from . import serializers


# Create your views here.

class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer


class AudiobookModelViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = serializers.AudiobookSerializer


class PodcastModelViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer


def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")
