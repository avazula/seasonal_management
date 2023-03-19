from enum import Enum


class MapDB(Enum):
    TABLE = "sd_map"  # str
    ID = "id" # str
    SHORT = "short_name"  # str
    FULL = "full_name"  # str
    MODE = "game_mode"  # str
