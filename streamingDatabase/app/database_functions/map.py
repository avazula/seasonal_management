from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.map import MapDB
from models.map import Map


class MapCRUD(DatabaseConnection):
    def create_map_returning_object(self, full_name: str, game_mode: str, short_name: str) -> Optional[Map]:
        query = sql.SQL(
            '''
                INSERT INTO {map}
                ({columns}) VALUES ({values})
                RETURNING *;
            '''
        ).format(
            map=sql.Identifier(MapDB.TABLE.value),
            columns=sql.SQL(',').join(map(sql.Identifier, [
                MapDB.FULL.value,
                MapDB.MODE.value,
                MapDB.SHORT.value
            ])),
            values=sql.SQL(',').join(map(sql.Literal, [
                full_name,
                game_mode,
                short_name
            ]))
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Map(id=res[0], short_name=res[1], full_name=res[2], game_mode=res[3])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_map_returning_object(self, map: Map) -> Optional[Map]:
        query = sql.SQL(
            '''
                UPDATE {map}
                SET {short}={short_name},
                {full}={full_name},
                {game_mode}={game_mode_value}
                WHERE {id}={value}
                RETURNING *;
            '''
        ).format(
            map=sql.Identifier(MapDB.TABLE.value),
            short=sql.Identifier(MapDB.SHORT.value),
            short_name=sql.Literal(map.short_name),
            game_mode=sql.Identifier(MapDB.MODE.value),
            game_mode_value=sql.Literal(map.game_mode),
            full=sql.Identifier(MapDB.FULL.value),
            full_name=sql.Literal(map.full_name),
            id=sql.Identifier(MapDB.ID.value),
            value=sql.Literal(map.id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Map(id=res[0], short_name=res[1], full_name=res[2], game_mode=res[3])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()
    
    def delete_map_by_id_returning_object(self, id: int) -> Optional[Map]:
        query = sql.SQL(
            '''
            DELETE FROM {map}
            WHERE {id}={value}
            RETURNING *;
            '''
        ).format(
            map=sql.Identifier(MapDB.TABLE.value),
            id=sql.Identifier(MapDB.ID.value),
            value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Map(id=res[0], short_name=res[1], full_name=res[2], game_mode=res[3])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()
    
    def get_map_by_id(self, id: int) -> Optional[Map]:
        query = sql.SQL(
            '''
            SELECT * FROM {map}
            WHERE {id}={value};
            '''
        ).format(
            map=sql.Identifier(MapDB.TABLE.value),
            id=sql.Identifier(MapDB.ID.value),
            value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            if res:
                return Map(id=res[0], short_name=res[1], full_name=res[2], game_mode=res[3])
        except:
            raise
        finally:
            self.cur.close()
    
    def get_all_maps(self) -> List[Map]:
        query = sql.SQL(
            '''
            SELECT * FROM {map};
            '''
        ).format(
            map=sql.Identifier(MapDB.TABLE.value)
        )
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return [
                Map(
                    id=row[0],
                    short_name=row[1],
                    full_name=row[2],
                    game_mode=row[3]
                ) for row in rows
            ]
        except:
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     mc = MapCRUD()
#     map = mc.create_map_returning_object(short_name='SMDM', full_name='Sainte-Marie Du Mont', game_mode='Warfare')
#     print("Map: {}")
#     print(map.id, map.short_name, map.full_name, map.game_mode)
#     mc = MapCRUD()
#     map = mc.update_map_returning_object(Map(id=1, short_name='SMDM', full_name='Sainte-Marie Du Mont', game_mode='Offensive'))
#     print("Map: {}")
#     print(map.id, map.short_name, map.full_name, map.game_mode)
#     mc = MapCRUD()
#     map = mc.get_map_by_id(id=1)
#     print("Map: {}")
#     print(map.id, map.short_name, map.full_name, map.game_mode)
#     mc = MapCRUD()
#     maps = mc.get_all_maps()
#     print("Maps length: {}", len(maps))
#     mc = MapCRUD()
#     map = mc.delete_map_by_id_returning_object(id=1)
#     print("Deleted map: {}")
#     print(map.id, map.short_name, map.full_name, map.game_mode)
#     mc = MapCRUD()
#     maps = mc.get_all_maps()
#     print("Maps length: {}", len(maps))
