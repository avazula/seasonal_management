from .team import Team


class Person:
    def __init__(self, id: int, username: str, discord_handler: str, team: Team = None):
        self._id = id
        self._username = username
        self._discord_handler = discord_handler
        self._team = team
