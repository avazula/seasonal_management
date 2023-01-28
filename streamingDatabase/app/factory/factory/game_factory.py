import arrow
from typing import List, Optional
from models.game import Game


class GameFactory:
    def __init__(self, id: int = None, datetime: arrow = None) -> Game:
        game = Game(
            id=id,
            datetime=datetime,
        )
        self.sanitize(game)
        return game

    def sanitize(game: Game) -> Optional[List[str]]:
        invalid_parameters: List[str] = []
        if game.id is not None:
            if not isinstance(game.id, int):
                invalid_parameters.append("id")
                raise Exception("id must be an integer")
            elif game.id < 1:
                invalid_parameters.append("id")
                raise Exception("id must be greater than 0")
        if game.datetime is not None:
            if not isinstance(game.datetime, arrow):
                invalid_parameters.append("datetime")
                raise Exception("datetime must be of type arrow")
            elif game.datetime.year < 2022 or game.datetime.year > 2030:
                invalid_parameters.append("datetime")
                raise Exception("datetime must be more recent than January 1st, 2022 and less than January 1st, 2030")
        return invalid_parameters if invalid_parameters else None
