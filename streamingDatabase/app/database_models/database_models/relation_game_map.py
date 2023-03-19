from enum import Enum


class GameMapDB(Enum):
    TABLE = "sd_relation_game_map"  # str
    ID = "id" # str
    MAP = "map"  # int
    GAME = "game"  # int
