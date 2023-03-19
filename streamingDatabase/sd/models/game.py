from .team import Team
from django.db import models


class Game(models.Model):
    datetime = models.DateTimeField(null=True)
