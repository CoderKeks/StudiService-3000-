import Database, pathlib
from Service.KursService import KursService
from Models.Kurs import Kurs

if __name__ == "__main__":
    kurs_service = KursService()

    print(kurs_service.getAll())