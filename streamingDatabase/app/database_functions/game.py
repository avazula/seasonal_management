import arrow
import psycopg2 as pg
from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.game import GameDB
from models.game import Game


class GameCRUD(DatabaseConnection):
    def create_game_returning_object(self, datetime: arrow) -> Optional[Game]:
        query = sql.SQL(
            """
                INSERT INTO {game} ({columns})
                VALUES ({values})
                RETURNING *; 
            """
        ).format(
            game=sql.Identifier(GameDB.TABLE.value),
            columns=sql.SQL(", ").join(map(sql.Identifier, [GameDB.DATE.value])),
            values=sql.Literal(datetime),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Game(id=res[0], datetime=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_game_returning_object(self, id: int, datetime: arrow) -> Optional[Game]:
        query = sql.SQL(
            """
            UPDATE {game}
            SET {datetime}={datetime_value}
            WHERE {id}={id_value}
            RETURNING *;
            """
        ).format(
            game=sql.Identifier(GameDB.TABLE.value),
            datetime=sql.Identifier(GameDB.DATE.value),
            datetime_value=sql.Literal(datetime),
            id=sql.Identifier(GameDB.ID.value),
            id_value=sql.Literal(id),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Game(id=res[0], datetime=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def delete_game_by_id_returning_object(self, id: int) -> Optional[Game]:
        query = sql.SQL(
            """
                DELETE FROM {game}
                WHERE {id}={value}
                RETURNING *; 
            """
        ).format(game=sql.Identifier(GameDB.TABLE.value), id=sql.Identifier(GameDB.ID.value), value=sql.Literal(id))
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Game(id=res[0], datetime=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_game_by_id(self, id: int) -> Optional[Game]:
        query = sql.SQL(
            """
                SELECT * FROM {game}
                WHERE {id}={value}; 
            """
        ).format(game=sql.Identifier(GameDB.TABLE.value), id=sql.Identifier(GameDB.ID.value), value=sql.Literal(id))
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Game(id=res[0], datetime=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_all_games(self) -> Optional[List[Game]]:
        query = sql.SQL(
            """
                SELECT * FROM {game}; 
            """
        ).format(game=sql.Identifier(GameDB.TABLE.value))
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.conn.commit()
            return [Game(id=row[0], datetime=rows[1]) for row in rows]
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     gc = GameCRUD()
#     g1 = gc.create_game_returning_object(arrow.get().datetime)
#     gc = GameCRUD()
#     g2 =     gc.create_game_returning_object(arrow.get().datetime)
#     gc = GameCRUD()
#     g3 =     gc.create_game_returning_object(arrow.get().datetime)
#     gc = GameCRUD()
#     games = gc.get_all_games()
#     print("Games: {}", len(games))
#     gc = GameCRUD()
#     deleted_game = gc.delete_game_by_id_returning_object(id=10)
#     print(deleted_game.id)
#     print(deleted_game.datetime)
#     gc = GameCRUD()
#     games = gc.get_all_games()
#     print("Games: {}", len(games))
