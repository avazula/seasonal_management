from .person import Person
from .team import Team
from django.db import models


class RelationTeamStreamer(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True)