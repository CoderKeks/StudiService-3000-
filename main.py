import Models
from GraphicalUserInterface import GraphicalUserInterface
import Models.Kurs
import Service
import Service.KursService

# todo: implement .env for config values like window size and database file name

if __name__ == "__main__":
    Service.KursService.KursService().create(Models.Kurs.Kurs('Deutsch', 'Ruhl', 1))    
    ui = GraphicalUserInterface()
    