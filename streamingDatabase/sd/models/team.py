from django.db import models


class Team(models.Model):
    short_name = models.CharField(max_length=15)
    full_name = models.CharField(max_length=120, null=True)
