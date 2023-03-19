from enum import Enum


class StreamerDB(Enum):
    TABLE = "sd_streamer"  # str
    ID = "id" # str
    USER = "user_id"  # int
    TWITCH = "twitch_handler"  # str
    YOUTUBE = "youtube_handler"  # str
    BILIBILI = "bilibili_handler"  # str
