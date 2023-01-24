from .person import Person
from .game import Game
from django.db import models


class RelationGameStreamer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)