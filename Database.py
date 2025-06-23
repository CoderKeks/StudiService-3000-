import sqlite3
from threading import Lock

class Database:
    _instance = None
    _instance_lock = Lock()

    def __new__(cls, db_path: str):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance._init(db_path)
        return cls._instance

    def _init(self, db_path, check_same_thread=False):
        self.connection = sqlite3.connect(db_path, check_same_thread)
        self.cursor = self.connection.cursor()
        self._db_lock = Lock()
        self.initialize_schema()

    def initialize_schema(self):
        with self._db_lock:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS kurse (
                    kurs_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kursname TEXT NOT NULL UNIQUE,
                    dozent TEXT,
                    semester INTEGER
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS studenten (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    matrikelnummer TEXT NOT NULL UNIQUE
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS anmeldungen (
                    anmeldung_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    kurs_id INTEGER,
                    FOREIGN KEY(student_id) REFERENCES studenten(student_id),
                    FOREIGN KEY(kurs_id) REFERENCES kurse(kurs_id)
                )
            """)
            self.connection.commit()

    def create(self, query, params=None):
        with self._db_lock:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.lastrowid

    def read(self, query, params=None):
        with self._db_lock:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()

    def update(self, query, params=None):
        with self._db_lock:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.rowcount

    def delete(self, query, params=None):
        with self._db_lock:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.rowcount

    def close(self):
        with self._db_lock:
            self.connection.close()
            Database._instance = None

