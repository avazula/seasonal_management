from enum import Enum


class TeamPersonDB(Enum):
    TABLE = "relation_team_person"  # str
    USER = "user"  # int
    TEAM = "team"  # int
    END = "end_date"  # datetime
