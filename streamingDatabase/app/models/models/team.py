class Team:
    def __init__(self, id: int, short_name: str, full_name: str = None):
        self._id = id
        self._short_name = short_name
        self._full_name = full_name

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def short_name(self) -> str:
        return self._short_name

    @short_name.setter
    def short_name(self, value: str) -> None:
        self._short_name = value

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        self._full_name = value
