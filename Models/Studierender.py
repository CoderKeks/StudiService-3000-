class Studierender:
    def __init__(self, name, matrikelnummer, studiengang, id=None):
        self.id = id
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.studiengang = studiengang

    # ID
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

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

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Matrikelnummer: {self.matrikelnummer}, Studiengang: {self.studiengang}"