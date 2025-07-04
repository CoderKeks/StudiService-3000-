import tkinter as tk

class Button(tk.Button):
    base_style = {
        "font": ('Times New Roman', 14, 'bold'),
        "bg": "grey",
        "fg": "white",
        "activebackground": "lightblue",
        "activeforeground": "white",
        "bd": 0,
        "relief": "ridge",
        "cursor": "hand2",
        "width": 22,
        "height": 2,
    }
    def __init__(self, master, text, command, **kwargs):
        style = self.base_style.copy()
        style.update(kwargs)
        super().__init__(
            master,
            text=text,
            command=command,
            **style
        )

class ScrollList(tk.Frame):
    def __init__(self, master, items, height=10, width=40, **kwargs):
        super().__init__(master, **kwargs)
        self.listbox = tk.Listbox(self, height=height, width=width)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        for item in items:
            self.listbox.insert("end", item)

    def get_selected(self):
        selection = self.listbox.curselection()
        return self.listbox.get(selection) if selection else None

class LabeledEntry(tk.Frame):
    def __init__(self, master, label, initial_value="", **kwargs):
        super().__init__(master, **kwargs)
        tk.Label(self, text=label).pack(side="left", padx=(0, 5))
        self.entry = tk.Entry(self)
        self.entry.pack(side="left", fill="x", expand=True)
        if initial_value:
            self.set(initial_value)

    def get(self):
        return self.entry.get()

    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

class LabeledDropdown(tk.Frame):
    def __init__(self, master, label, options, **kwargs):
        super().__init__(master, **kwargs)
        self.var = tk.StringVar()
        self.label = tk.Label(self, text=label)
        self.dropdown = tk.OptionMenu(self, self.var, *options)
        self.label.pack(side="left", padx=(0, 5))
        self.dropdown.pack(side="left", fill="x", expand=True)
        if options:
            self.var.set(options[0])

    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)

class Popup(tk.Toplevel):
    def __init__(self, master, title="Hinweis", content=None, on_close=None, **kwargs):
        super().__init__(master, **kwargs)

        self.title(title)
        self.grab_set()
        self.resizable(False, False)
        self.geometry("+%d+%d" % (master.winfo_rootx() + 400, master.winfo_rooty() + 150))

        tk.Label(self, text=title, font=('Times', 16, 'bold')).pack(padx=30, pady=(20, 10))

        if content is not None and isinstance(content, tk.Widget):
            self.content = content
        elif content is not None:
                tk.Label(self, text=str(content), font=('Times New Roman', 13), wraplength=350).pack(padx=30, pady=(0, 15))

        self.on_close = on_close
        self.protocol("WM_DELETE_WINDOW", self._close)

    def _close(self):
        if self.on_close:
            
            self.on_close()
        self.destroy()