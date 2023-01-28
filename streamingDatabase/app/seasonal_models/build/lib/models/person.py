from .team import Team


class Person:
    def __init__(self, id: int, username: str, discord_handler: str, team: Team = None):
        self._id = id
        self._username = username
        self._discord_handler = discord_handler
        self._team = team

    @property
    def id(self) -> int:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def discord_handler(self) -> str:
        return self._discord_handler

    @property
    def team(self) -> Team:
        return self._team

    @team.setter
    def team(self, team: Team) -> None:
        self._team = team
