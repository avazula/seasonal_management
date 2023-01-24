from .team import Team
from django.db import models


class Game(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
