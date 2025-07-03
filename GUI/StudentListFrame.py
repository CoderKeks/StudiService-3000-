import tkinter as tk
from Models.Studierender import Studierender
from Service.StudierendeService import StudierendeService
from GUI.widgets import Button, Popup, LabeledEntry

class StudentListFrame(tk.Frame):
    def __init__(self, master, show_main_menu, create_student_callback=None, edit_callback=None, delete_callback=None):
        super().__init__(master, bg="#f0f4f8")

        self.studierender_service = StudierendeService()

        self.columnconfigure(0, weight=1, minsize=260)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        # Left frame
        left_title = tk.Label(
            self,
            text="Aktionen",
            font=('Times', 22, 'bold')
        )
        left_title.grid(row=0, column=0, sticky="ew", padx=(30, 10), pady=(5, 0))

        left_frame = tk.Frame(self, bg="red")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=(30, 10), pady=10)
        left_frame.rowconfigure(0, weight=0)
        left_frame.rowconfigure(1, weight=1)
        left_frame.rowconfigure(2, weight=0)
        left_frame.columnconfigure(0, weight=1)

        back_btn = Button(self, text="< Zurück", command=show_main_menu, width = 8, height = 1)
        back_btn.grid(row=0, column=0, sticky="nw", pady=(0, 20))

        create_btn = Button(
            left_frame,
            text="Neuen Studenten anlegen",
            command=create_student_callback if create_student_callback else lambda: None,
            bg="blue"
        )
        create_btn.grid(row=1, column=0, sticky="n", pady=(0, 0))

        # Right frame
        right_title = tk.Label(
            self,
            text="Studierende",
            font=('Times', 22, 'bold')
        )
        right_title.grid(row=0, column=1, sticky="ew", padx=(10, 30), pady=(5, 0))

        right_frame = tk.Frame(self, bg="orange")
        right_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 30), pady=10)
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        # Scrollable list container
        canvas = tk.Canvas(right_frame, bg="pink", highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        list_container = tk.Frame(canvas, bg="white")
        list_window = canvas.create_window((0, 0), window=list_container, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(list_window, width=canvas.winfo_width())

        list_container.bind("<Configure>", on_configure)
        canvas.bind('<Configure>', on_configure)

        students = self.studierender_service.get_all()
        for student in students:
            entry_frame = tk.Frame(list_container, bg="grey", bd=1, relief="solid")
            entry_frame.pack(fill="x", pady=6, padx=10)

            label = tk.Label(
                entry_frame,
                text=str(student)
            )
            label.pack(side="left", padx=(10, 20), pady=8, expand=True, fill="x")

            edit_btn = Button(
                entry_frame,
                text="Bearbeiten",
                command=lambda s=student: self.open_student_popup(s),
                width=8,
                height=1,
                font=('times', 10)
            )
            edit_btn.pack(side="left", padx=5, pady=5)

            delete_btn = Button(
                entry_frame,
                text="Löschen",
                command=lambda student: self.studierender_service.delete(student.id) if self.studierender_service.delete else None,
                bg="red",
                width=8,
                height=1,
                font=('times', 10)
            )
            delete_btn.pack(side="left", padx=5, pady=5)

    def open_student_popup(self, student: Studierender):

        popup = Popup(self, title="Student anlegen", button_text="Speichern")

        content = tk.Frame(popup)

        LabeledEntry(content, "Name: ", student.name).pack()
        LabeledEntry(content, "Matrikelnummer: ", student.matrikelnummer).pack()
        LabeledEntry(content, "Studiengang: ", student.studiengang).pack()
        
        content.pack(padx=30, pady=(0, 15))

        popup.content = content