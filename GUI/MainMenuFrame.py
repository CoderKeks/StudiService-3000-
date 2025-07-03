import tkinter as tk
from GUI.widgets import Button

class MainMenuFrame(tk.Frame):
    def __init__(self, master, show_students, show_courses):
        super().__init__(master)
        self.configure(bg="white")
        self.create_widgets(show_students, show_courses)

    def create_widgets(self, show_students, show_courses):
        self.title_label = tk.Label(
            self,
            text="Willkommen im Studi-Service-3000!",
            font=('times', 28, 'bold'),
            fg="black",
            pady=40
        )
        self.title_label.pack(pady=(40, 20))

        self.subtitle_label = tk.Label(
            self,
            text="Verwalten Sie Studierende und Kurse einfach und übersichtlich.",
            font=('times', 16)
        )
        self.subtitle_label.pack(pady=(0, 40))

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(pady=20)

        self.btn_students = Button(
            self.button_frame,
            text="Studierende anzeigen und bearbeiten",
            command=show_students,
            bg="blue",
            width=30,
        )
        self.btn_students.pack(pady=10)

        self.btn_courses = Button(
            self.button_frame,
            text="Kurse anzeigen und bearbeiten",
            command=show_courses,
            bg="green",
            width=30,
        )
        self.btn_courses.pack(pady=10)