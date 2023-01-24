from arrow import arrow


class Game:
    def __init__(self, id: int, date: arrow = None, time: arrow = None):
        self._id = id
        self._date = date
        self._time = time
