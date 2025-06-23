class Studierender:
    def __init__(self, name, matrikelnummer, studiengang):
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.studiengang = studiengang

    # Name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    # matrikelnummer
    @property
    def matrikelnummer(self):
        return self.__matrikelnummer
    
    @matrikelnummer.setter
    def matrikelnummer(self, value):
        self.__matrikelnummer = value

    # studiengang
    @property
    def studiengang(self):
        return self.__studiengang
    
    @studiengang.setter
    def studiengang(self, value):
        self.__studiengang = value