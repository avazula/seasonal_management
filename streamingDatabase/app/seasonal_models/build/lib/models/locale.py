class Locale:
    def __init__(self, id: int, time: str, abbreviation: str = None):
        self._id = id
        self._time = time
        self._abbreviation = abbreviation
