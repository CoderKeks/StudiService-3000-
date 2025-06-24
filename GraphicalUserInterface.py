import tkinter
from Service.KursService import KursService
from Service.StudierendeService import StudierendeService

#config
project_name = "Studi-Service-3000"
width = 1000
height = 1000

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
        header = tkinter.Message(self.root, text="Wilkommen im Studi-Service-3000. Hier können Sie Studierende und Kurse bearbeiten, neu anlegen, und löschen.")
        header.config(font=('times', 24), justify='center', pady=30)
        header.pack()

        button_studierende = tkinter.Button(self.root, text="Studierende anzeigen und bearbeiten", command=self.show_studenten_list)
        button_studierende.config(font=('times', 15), justify='center', pady=5, padx=5, width=100, height=5)
        button_studierende.pack()

        button_kurse = tkinter.Button(self.root, text="Kurse anzeigen und bearbeiten")
        button_kurse.config(font=('times', 15), justify='center', pady=5, padx=5, width=100, height=5)
        button_kurse.pack()

    
    def show_studenten_list(self):
        self.clear_window()
        self.add_home_btn()
        header = tkinter.Message(self.root, text="Studenten-Liste")
        header.config(font=('times', 24), justify='center', pady=30, width=500)
        header.pack()

        create_btn = tkinter.Button(self.root, text="Neuen Studierenden anlegen", command=self.show_create_student)
        create_btn.pack()

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
        name_label = tkinter.Label(self.root, text="Name")
        name_label.pack()
        name_field = tkinter.Entry(self.root)
        name_field.pack()
        matrikelnummer_label = tkinter.Label(self.root, text="Matrikelnummer")
        matrikelnummer_label.pack()
        matrikelnummer_field = tkinter.Entry(self.root)
        matrikelnummer_field.pack()
        studiengang_label = tkinter.Label(self.root, text="Studiengang")
        studiengang_label.pack()
        studiengang_field = tkinter.Entry(self.root)
        studiengang_field.pack()



    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def add_home_btn(self):
        back_btn = tkinter.Button(self.root, text="Home", command=self.show_main_menu)
        back_btn.place(x=0, y=0)


