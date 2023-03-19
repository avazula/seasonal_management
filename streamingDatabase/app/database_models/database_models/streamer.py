from enum import Enum


class StreamerDB(Enum):
    TABLE = "sd_streamer"  # str
    ID = "id" # str
    USER = "user"  # int
    TWITCH = "twitch_handler"  # str
    YOUTUBE = "youtube_handler"  # str
    BILIBILI = "bilibili_handler"  # str
