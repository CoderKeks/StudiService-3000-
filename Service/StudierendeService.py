from Database import Database
from Models.Studierender import Studierender
from Models.Kurs import Kurs

class StudierendeService:
    def __init__(self):
         self.db = Database("./database.db")

    def create(self, studierender: Studierender):
        print(studierender)
        return self.db.create(f"""
                        INSERT INTO studierende (
                            name,
                            matrikelnummer,
                            studiengang
                        )
                        VALUES 
                        (
                            ?, ?, ?
                        );""", (studierender.name, studierender.matrikelnummer, studierender.studiengang))

    def update(self, studierendeId: int, studierender: Studierender):
        return self.db.update(f"""UPDATE studierende SET
                        name = ?,
                        matrikelnummer = ?,
                        studiengang = ?
                        WHERE studierende.id = ?;""", (studierender.name, studierender.matrikelnummer, studierender.studiengang, int(studierendeId)))
        
    def delete(self, studierendeId: int):
        result = self.db.delete(f"DELETE FROM studierende WHERE studierende.id = ?", str(studierendeId))
        return result

    def get_one(self, studierendeId: int):
        row = self.db.read(f"SELECT * FROM studierende WHERE studierende.id = ?", str(studierendeId))
        return Studierender(*row)
    
    def get_all(self):
        rows = self.db.read("SELECT name, matrikelnummer, studiengang, id FROM studierende")
        return [Studierender(*row) for row in rows]
    
    def get_all_kurse_for_studierender(self, studierenderId):
        rows = self.db.read("""SELECT K.*
                            FROM kurs K
                            JOIN teilnahme T on T.kursId = K.id
                            WHERE T.studierendeId = ?""", (str(studierenderId),))
        return [Kurs(*row) for row in rows]

    def delete_from_kurs(self, studierendeId, kursId):
        return self.db.delete("DELETE FROM teilnahme WHERE kursId = ? AND studierendeId = ?", (str(kursId), str(studierendeId)))

    def add_to_kurs(self, studierendeId, kursId):
        return self.db.update("INSERT INTO teilnahme (studierendeId, kursId) VALUES(?, ?)", (int(studierendeId), int(kursId)))