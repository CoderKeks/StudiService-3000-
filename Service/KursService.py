from Database import Database
from Models.Kurs import Kurs

class KursService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, kurs: Kurs):
        return self.db.create(f"""INSERT INTO kurs 
                        (
                            kursname,
                            dozent,
                            semester
                        )
                        VALUES 
                       (
                            '{kurs.kursname}',
                            '{kurs.dozent}',
                            '{kurs.semester}'
                        );""")

    def update(self, kursID: int, kurs: Kurs):
        return self.db.update(f"""UPDATE kurs SET
                        kursname = '{kurs.kursname}',
                        dozent = '{kurs.dozent}',
                        semester = {kurs.semester}
                        WHERE kurs.id = {kursID};""")
        
    def delete(self, kursID: int):
        return self.db.delete(f"DELETE FROM kurs WHERE kurs.id = {kursID}") > 1 and self.db.delete(f"DELETE FROM teilnahme WHERE teilname.kursId = {kursID}") > 1

    def getOne(self, kursID: int):
        return self.db.read(f"SELECT FROM kurs WHERE kurs.id = {kursID} LIMIT 1")