import tkinter as tk
from GUI.KursListFrame import KursListFrame
from GUI.MainMenuFrame import MainMenuFrame 
from GUI.StudentListFrame import StudentListFrame
from Service.KursService import KursService
from Service.StudierendeService import StudierendeService
from GraphicalUserInterface import GraphicalUserInterface
from Models.Kurs import Kurs
from Models.Studierender import Studierender

# todo: implement .env for config values like window size and database file name

#config
PROJECT_NAME = "Studi-Service-3000"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.kurs_service = KursService()
        self.studierender_service = StudierendeService()
        
        self.title(PROJECT_NAME)
        self.geometry("%dx%d" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        self.show_main_menu()

    def show_main_menu(self):
        self._show_frame(MainMenuFrame(self, self.show_students, self.show_courses))

    def show_students(self):
        self._show_frame(StudentListFrame(self, self.show_main_menu))

    def show_courses(self):
        self._show_frame(KursListFrame(self, self.show_main_menu))

    def _show_frame(self, frame):
        if hasattr(self, "_frame") and self._frame is not None:
            self._frame.destroy()
        self._frame = frame
        self._frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    studi_service = StudierendeService()
    
    # Testdaten erzeugen
    kurs_id = KursService().create(Kurs('ITS', 'Dörr', 1))

    # GUI starten
    App().mainloop()

""" if __name__ == "__main__":
    KursService().create(Kurs('Deutsch', 'Ruhl', 1))    
    ui = GraphicalUserInterface() """