from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=80)
    discord_handler = models.CharField(max_length=120)
