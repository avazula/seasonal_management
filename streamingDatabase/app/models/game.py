import arrow
from typing import List
from .map import Map
from .streamer import Streamer
from .team import Team


class Game:
    def __init__(
        self, id: int, datetime: arrow, teamA: Team = None, teamB: Team = None, streamers: List[Streamer] = None, map: Map = None
    ):
        self._id = id
        self._datetime = datetime
        self._teamA = teamA
        self._teamB = teamB
        self._streamers = streamers
        self._map = map

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def datetime(self) -> arrow:
        return self._datetime

    @datetime.setter
    def datetime(self, value: arrow) -> None:
        self._datetime = value

    @property
    def teamA(self) -> Team:
        return self._teamA

    @teamA.setter
    def teamA(self, value: Team) -> None:
        self._teamA = value

    @property
    def teamB(self) -> Team:
        return self._teamB

    @teamB.setter
    def teamB(self, value: Team) -> None:
        self._teamB = value

    @property
    def streamers(self) -> List[Streamer]:
        return self._streamers

    @streamers.setter
    def streamers(self, value: List[Streamer]) -> None:
        self._streamers = value

    @property
    def map(self) -> Map:
        return self._map

    @map.setter
    def map(self, value: Map) -> None:
        self._map = value
