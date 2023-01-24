from .game import Game
from .team import Team
from django.db import models


class RelationGameTeam(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
