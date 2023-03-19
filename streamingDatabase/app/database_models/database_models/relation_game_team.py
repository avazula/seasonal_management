from enum import Enum


class GameTeamDB(Enum):
    TABLE = "sd_relation_game_team"  # str
    ID = "id" # str
    GAME = "game"  # int
    TEAM = "team"  # int
