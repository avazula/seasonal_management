from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.team import TeamDB
from models.team import Team


class TeamCRUD(DatabaseConnection):
    def create_team_returning_object(self, short_name: str, full_name: str) -> Optional[Team]:
        query = sql.SQL(
            """
                INSERT INTO {team}
                ({columns}) VALUES ({values})
                RETURNING *;
            """
        ).format(
            team=sql.Identifier(TeamDB.TABLE.value),
            columns=sql.SQL(",").join(map(sql.Identifier, [TeamDB.SHORT.value, TeamDB.FULL.value])),
            values=sql.SQL(",").join(map(sql.Literal, [short_name, full_name])),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Team(id=res[0], short_name=res[1], full_name=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_team_returning_object(self, team: Team) -> Optional[Team]:
        query = sql.SQL(
            """
                UPDATE {team}
                SET {short_id}={short_value},
                {full_id}={full_value}
                WHERE {id}={value}
                RETURNING *;
            """
        ).format(
            team=sql.Identifier(TeamDB.TABLE.value),
            short_id=sql.Identifier(TeamDB.SHORT.value),
            short_value=sql.Literal(team.short_name),
            full_id=sql.Identifier(TeamDB.FULL.value),
            full_value=sql.Literal(team.full_name),
            id=sql.Identifier(TeamDB.ID.value),
            value=sql.Literal(team.id),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Team(id=res[0], short_name=res[1], full_name=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def delete_team_by_id_returning_object(self, id: int) -> Optional[Team]:
        query = sql.SQL(
            """
                DELETE FROM {team}
                WHERE {id}={value}
                RETURNING *;
            """
        ).format(team=sql.Identifier(TeamDB.TABLE.value), id=sql.Identifier(TeamDB.ID.value), value=sql.Literal(id))
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Team(id=res[0], short_name=res[1], full_name=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_team_by_id(self, id: int) -> Optional[Team]:
        query = sql.SQL(
            """
                SELECT * FROM {team}
                WHERE {id}={value};
            """
        ).format(team=sql.Identifier(TeamDB.TABLE.value), id=sql.Identifier(TeamDB.ID.value), value=sql.Literal(id))
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            if res:
                return Team(id=res[0], short_name=res[1], full_name=res[2])
        except:
            raise
        finally:
            self.cur.close()

    def get_all_teams(self) -> List[Team]:
        query = sql.SQL(
            """
                SELECT * FROM {team};
            """
        ).format(team=sql.Identifier(TeamDB.TABLE.value))
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return [Team(id=row[0], short_name=row[1], full_name=row[2]) for row in rows]
        except:
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     tc = TeamCRUD()
#     team = tc.update_team_returning_object(Team(id=2, short_name='blblbl', full_name='wheeeeeeeeeeeee'))
#     print("Team: {}")
#     print(team.id, team.short_name, team.full_name)
#     tc = TeamCRUD()
#     team = tc.delete_team_by_id_returning_object(id=1)
#     print("Deleted team: {}")
#     print(team.id, team.short_name, team.full_name)
#     tc = TeamCRUD()
#     team = tc.get_team_by_id(id=2)
#     print("Team: {}")
#     print(team.id, team.short_name, team.full_name)
#     tc = TeamCRUD()
#     teams = tc.get_all_teams()
#     print("Teams length: {}", len(teams))
