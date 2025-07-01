import tkinter as tk

class MainMenuFrame(tk.Frame):
    def __init__(self, master, show_students, show_courses):
        super().__init__(master)
        tk.Label(self, text="Willkommen!").pack()
        tk.Button(self, text="Studierende", command=show_students).pack()
        tk.Button(self, text="Kurse", command=show_courses).pack()