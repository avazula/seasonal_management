from enum import Enum


class GameStreamerDB(Enum):
    TABLE = "sd_relation_game_streamer"  # str
    ID = "id" # str
    GAME = "game"  # int
    USER = "user"  # int
