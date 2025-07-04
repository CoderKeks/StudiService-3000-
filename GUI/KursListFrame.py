import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Service.KursService import KursService
from GUI.widgets import Button, LabeledEntry, Popup
from Models.Kurs import Kurs

class KursListFrame(tk.Frame):
    def __init__(self, master, show_main_menu, create_kurs_callback=None, edit_callback=None, delete_callback=None):
        super().__init__(master)

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

        left_frame = tk.Frame(self,)
        left_frame.grid(row=1, column=0, sticky="nsew", padx=(30, 10), pady=10)
        left_frame.rowconfigure(0, weight=0)
        left_frame.rowconfigure(1, weight=1)
        left_frame.rowconfigure(2, weight=0)
        left_frame.columnconfigure(0, weight=1)

        back_btn = Button(self, text="< Zurück", command=show_main_menu, width=8, height=1)
        back_btn.grid(row=0, column=0, sticky="nw", pady=(0, 20))

        create_btn = Button(
            left_frame,
            text="Neuen Kurs anlegen",
            command=self.show_kurs_form,
            bg="green"
        )
        create_btn.grid(row=1, column=0, sticky="n", pady=(0, 0))

        export_btn = Button(
            left_frame,
            text="CSV Export",
            command=self.export_kurse_csv,
            bg="green"
        )
        export_btn.grid(row=1, column=0, sticky="n", pady=(100, 0))

        # Right panel
        right_title = tk.Label(
            self,
            text="Kurse",
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

        kurse = self.kurs_service.get_all()
        for kurs in kurse:
            entry_frame = tk.Frame(list_container, bd=1, relief="solid")
            entry_frame.pack(fill="x", pady=6, padx=10)

            label = tk.Label(
                entry_frame,
                text=str(kurs)
            )
            label.pack(side="left", padx=(10, 20), pady=8, expand=True, fill="x")

            edit_btn = Button(
                entry_frame,
                text="Bearbeiten",
                command=lambda k=kurs: self.show_kurs_form(k, "Kurs editieren"),
                width=8,
                height=1,
                font=('Times', 10)
            )
            edit_btn.pack(side="left", padx=5, pady=5)

            delete_btn = Button(
                entry_frame,
                text="Löschen",
                command=lambda k=kurs: self.delete_kurs(k.id),
                bg="red",
                width=8,
                height=1,
                font=('Times', 10)
            )
            delete_btn.pack(side="left", padx=5, pady=5)

    def show_kurs_form(self, kurs: Kurs = None, title="Kurs anlegen"):
        popup = Popup(self, title)
        content = tk.Frame(popup)

        name_entry = LabeledEntry(content, "Name: ", kurs.kursname if kurs else "")
        name_entry.pack(padx=10, pady=10)
        semester_entry = LabeledEntry(content, "Semester: ", kurs.semester if kurs else "")
        semester_entry.pack(padx=10, pady=10)
        dozent_entry = LabeledEntry(content, "Dozent: ", kurs.dozent if kurs else "")
        dozent_entry.pack(padx=10, pady=10)

        save_btn = Button(
            content,
            text="Speichern",
            command=lambda: self.edit_kurs(
                kurs,
                name_entry.get(),
                semester_entry.get(),
                dozent_entry.get(),
                popup
            ) if kurs else self.save_kurs(
                self.create_kurs(
                    name_entry.get(),
                    semester_entry.get(),
                    dozent_entry.get()
                ),
                popup
            )
        )
        save_btn.pack(padx=10, pady=10)

        content.pack()
        popup.content = content

    def create_kurs(self, name: str, semester: int, dozent: str):
        return Kurs(name, dozent, semester)

    def save_kurs(self, kurs: Kurs, popup):
        result = self.kurs_service.create(kurs)
        if result > 0 and popup is not None:
            popup.destroy()
            self.reload()

    def edit_kurs(self, kurs: Kurs, name: str, semester: int, dozent: str, popup):
        kurs.kursname = name
        kurs.semester = semester
        kurs.dozent = dozent
        result = self.kurs_service.update(kurs.id, kurs)
        
        if result > 0 and popup is not None:
            popup.destroy()
            self.reload()
        

    def delete_kurs(self, kurs_id: int):
        if self.kurs_service.delete(kurs_id) > 0:
            self.reload()

    def reload(self):
        if hasattr(self.master, "show_courses"):
            self.master.show_courses()

    def export_kurse_csv(self):
        kurse = self.kurs_service.get_all()
        if not kurse:
            messagebox.showinfo("Export", "Keine Studierenden zum Exportieren vorhanden.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV-Dateien", "*.csv")],
            title="Kurse als CSV exportieren"
        )
        if not file_path:
            return

        with open(file_path, mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(["ID", "Kursname", "Dozent", "Semester"])
            for s in kurse:
                writer.writerow([s.id, s.kursname, s.dozent, s.semester])

        messagebox.showinfo("Export", f"Export erfolgreich:\n{file_path}")