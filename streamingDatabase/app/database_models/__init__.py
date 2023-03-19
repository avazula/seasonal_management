from .game import GameDB
from .language import LanguageDB
from .locale import LocaleDB
from .map import MapDB
from .person import PersonDB
from .relation_game_map import GameMapDB
from .relation_game_stage import GameStageDB
from .relation_game_streamer import GameStreamerDB
from .relation_game_team import GameTeamDB
from .relation_language_streamer import LanguageStreamerDB
from .relation_team_person import TeamPersonDB
from .stage import StageDB
from .streamer import StreamerDB
from .team import TeamDB

__all__ = [
    GameDB,
    LanguageDB,
    LocaleDB,
    MapDB,
    PersonDB,
    GameMapDB,
    GameStageDB,
    GameStreamerDB,
    GameTeamDB,
    LanguageStreamerDB,
    TeamPersonDB,
    StageDB,
    StreamerDB,
    TeamDB,
]
