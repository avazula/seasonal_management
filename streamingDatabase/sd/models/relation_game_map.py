from .game import Game
from .map import Map
from django.db import models


class RelationGameMap(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
