from .person import Person
from .team import Team
from .language import Language
from typing import List


class Streamer(Person):
    def __init__(
        self,
        id: int,
        username: str,
        discord_handler: str,
        twitch_handler: str = None,
        youtube_handler: str = None,
        bilibili_handler: str = None,
        team: Team = None,
        languages: List[Language] = None,
    ):
        self._id = id
        self._username = username
        self._discord_handler = discord_handler
        self._youtube_handler = youtube_handler
        self._twitch_handler = twitch_handler
        self._bilibili_handler = bilibili_handler
        self._team = team
        self._languages = languages
