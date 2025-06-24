from Models.Studierender import Studierender
from GraphicalUserInterface import GraphicalUserInterface
from Service.StudierendeService import StudierendeService

# todo: implement .env for config values like window size and database file name

if __name__ == "__main__":
    StudierendeService().create(Studierender('Leander', '5', 'ITS'))
    ui = GraphicalUserInterface()
    