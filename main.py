import tkinter as tk
from GUI.MainMenuFrame import MainMenuFrame 
from GUI.StudentListFrame import StudentListFrame
""" import Models
from GraphicalUserInterface import GraphicalUserInterface
import Models.Kurs
import Service
import Service.KursService """

# todo: implement .env for config values like window size and database file name

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Studi-Service-3000")
        self.geometry("800x600")
        self.show_main_menu()

    def show_main_menu(self):
        self._show_frame(MainMenuFrame(self, self.show_students, self.show_courses))

    def show_students(self):
        # Replace with real data/service call
        students = ["Max", "Anna"]
        self._show_frame(StudentListFrame(self, students, self.show_main_menu))

    def show_courses(self):
        # Placeholder for course list frame, implement analog to show_students
        pass

    def _show_frame(self, frame):
        if hasattr(self, "_frame") and self._frame is not None:
            self._frame.destroy()
        self._frame = frame
        self._frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    App().mainloop()

""" if __name__ == "__main__":
    Service.KursService.KursService().create(Models.Kurs.Kurs('Deutsch', 'Ruhl', 1))    
    ui = GraphicalUserInterface() """
    