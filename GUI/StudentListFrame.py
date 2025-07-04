import tkinter as tk
from Models.Studierender import Studierender
from Service.StudierendeService import StudierendeService
from Service.KursService import KursService
from GUI.widgets import Button, Popup, LabeledEntry

class StudentListFrame(tk.Frame):
    def __init__(self, master, show_main_menu, create_student_callback=None, edit_callback=None, delete_callback=None):
        super().__init__(master, bg="#f0f4f8")

        self.studierender_service = StudierendeService()
        self.kurs_service = KursService()

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

        left_frame = tk.Frame(self)
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
            command=self.show_student_form,
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
        canvas = tk.Canvas(right_frame, bg="white", highlightthickness=0)
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

        def handle_edit_student(s):
            self.open_popup()
            self.show_student_form(s)

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
                command=lambda s=student: handle_edit_student(s),
                width=8,
                height=1,
                font=('times', 10)
            )
            edit_btn.pack(side="left", padx=5, pady=5)

            delete_btn = Button(
                entry_frame,
                text="Löschen",
                command=lambda s=student: self.delete_student(s.id),
                bg="red",
                width=8,
                height=1,
                font=('times', 10)
            )
            delete_btn.pack(side="left", padx=5, pady=5)

    def open_popup(self):
        self.popup = Popup(self)
        self.popup_content = tk.Frame(self.popup)

    def show_student_form(self, student: Studierender = None):
        self.popup_content.destroy()
        self.popup_content = tk.Frame(self.popup)

        name_entry = LabeledEntry(self.popup_content, "Name: ", student.name if student else "")
        name_entry.pack()
        matrikelnummer_entry = LabeledEntry(self.popup_content, "Matrikelnummer: ", student.matrikelnummer if student else "")
        matrikelnummer_entry.pack()
        studiengang_entry = LabeledEntry(self.popup_content, "Studiengang: ", student.studiengang if student else "")
        studiengang_entry.pack()

        if student:
            # Scrollable list container
            # Wrapper-Frame für Canvas und Scrollbar
            scroll_frame = tk.Frame(self.popup_content)
            scroll_frame.pack(fill="both", expand=True)

            # Canvas für den Inhalt
            canvas = tk.Canvas(scroll_frame, bg='white', highlightthickness=0)
            canvas.pack(side="left", fill="both", expand=True)

            # Scrollbar direkt rechts neben der Canvas
            scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
            scrollbar.pack(side="right", fill="y")

            canvas.configure(yscrollcommand=scrollbar.set)

            # Container für alle Listeneinträge
            list_container = tk.Frame(canvas, bg="white")
            list_window = canvas.create_window((0, 0), window=list_container, anchor="nw")

            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
                canvas.itemconfig(list_window, width=canvas.winfo_width())

            list_container.bind("<Configure>", on_configure)
            canvas.bind('<Configure>', on_configure)

            kurse = self.studierender_service.get_all_kurse_for_studierender(student.id)
            for kurs in kurse:
                entry_frame = tk.Frame(list_container, bg="grey", bd=1, relief="solid")
                entry_frame.pack(fill="x", pady=6, padx=10)

                label = tk.Label(
                    entry_frame,
                    text=str(kurs)
                )
                label.pack(side="left", padx=(10, 20), pady=8, expand=True, fill="x")

                # Verknüpfung zwischen Kurs und Student entfernen
                delete_btn = Button(
                    entry_frame,
                    text="Löschen",
                    command=lambda k=kurs: self.remove_student_from_kurs(student, k.id),
                    bg="red",
                    width=8,
                    height=1,
                    font=('times', 10)
                )
                delete_btn.pack(side="left", padx=5, pady=5)

            def render_kurs_verknuepfung():
                self.show_kurs_verknuepfung(student)

            # Button um Student zu kursen hinzuzufügen
            add_verknuepfung_btn = Button(
            self.popup_content,
            text="Student zu neuem Kurs hinzufügen",
            command=render_kurs_verknuepfung)

            add_verknuepfung_btn.pack()

        save_btn = Button(
            self.popup_content,
            text="Speichern",
            command=lambda: self.edit_student(student, name_entry.get(), matrikelnummer_entry.get(), studiengang_entry.get(), self.popup)
            if student
            else self.save_student(
                self.create_student(
                    name_entry.get(),
                    matrikelnummer_entry.get(),
                    studiengang_entry.get()
                ),
                self.popup
            )
        )
        save_btn.pack()

        self.popup_content.pack(fill='both')
        self.popup.content = self.popup_content



    def show_kurs_verknuepfung(self, student: Studierender):
        self.popup_content.destroy()
        self.popup_content = tk.Frame(self.popup)

        # Wrapper für Scrollbereich
        scroll_frame = tk.Frame(self.popup_content)
        scroll_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(scroll_frame, bg="lightblue", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        list_container = tk.Frame(canvas, bg="white")
        list_window = canvas.create_window((0, 0), window=list_container, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(list_window, width=canvas.winfo_width())

        list_container.bind("<Configure>", on_configure)
        canvas.bind('<Configure>', on_configure)

        # Hole alle Kurse (du brauchst ggf. self.kurs_service.get_all() oder so ähnlich)
        # todo: hier methode schreiben, die nur kurse holt, in denen der Student noch nicht ist
        alle_kurse = self.studierender_service.get_all_kurse_where_studierender_is_not_part_of(student.id)

        for kurs in alle_kurse:
            entry_frame = tk.Frame(list_container, bg="white", bd=1, relief="solid")
            entry_frame.pack(fill='both', pady=6, padx=10)

            label = tk.Label(
                entry_frame,
                text=str(kurs),
                font=("Arial", 11)
            )
            label.pack(side="left", padx=(10, 20), pady=8, expand=True, fill="x")

            verknuepfen_btn = Button(
                entry_frame,
                text="Verknüpfen",
                command=lambda k=kurs: self.add_student_to_kurs(student, k.id),
                bg="green",
                fg="white",
                width=10,
                height=1,
                font=('times', 10)
            )
            verknuepfen_btn.pack(side="left", padx=5, pady=5)

        self.popup_content.pack(fill='both')
        self.popup.content = self.popup_content

    def create_student(self, name: str, matrikelnummer: str, studiengang: str):
        return Studierender(name, matrikelnummer, studiengang)
    
    def edit_student(self, student: Studierender, name, matrikelnummer, studiengang, popup: Popup):
        print("before", student)
        student.name = name
        student.matrikelnummer = matrikelnummer
        student.studiengang = studiengang
        print("after", student)
        result = self.studierender_service.update(student.id, student)
        
        if result > 0:
            if popup is not None:
                popup.destroy()
            self.reload()

    def save_student(self, student: Studierender, popup: Popup=None):
        result = self.studierender_service.create(student)

        if result > 0:
            if popup is not None:
                popup.destroy()
            self.reload()

    def delete_student(self, student_id: int):
        if self.studierender_service.delete(student_id) > 0 :
            self.reload()

    def remove_student_from_kurs(self, student: Studierender, kurs_id: int):
        if self.studierender_service.delete_from_kurs(student.id, kurs_id) > 0:
            self.show_student_form(student)

    def add_student_to_kurs(self, student: Studierender, kurs_id: int):
        if self.studierender_service.add_to_kurs(student.id, kurs_id) > 0:
            self.show_student_form(student)

    def reload(self):
        if hasattr(self.master, "show_students"):
            print("Reloading")
            self.master.show_students()
