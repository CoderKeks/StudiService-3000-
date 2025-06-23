import Kurs, Database, pathlib

if __name__ == "__main__":
    kurs1 = Kurs.Kurs("Deutsch", "Herr Ruhl", 1)
    db = Database.Database(pathlib.Path("test.db"))
    cur  = db.connection.cursor()

    print(db.read("SELECT * FROM kurs"))
