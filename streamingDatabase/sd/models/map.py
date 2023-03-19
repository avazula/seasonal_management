from django.db import models


class Map(models.Model):
    short_name = models.CharField(max_length=5, null=True)
    full_name = models.CharField(max_length=120)
    game_mode = models.CharField(max_length=15)  # Warfare || Offensive
