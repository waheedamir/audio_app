from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError


class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now=True)
    file = models.FileField()


class Podcast(Song):
    host = models.CharField(max_length=100)


def restrict_participants(value):
    if Participants.objects.filter(podcast_id=value).count() > 10:
        raise ValidationError('This Podcast already have 10 Participants')


class Participants(models.Model):

    name = models.CharField(max_length=100)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='Participants')


class Audiobook(Song):
    author_name = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
