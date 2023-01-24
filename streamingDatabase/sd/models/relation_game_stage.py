from .game import Game
from .stage import Stage
from django.db import models


class RelationGameStage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
