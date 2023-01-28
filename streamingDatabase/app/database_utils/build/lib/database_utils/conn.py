import environ
import psycopg2 as pg


env = environ.Env()
environ.Env.read_env()

conn = pg.connect(host=env("DB_HOST"), user=env("DB_USER"), password=env("DB_PASSWORD"), dbname=env("DB_NAME"))

class Connection:
    def __init__(self):
        self._conn = conn
        self._cur = conn.cursor()
    
    @property
    def conn(self):
        return self._conn

    @property
    def cur(self):
        return self._cur
