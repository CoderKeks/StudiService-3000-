import tkinter as tk

class StudentListFrame(tk.Frame):
    def __init__(self, master, students, show_main_menu):
        super().__init__(master)
        tk.Button(self, text="Zurück", command=show_main_menu).pack()
        for s in students:
            tk.Label(self, text=str(s)).pack()