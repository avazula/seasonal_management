from enum import Enum


class GameStageDB(Enum):
    TABLE = "sd_relation_game_stage"  # str
    ID = "id" # str
    GAME = "game"  # int
    STAGE = "stage"  # int
