import sqlite3
from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls, db_path=":memory:"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance._init(db_path)
        return cls._instance

    def _init(self, db_path, check_same_thread=False):
        self.connection = sqlite3.connect(db_path, check_same_thread)
        self.cursor = self.connection.cursor()

    def create(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()
        return self.cursor.lastrowid

    def read(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def update(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()
        return self.cursor.rowcount

    def delete(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()
        return self.cursor.rowcount

    def close(self):
        self.connection.close()
        Database._instance = None

