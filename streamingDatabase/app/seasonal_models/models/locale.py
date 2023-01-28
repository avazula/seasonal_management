class Locale:
    def __init__(self, id: int, time: str, abbreviation: str = None):
        self._id = id
        self._time = time
        self._abbreviation = abbreviation

    @property
    def id(self) -> int:
        return self._id

    @property
    def time(self) -> str:
        return self._time

    @property
    def abbreviation(self) -> str:
        return self._abbreviation
