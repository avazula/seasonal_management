from psycopg2 import sql
from typing import List, Optional
from connection import DatabaseConnection
from database_models.person import PersonDB
from models.person import Person


class PersonCRUD(DatabaseConnection):
    def create_person_returning_object(self, username: str, discord_handler: str) -> Optional[Person]:
        query = sql.SQL(
            """
            INSERT INTO {person} ({columns})
            VALUES ({values})
            RETURNING *;
            """
        ).format(
            person=sql.Identifier(PersonDB.TABLE.value),
            columns=sql.SQL(",").join(map(sql.Identifier, [PersonDB.USERNAME.value, PersonDB.DISCORD.value])),
            values=sql.SQL(",").join(map(sql.Literal, [username, discord_handler])),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Person(id=res[0], username=res[1], discord_handler=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def update_person_returning_object(self, id: int, username: str, discord_handler: str) -> Optional[Person]:
        query = sql.SQL(
            """
            UPDATE {person} 
            SET {username}={username_value}, {discord}={discord_handler}
            WHERE {id}={id_value}
            RETURNING *;
            """
        ).format(
            person=sql.Identifier(PersonDB.TABLE.value),
            username=sql.Identifier(PersonDB.USERNAME.value),
            username_value=sql.Literal(username),
            discord=sql.Identifier(PersonDB.DISCORD.value),
            discord_handler=sql.Literal(discord_handler),
            id=sql.Identifier(PersonDB.ID.value),
            id_value=sql.Literal(id),
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Person(id=res[0], username=res[1], discord_handler=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def delete_person_by_id_returning_object(self, id: int) -> Optional[Person]:
        query = sql.SQL(
            """
            DELETE FROM {person}
            WHERE {id}={value}
            RETURNING *;
            """
        ).format(
            person=sql.Identifier(PersonDB.TABLE.value), id=sql.Identifier(PersonDB.ID.value), value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Person(id=res[0], username=res[1], discord_handler=res[2])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_person_by_id(self, id: int) -> Optional[Person]:
        query = sql.SQL(
            """
                SELECT * FROM {person}
                WHERE {id}={value}; 
            """
        ).format(
            person=sql.Identifier(PersonDB.TABLE.value), id=sql.Identifier(PersonDB.ID.value), value=sql.Literal(id)
        )
        try:
            self.cur.execute(query)
            res = self.cur.fetchone()
            self.conn.commit()
            if res:
                return Person(id=res[0], datetime=res[1])
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()

    def get_all_people(self) -> List[Person]:
        query = sql.SQL(
            """
                SELECT * FROM {person}; 
            """
        ).format(person=sql.Identifier(PersonDB.TABLE.value))
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.conn.commit()
            return [Person(id=row[0], datetime=rows[1]) for row in rows]
        except:
            self.conn.rollback()
            raise
        finally:
            self.cur.close()


# if __name__ == "__main__":
#     pc = PersonCRUD()
#     person = pc.create_person_returning_object(username="Jain", discord_handler="avazula#2077")
#     print("Person: {}")
#     print(person.username, person.discord_handler)
#     pc = PersonCRUD()
#     updated_person = pc.update_person_returning_object(id=8, username='Jainou', discord_handler='avazula#2078')
#     print("Person: {}")
#     print(updated_person.username, updated_person.discord_handler)
#     pc = PersonCRUD()
#     deleted_person = pc.delete_person_by_id_returning_object(id=8)
#     print("Person: {}")
#     print(updated_person.username, updated_person.discord_handler)
