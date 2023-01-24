from .person import Person
from django.db import models


class Streamer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    discord_handler = models.CharField(max_length=120)
    twitch_handler = models.CharField(max_length=120, null=True)
    youtube_handler = models.CharField(max_length=120, null=True)
    bilibili_handler = models.CharField(max_length=120, null=True)
