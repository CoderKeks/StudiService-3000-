import Database
class Kurs:
    def __init__(self, kursname, dozent, semester):
        self.kursname = kursname
        self.dozent = dozent
        self.semester = semester

        db = Database.Database("test.db")
        db.create(f"CREATE TABLE IF NOT EXISTS kurs(kursname TEXT, dozent TEXT, semester INTEGER)")
        db.update(f"INSERT INTO kurs VALUES ('{self.kursname}', '{self.dozent}', {self.semester})")
        


    # kursname
    @property
    def kursname(self):
        return self._kursname
    
    @kursname.setter
    def kursname(self, value):
        self._kursname = value

    # dozent
    @property
    def dozent(self):
        return self._dozent
    
    @dozent.setter
    def dozent(self, value):
        self._dozent = value

    # semester
    @property
    def semester(self):
        return self._semester
    
    @semester.setter
    def semester(self, value):
        self._semester = value