from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=80)
    discord_handler = models.CharField(max_length=120)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['username', 'discord_handler'], name='Only one person with same name+discord account')
        ]