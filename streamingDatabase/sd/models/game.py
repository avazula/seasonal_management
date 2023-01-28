from .team import Team
from django.db import models


class Game(models.Model):
    datetime = models.DateField(null=True)
