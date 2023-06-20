import tkinter
from tkinter import ttk
from Classes.Database import Database


class PrizesView:
    def __init__(self, login):
        self.window = tkinter.Tk()
        self.window.title("Prizes")
        self.list = Database.get_all_prizes_by_login(login)
        self.set_prizes_view()

    def set_prizes_view(self):
        treeview = ttk.Treeview(self.window, columns=("Min points", "Description"), show="headings")
        treeview.pack()

        treeview.heading("#1", text="Min Points")
        treeview.heading("#2", text="Description")

        for row in self.list:
            treeview.insert("", tkinter.END, values=row)

        self.window.mainloop()
