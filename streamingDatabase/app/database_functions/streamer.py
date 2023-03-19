from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.person import PersonDB
from database_models.streamer import StreamerDB
from models.streamer import Streamer


class StreamerCRUD(DatabaseConnection):
    def create_streamer(self, twitch_handler: str, youtube_handler: str, bilibili_handler: str, user_id: int) -> None:
        query = sql.SQL(
            """
            INSERT INTO {streamer} ({columns})
            VALUES ({values});
            """
        ).format(
            streamer=sql.Identifier(StreamerDB.TABLE.value),
            columns=sql.SQL(",").join(
                map(
                    sql.Identifier,
                    [
                        StreamerDB.TWITCH.value,
                        StreamerDB.YOUTUBE.value,
                        StreamerDB.BILIBILI.value,
                        StreamerDB.USER.value,
                    ],
                )
            ),
            values=sql.SQL(",").join(map(sql.Literal, [twitch_handler, youtube_handler, bilibili_handler, user_id])),
        )
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_streamer(self, twitch_handler: str, youtube_handler: str, bilibili_handler: str, user_id: int) -> None:
        query = sql.SQL(
            """
            UPDATE {streamer}
            SET {twitch}={twitch_value},
            {youtube}={youtube_value},
            {bilibili}={bilibili_value}
            WHERE {user}={user_value};
            """
        ).format(
            streamer=sql.Identifier(StreamerDB.TABLE.value),
            twitch=sql.Identifier(StreamerDB.TWITCH.value),
            twitch_value=sql.Literal(twitch_handler),
            youtube=sql.Identifier(StreamerDB.YOUTUBE.value),
            youtube_value=sql.Literal(youtube_handler),
            bilibili=sql.Identifier(StreamerDB.BILIBILI.value),
            bilibili_value=sql.Literal(bilibili_handler),
            user=sql.Identifier(StreamerDB.USER.value),
            user_value=sql.Literal(user_id),
        )
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def delete_streamer_by_id(self, id: int) -> None:
        query = sql.SQL(
            """
            DELETE FROM {streamer}
            WHERE {user}={value};
            """
        ).format(
            streamer=sql.Identifier(StreamerDB.TABLE.value),
            user=sql.Identifier(StreamerDB.USER.value),
            value=sql.Literal(id),
        )
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_all_streamers(self) -> List[Streamer]:
        query = sql.SQL(
            """
            SELECT p.{p_columns}, s.{s_columns} FROM {person} p INNER JOIN {streamer} s
            ON p.{p_id}=s.{s_id};
            """
        ).format(
            p_columns=sql.SQL(",").join(
                map(
                    sql.Identifier,
                    [
                        PersonDB.ID.value,
                        PersonDB.USERNAME.value,
                        PersonDB.DISCORD.value,
                    ],
                )
            ),
            s_columns=sql.SQL(",").join(
                map(sql.Identifier, [StreamerDB.TWITCH.value, StreamerDB.YOUTUBE.value, StreamerDB.BILIBILI.value])
            ),
            person=sql.Identifier(PersonDB.TABLE.value),
            streamer=sql.Identifier(StreamerDB.TABLE.value),
            p_id=sql.Identifier(PersonDB.ID.value),
            s_id=sql.Identifier(StreamerDB.USER.value),
        )
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return [
                Streamer(
                    id=row[0],
                    username=row[1],
                    discord_handler=row[2],
                    twitch_handler=row[3],
                    youtube_handler=row[4],
                    bilibili_handler=row[5],
                )
                for row in rows
            ]
        except:
            raise
        finally:
            self.cur.close()

    def get_streamer_by_user_id(self, user_id: int) -> Optional[Streamer]:
        query = sql.SQL(
            """
            SELECT p.{p_columns}, s.{s_columns} FROM {person} p INNER JOIN {streamer} s
            ON p.{p_id}=s.{s_id}
            WHERE s.{s_id}={user_id};
            """
        ).format(
            p_columns=sql.SQL(",").join(
                map(
                    sql.Identifier,
                    [
                        PersonDB.ID.value,
                        PersonDB.USERNAME.value,
                        PersonDB.DISCORD.value,
                    ],
                )
            ),
            s_columns=sql.SQL(",").join(
                map(sql.Identifier, [StreamerDB.TWITCH.value, StreamerDB.YOUTUBE.value, StreamerDB.BILIBILI.value])
            ),
            person=sql.Identifier(PersonDB.TABLE.value),
            streamer=sql.Identifier(StreamerDB.TABLE.value),
            p_id=sql.Identifier(PersonDB.ID.value),
            s_id=sql.Identifier(StreamerDB.USER.value),
            user_id=sql.Literal(user_id),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            if res:
                return Streamer(
                    id=res[0],
                    username=res[1],
                    discord_handler=res[2],
                    twitch_handler=res[3],
                    youtube_handler=res[4],
                    bilibili_handler=res[5],
                )
        except:
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     sc = StreamerCRUD()
#     sc.create_streamer(twitch_handler='ava', bilibili_handler='avazjain', youtube_handler='Lakshakodee', user_id=9)
#     sc = StreamerCRUD()
#     streamer = sc.get_streamer_by_user_id(user_id=9)
#     print(streamer.id, streamer.discord_handler, streamer.username, streamer.twitch_handler, streamer.youtube_handler, streamer.bilibili_handler)
#     sc = StreamerCRUD()
#     sc.update_streamer(user_id=9, youtube_handler='avaz', bilibili_handler='avaz', twitch_handler='avaz')
#     sc = StreamerCRUD()
#     streamer = sc.get_streamer_by_user_id(user_id=9)
#     print(streamer.id, streamer.discord_handler, streamer.username, streamer.twitch_handler, streamer.youtube_handler, streamer.bilibili_handler)
#     sc = StreamerCRUD()
#     sc.delete_streamer_by_id(id=9)
#     sc = StreamerCRUD()
#     streamers = sc.get_all_streamers()
#     print(len(streamers))
