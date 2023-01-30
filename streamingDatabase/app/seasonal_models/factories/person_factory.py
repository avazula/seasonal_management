from models.person import Person
from models.team import Team
from typing import Optional, List


class PersonFactory:
    @staticmethod
    def sanitize(id: int, username: str, discord_handler: str, team: Team = None) -> Optional[Person]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if username is not None:
            if not isinstance(username, str):
                invalid_parameters.append("username")
                raise Exception("username must be of type str")
            elif len(username) < 4 or len(username) > 80:
                invalid_parameters.append("username")
                raise Exception("time must be of length 4 < x < 80")
        if discord_handler is not None:
            if not isinstance(discord_handler, str):
                invalid_parameters.append("discord_handler")
                raise Exception("discord_handler must be of type str")
            elif len(discord_handler) < 7 or len(discord_handler) > 120:
                invalid_parameters.append("discord_handler")
                raise Exception("time must be of length 7 < x < 120")
        if team is not None:
            if not isinstance(team, Team):
                invalid_parameters.append("team")
                raise Exception("team must be of type Team")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id: int, username: str, discord_handler: str, team: Team = None) -> Optional[List[str]]:
        try:
            PersonFactory.sanitize(id, username, discord_handler, team)
        except:
            raise
        return Person(id=id, username=username, discord_handler=discord_handler, team=team)
