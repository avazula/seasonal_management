import arrow
from typing import List, Optional
from models.game import Game


class GameFactory():

    @staticmethod
    def sanitize(id: int, datetime: arrow.arrow.Arrow = None) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if id is not None:
            if not isinstance(id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if datetime is not None:
            if not isinstance(datetime, arrow.arrow.Arrow):
                invalid_parameters.append("datetime")
                raise Exception("datetime must be of type arrow")
            elif datetime.year < 2022 or datetime.year > 2030:
                invalid_parameters.append("datetime")
                raise Exception("datetime must be more recent than January 1st, 2022 and less than January 1st, 2030")
        return invalid_parameters if invalid_parameters else None

    @staticmethod
    def create(id: int, datetime: arrow.arrow.Arrow = None) -> Game:
        try:
            GameFactory.sanitize(id, datetime)
        except:
            raise
        return Game(id=id, datetime=datetime)