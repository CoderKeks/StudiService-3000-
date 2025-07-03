from Database import Database
from Models.Studierender import Studierender

class StudierendeService:
    def __init__(self):
        self.db = Database("./database.db")

    def create(self, studierender: Studierender):
        return self.db.create("""
            INSERT INTO studierende (
                name,
                matrikelnummer,
                studiengang
            ) VALUES (?, ?, ?);
        """, (studierender.name, studierender.matrikelnummer, studierender.studiengang))

    def update(self, studierendeId: int, studierender: Studierender):
        return self.db.update("""
            UPDATE studierende SET
                name = ?,
                matrikelnummer = ?,
                studiengang = ?
            WHERE id = ?;
        """, (studierender.name, studierender.matrikelnummer, studierender.studiengang, int(studierendeId)))

    def delete(self, studierendeId: int):
        return self.db.delete("DELETE FROM studierende WHERE id = ?", (str(studierendeId),))

    def get_one(self, studierendeId: int):
        row = self.db.read("SELECT * FROM studierende WHERE id = ?", (str(studierendeId),))
        return Studierender(*row[0]) if row else None

    def get_all(self):
        rows = self.db.read("SELECT * FROM studierende")
        return [Studierender(*row) for row in rows]

    def add_to_kurs(self, studierendeId, kursId):
        return self.db.create(
            "INSERT INTO teilnahme (studierendeId, kursId) VALUES (?, ?);",
            (int(studierendeId), int(kursId))
        )
