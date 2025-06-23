class Studierender:
    def __init__(self, name, matrikelnummer, studiengang):
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.studiengang = studiengang

    # Name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    # matrikelnummer
    @property
    def matrikelnummer(self):
        return self._matrikelnummer
    
    @matrikelnummer.setter
    def matrikelnummer(self, value):
        self._matrikelnummer = value

    # studiengang
    @property
    def studiengang(self):
        return self._studiengang
    
    @studiengang.setter
    def studiengang(self, value):
        self._studiengang = value