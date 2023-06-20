import tkinter
from tkinter import ttk
from Classes.Database import Database


class Leaderboard:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Leaderboard')
        self.list = Database.get_all_users_points()
        self.list = sorted(self.list, key=lambda x: x[1], reverse=True)
        self.set_leaderboard()

    def set_leaderboard(self):
        treeview = ttk.Treeview(self.window, columns=("Place", "User", "Points"), show="headings")
        treeview.pack()

        treeview.heading("Place", text="Place")
        treeview.heading("User", text="User")
        treeview.heading("Points", text="Points")

        for i in range(len(self.list)):
            self.list[i].insert(0, i+1)

        for row in self.list:
            treeview.insert("", tkinter.END, values=row)

        self.window.mainloop()
