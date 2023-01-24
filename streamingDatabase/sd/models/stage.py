from django.db import models


class Stage(models.Model):
    name = models.CharField(max_length=40)