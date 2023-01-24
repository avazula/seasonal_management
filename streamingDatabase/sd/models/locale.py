from django.db import models


class Locale(models.Model):
    time = models.CharField(max_length=6)
    abbreviation = models.CharField(max_length=20, null=True)
