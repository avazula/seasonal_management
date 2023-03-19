from enum import Enum


class TeamPersonDB(Enum):
    TABLE = "sd_relation_team_person"  # str
    ID = "id" # str
    USER = "user"  # int
    TEAM = "team"  # int
    END = "end_date"  # datetime
