import Database
class Kurs:
    def __init__(self, kursname, dozent, semester):
        self.kursname = kursname
        self.dozent = dozent
        self.semester = semester
        

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
