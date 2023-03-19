from .person import Person


class Streamer(Person):
    def __init__(
        self,
        id: int,
        username: str,
        discord_handler: str,
        youtube_handler: str,
        twitch_handler: str = None,
        bilibili_handler: str = None,
    ):
        Person.__init__(self, id=id, username=username, discord_handler=discord_handler)
        self._youtube_handler = youtube_handler
        self._twitch_handler = twitch_handler
        self._bilibili_handler = bilibili_handler

    @property
    def youtube_handler(self) -> str:
        return self._youtube_handler

    @youtube_handler.setter
    def youtube_handler(self, value: str) -> None:
        self._youtube_handler = value

    @property
    def twitch_handler(self) -> str:
        return self._twitch_handler

    @twitch_handler.setter
    def twitch_handler(self, value: str) -> None:
        self._youtube_handler = value

    @property
    def bilibili_handler(self) -> str:
        return self._bilibili_handler

    @bilibili_handler.setter
    def bilibili_handler(self, value: str) -> None:
        self._bilibili_handler = value
