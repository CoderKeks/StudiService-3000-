from Database import Database
from Models.Kurs import Kurs

class KursService:
    def __init__(self):
        self.db = Database("./database.db")


    def create(self, kurs: Kurs):
        return self.db.create("""INSERT INTO kurs 
                        (
                            kursname,
                            dozent,
                            semester
                        )
                        VALUES 
                       (
                            ?, ?, ?
                        );""", (kurs.kursname, kurs.dozent, kurs.semester))

    def update(self, kursID: int, kurs: Kurs):
        return self.db.update("""UPDATE kurs SET
                        kursname = ?,
                        dozent = ?,
                        semester = ?
                        WHERE kurs.id = ?;""", (kurs.kursname, kurs.dozent, kurs.semester, kursID))
        
    def delete(self, kursID: int):
        return self.db.delete("DELETE FROM kurs WHERE kurs.id = ?", [kursID])

    def get_one(self, kursID: int):
        row = self.db.read("SELECT * FROM kurs WHERE kurs.id = ? LIMIT 1", [kursID])
        return Kurs(*row[0])
    
    def get_all(self):
        rows = self.db.read("SELECT * FROM kurs")
        return [Kurs(*row) for row in rows]
