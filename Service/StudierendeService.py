from Database import Database
from Models.Studierender import Studierender

class StudierendeService:
    def __init__(self, db: Database):
        self.db = db

    def create(self, studierender: Studierender):
        return self.db.create(f"""
                        INSERT INTO studierende (
                            name,
                            matrikelnummer,
                            studiengang
                        )
                        VALUES 
                        (
                            '{studierender.name}',
                            '{studierender.matrikelnummer}',
                            '{studierender.studiengang}'
                        );""")

    def update(self, studierendeId: int, studierender: Studierender):
        return self.db.update(f"""UPDATE studierende SET
                        name = '{studierender.name}',
                        matrikelnummer = '{studierender.matrikelnummer}',
                        studiengang = {studierender.studiengang}
                        WHERE studierende.id = {studierendeId};""")
        
    def delete(self, studierendeId: int):
        return self.db.delete(f"DELETE FROM studierende WHERE studierende.id = {studierendeId}") > 1 and self.db.delete(f"DELETE FROM teilnahme WHERE teilname.studierendeId = {studierendeId}") > 1

    def getOne(self, studierendeId: int):
        return self.db.read(f"SELECT FROM studierende WHERE studierende.id = {studierendeId} LIMIT 1")