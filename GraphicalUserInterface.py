import tkinter
from Models.Kurs import Kurs
from Models.Person import Student
from Repositories.KursRepository import KursService
from Repositories.StudentRepository import StudierendeService

#config
project_name = "Studi-Service-3000"
width = 1000
height = 500

class GraphicalUserInterface:    
    def __init__(self):

        self.kurs_service = KursService()
        self.studierender_service = StudierendeService()

        self.root = tkinter.Tk(baseName=project_name, className=project_name, useTk=1)
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(width, height)
        self.root.maxsize(width, height)
        self.root.title = project_name
        self.show_main_menu()
        self.root.mainloop()

    def show_main_menu(self):
        self.clear_window()
        self.add_title("Wilkommen im Studi-Service-3000. Hier können Sie Studierende und Kurse bearbeiten, neu anlegen, und löschen.")

        button_studierende = tkinter.Button(self.root, text="Studierende anzeigen und bearbeiten", command=self.show_studenten_list)
        button_studierende.config(font=('times', 15), justify='center', pady=5, padx=5, width=100, height=5)
        button_studierende.pack()

        button_kurse = tkinter.Button(self.root, text="Kurse anzeigen und bearbeiten", command=self.show_class_list)
        button_kurse.config(font=('times', 15), justify='center', pady=5, padx=5, width=100, height=5)
        button_kurse.pack()

    
    def show_studenten_list(self):
        self.clear_window()
        self.add_home_btn()
        self.add_title("Studenten-Liste")

        create_btn = tkinter.Button(self.root, text="Neuen Studierenden anlegen", command=self.show_create_student)
        create_btn.pack(fill="x")

        scroll_bar = tkinter.Scrollbar(self.root)
        scroll_bar.pack( side = "right", fill="y")
        mylist = tkinter.Listbox(self.root, yscrollcommand = scroll_bar.set )
        mylist.config(height=100)

        for student in self.studierender_service.get_all():
            mylist.insert("end", str(student))

        mylist.pack(fill = "both")
        scroll_bar.config( command = mylist.yview )


    def show_create_student(self):
        self.clear_window()
        self.add_home_btn()
        self.add_title("Neuen Student hinzufügen")
        name = self.add_field_with_label("Name")
        matrikelnummer = self.add_field_with_label("Matrikelnummer")
        studiengang = self.add_field_with_label("Studiengang")

        def handle_create_student():
            self.studierender_service.create(Student(name.get(), matrikelnummer.get(), studiengang.get()))
            self.show_studenten_list()

        submit_btn = tkinter.Button(self.root, text="Student anlegen",command=handle_create_student)
        submit_btn.pack(pady=20)

    def show_class_list(self):
        self.clear_window()
        self.add_home_btn()
        self.add_title("Kurs-Liste")

        create_btn = tkinter.Button(self.root, text="Neuen Kurs anlegen", command=self.show_create_class)
        create_btn.pack(fill="x")

        scroll_bar = tkinter.Scrollbar(self.root)
        scroll_bar.pack( side = "right", fill="y")
        mylist = tkinter.Listbox(self.root, yscrollcommand = scroll_bar.set )
        mylist.config(height=100)

        for student in self.kurs_service.get_all():
            mylist.insert("end", str(student))

        mylist.pack(fill = "both")
        scroll_bar.config( command = mylist.yview )


    def show_create_class(self):
        self.clear_window()
        self.add_home_btn()
        self.add_title("Neuen Kurs hinzufügen")
        kursname = self.add_field_with_label("Kursname")
        dozent = self.add_field_with_label("Dozent")
        semester = self.add_field_with_label("Semester")

        def handle_create_class():
            self.kurs_service.create(Kurs(kursname.get(), dozent.get(), int(semester.get())))
            self.show_class_list()

        submit_btn = tkinter.Button(self.root, text="Kurs anlegen",command=handle_create_class)
        submit_btn.pack(pady=20)


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_home_btn(self):
        back_btn = tkinter.Button(self.root, text="Home", command=self.show_main_menu)
        back_btn.place(x=0, y=0)
        return back_btn

    def add_title(self, text):
        header = tkinter.Message(self.root, text=text)
        header.config(font=('times', 24), justify='center', pady=30, width=500)
        header.pack()
        return header

    def add_field_with_label(self, text):
        label = tkinter.StringVar()
        tkinter.Label(self.root, text=text).pack()
        tkinter.Entry(self.root, textvariable=label).pack()
        return label
    
