from arrow import arrow


class Game:
    def __init__(self, id: int, datetime: arrow = None):
        self._id = id
        self._datetime = datetime

    @property
    def id(self):
        return self._id

    @property
    def datetime(self):
        return self._datetime

    def create_game(self):
        pass
