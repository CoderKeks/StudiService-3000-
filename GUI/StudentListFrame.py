import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Models.Studierender import Studierender
from Service.StudierendeService import StudierendeService
from GUI.widgets import Button, Popup, LabeledEntry

class StudentListFrame(tk.Frame):
    def __init__(self, master, show_main_menu, create_student_callback=None, edit_callback=None, delete_callback=None):
        super().__init__(master)

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

        export_btn = Button(
            left_frame,
            text="CSV Export",
            command=self.export_students_csv,
            bg="blue"
        )
        export_btn.grid(row=1, column=0, sticky="n", pady=(100, 0))


        # Right frame
        right_title = tk.Label(
            self,
            text="Studierende",
            font=('Times', 22, 'bold')
        )
        right_title.grid(row=0, column=1, sticky="ew", padx=(10, 30), pady=(5, 0))

        right_frame = tk.Frame(self)
        right_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 30), pady=10)
        right_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)

        # Scrollable list container
        canvas = tk.Canvas(right_frame, highlightthickness=0)
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        list_container = tk.Frame(canvas)
        list_window = canvas.create_window((0, 0), window=list_container, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(list_window, width=canvas.winfo_width())

        list_container.bind("<Configure>", on_configure)
        canvas.bind('<Configure>', on_configure)

        students = self.studierender_service.get_all()
        for student in students:
            entry_frame = tk.Frame(list_container, bd=1, relief="solid")
            entry_frame.pack(fill="x", pady=6, padx=10)

            label = tk.Label(
                entry_frame,
                text=str(student)
            )
            label.pack(side="left", padx=(10, 20), pady=8, expand=True, fill="x")

            edit_btn = Button(
                entry_frame,
                text="Bearbeiten",
                command=lambda s=student: self.show_student_form(s, "Student editieren"),
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

    def show_student_form(self, student: Studierender = None, title: str = "Student anlegen"):
        popup = Popup(self, title)
        content = tk.Frame(popup)

        name_entry = LabeledEntry(content, "Name: ", student.name if student else "")
        name_entry.pack(padx=10, pady=10)
        matrikelnummer_entry = LabeledEntry(content, "Matrikelnummer: ", student.matrikelnummer if student else "")
        matrikelnummer_entry.pack(padx=10, pady=10)
        studiengang_entry = LabeledEntry(content, "Studiengang: ", student.studiengang if student else "")
        studiengang_entry.pack(padx=10, pady=10)
        save_btn = Button(
            content,
            text="Speichern",
            command=lambda: self.edit_student(
                student, 
                name_entry.get(), 
                matrikelnummer_entry.get(), 
                studiengang_entry.get(),popup
            ) if student else self.save_student(
                self.create_student(
                    name_entry.get(),
                    matrikelnummer_entry.get(),
                    studiengang_entry.get()
                ),
                popup
            )
        )
        save_btn.pack(padx=10, pady=10)

        content.pack()
        popup.content = content

    def create_student(self, name: str, matrikelnummer: str, studiengang: str):
        return Studierender(name, matrikelnummer, studiengang)
    
    def edit_student(self, student: Studierender, name, matrikelnummer, studiengang, popup):
        student.name = name
        student.matrikelnummer = matrikelnummer
        student.studiengang = studiengang
        result = self.studierender_service.update(student.id, student)

        if result > 0 and popup is not None:
            popup.destroy()
            self.reload()

    def save_student(self, student: Studierender, popup=None):
        result = self.studierender_service.create(student)

        if result > 0 and popup is not None:
            popup.destroy()
            self.reload()

    def delete_student(self, student_id: int):
        if self.studierender_service.delete(student_id) > 0 :
            self.reload()

    def reload(self):
        if hasattr(self.master, "show_students"):
            self.master.show_students()

    def export_students_csv(self):
        students = self.studierender_service.get_all()
        if not students:
            messagebox.showinfo("Export", "Keine Studierenden zum Exportieren vorhanden.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV-Dateien", "*.csv")],
            title="Studierende als CSV exportieren"
        )
        if not file_path:
            return

        with open(file_path, mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(["ID", "Name", "Matrikelnummer", "Studiengang"])
            for s in students:
                writer.writerow([s.id, s.name, s.matrikelnummer, s.studiengang])

        messagebox.showinfo("Export", f"Export erfolgreich:\n{file_path}")
