from .person import Person
from .team import Team
from .language import Language
from typing import List, Optional


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
        Person.__init__(id=id, username=username, discord_handler=discord_handler, team=team)
        self._youtube_handler = youtube_handler
        self._twitch_handler = twitch_handler
        self._bilibili_handler = bilibili_handler
        self._languages = languages

    @property
    def youtube_handler(self) -> str:
        return self._youtube_handler

    @property
    def twitch_handler(self) -> Optional[str]:
        return self._twitch_handler

    @property
    def bilibili_handler(self) -> Optional[str]:
        return self._bilibili_handler

    @property
    def languages(self) -> List[Language]:
        return self._languages

    @languages.setter
    def languages(self, languages: List[Language]) -> None:
        self._languages = languages
