import Database
class Kurs:
    def __init__(self, kursname, dozent, semester, id=None):
        self.id = id
        self.kursname = kursname
        self.dozent = dozent
        self.semester = semester

    # ID
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    # kursname
    @property
    def kursname(self):
        return self.__kursname
    
    @kursname.setter
    def kursname(self, value):
        self.__kursname = value

    # dozent
    @property
    def dozent(self):
        return self.__dozent
    
    @dozent.setter
    def dozent(self, value):
        self.__dozent = value

    # semester
    @property
    def semester(self):
        return self.__semester
    
    @semester.setter
    def semester(self, value):
        self.__semester = value

    def __str__(self):
        return f"ID: {self.id}, Kursname: {self.kursname}, Dozent: {self.dozent}, Semester: {self.semester}"
