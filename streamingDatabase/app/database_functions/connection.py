import psycopg2 as pg
from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1} file".format(section, filename))
    return db


class DatabaseConnection:
    def __init__(self):
        self.conn = None
        try:
            params = config()
            self.conn = pg.connect(**params)
            self.cur = self.conn.cursor()
            print("OK")
        except (Exception, pg.DatabaseError):
            raise
