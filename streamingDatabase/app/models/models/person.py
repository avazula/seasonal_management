class Person:
    def __init__(self, id: int, username: str, discord_handler: str):
        self._id = id
        self._username = username
        self._discord_handler = discord_handler

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def discord_handler(self) -> str:
        return self._discord_handler

    @discord_handler.setter
    def discord_handler(self, value: str) -> None:
        self._discord_handler = value
