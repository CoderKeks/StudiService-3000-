from abc import ABC

class Person(ABC):
    def __init__(self, name: str, email: str = None, telefon: int = None):
        self.__name = name
        self.__email = email
        self.__telefone = telefon

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

class Dozent(Person):
    def __init__(self, name: str, personalnummer: int, institut: Institut, id: int = None, email: str = None, telefon: int = None, titel: str = None):
        super().__init__(name, email, telefon)
        self.__id = id
        self.__personalnummer = personalnummer
        self.__institut = institut
        self.__titel = titel

class Student(Person):
    def __init__(self, name: str, matrikelnummer: int, studiengang: Studiengang, id: int = None, email: str = None, telefon: int = None):
        super().__init__(name, email, telefon)
        self.__id = id
        self.__matrikelnummer = matrikelnummer
        self.__studiengang = studiengang

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def matrikelnummer(self):
        return self.__matrikelnummer
    
    @matrikelnummer.setter
    def matrikelnummer(self, value: int):
        self.__matrikelnummer = value

    @property
    def studiengang(self):
        return self.__studiengang
    
    @studiengang.setter
    def studiengang(self, value: Studiengang):
        self.__studiengang = value

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Matrikelnummer: {self.matrikelnummer}, Studiengang: {self.studiengang.name}"