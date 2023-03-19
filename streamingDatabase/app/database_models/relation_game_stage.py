from enum import Enum


class GameStageDB(Enum):
    TABLE = "relation_game_stage"  # str
    GAME = "game"  # int
    STAGE = "stage"  # int
