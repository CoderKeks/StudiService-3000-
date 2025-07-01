from Models.Kurs import Kurs
from Models.Person import Student, Dozent
from GraphicalUserInterface import GraphicalUserInterface
from Repositories.KursRepository import KursService
from Repositories.StudentRepository import StudierendeService

# todo: implement .env for config values like window size and database file name

if __name__ == "__main__":
    #KursService().create(Kurs('Deutsch', 'Ruhl', 1))    
    ui = GraphicalUserInterface()