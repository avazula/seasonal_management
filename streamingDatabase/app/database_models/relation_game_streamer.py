from enum import Enum


class GameStreamerDB(Enum):
    TABLE = "relation_game_streamer"  # str
    GAME = "game"  # int
    USER = "user"  # int
