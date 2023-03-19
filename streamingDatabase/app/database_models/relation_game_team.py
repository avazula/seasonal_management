from enum import Enum


class GameTeamDB(Enum):
    TABLE = "relation_game_team"  # str
    GAME = "game"  # int
    TEAM = "team"  # int
