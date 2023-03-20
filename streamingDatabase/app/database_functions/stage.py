from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.stage import StageDB
from models.stage import Stage


class StageCRUD(DatabaseConnection):
    def create_stage_returning_object(self, name: str) -> Optional[Stage]:
        query = sql.SQL(
            """
                INSERT INTO {stage}
                ({columns}) VALUES ({values})
                RETURNING *;
            """
        ).format(
            stage=sql.Identifier(StageDB.TABLE.value),
            columns=sql.SQL(",").join(map(sql.Identifier, [StageDB.NAME.value])),
            values=sql.SQL(",").join(map(sql.Literal, [name])),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Stage(id=res[0], name=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_stage_returning_object(self, stage: Stage) -> Optional[Stage]:
        query = sql.SQL(
            """
                UPDATE {stage}
                SET {name}={name_value}
                WHERE {id}={id_value}
                RETURNING *;
            """
        ).format(
            stage=sql.Identifier(StageDB.TABLE.value),
            name=sql.Identifier(StageDB.NAME.value),
            name_value=sql.Literal(stage.name),
            id=sql.Identifier(StageDB.ID.value),
            id_value=sql.Literal(stage.id),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Stage(id=res[0], name=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def delete_stage_by_id_returning_object(self, id: int) -> Optional[Stage]:
        query = sql.SQL(
            """
                DELETE FROM {stage}
                WHERE {id}={id_value}
                RETURNING *;
            """
        ).format(
            stage=sql.Identifier(StageDB.TABLE.value), id=sql.Identifier(StageDB.ID.value), id_value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Stage(id=res[0], name=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_stage_by_id(self, id: int) -> Optional[Stage]:
        query = sql.SQL(
            """
                SELECT * FROM {stage}
                WHERE {id}={id_value};
            """
        ).format(
            stage=sql.Identifier(StageDB.TABLE.value), id=sql.Identifier(StageDB.ID.value), id_value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            if res:
                return Stage(id=res[0], name=res[1])
        except:
            raise
        finally:
            self.cur.close()

    def get_all_stages(self) -> List[Stage]:
        query = sql.SQL(
            """
                SELECT * FROM {stage};
            """
        ).format(stage=sql.Identifier(StageDB.TABLE.value))
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return [Stage(id=row[0], name=row[1]) for row in rows]
        except:
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     sc = StageCRUD()
#     stage = sc.create_stage_returning_object(name='blblbl')
#     print("Stage: {}")
#     print(stage.id, stage.name)
#     sc = StageCRUD()
#     stage = sc.update_stage_returning_object(Stage(id=3, name='playoffs'))
#     print("Stage: {}")
#     print(stage.id, stage.name)
#     sc = StageCRUD()
#     stage = sc.get_stage_by_id(id=3)
#     print("Stage: {}")
#     print(stage.id, stage.name)
#     sc = StageCRUD()
#     stages = sc.get_all_stages()
#     print("Stages length: {}", len(stages))
#     sc = StageCRUD()
#     stage = sc.delete_stage_by_id_returning_object(id=3)
#     print("Deleted stage: {}")
#     print(stage.id, stage.name)
#     sc = StageCRUD()
#     stages = sc.get_all_stages()
#     print("Stages length: {}", len(stages))
