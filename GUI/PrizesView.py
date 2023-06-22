import tkinter
from tkinter import ttk
from Classes.Database import Database
from Classes.User import User


class PrizesView:
    def __init__(self, login):
        self.window = tkinter.Tk()
        self.window.title("Prizes")
        data_user = Database.get_user(login)
        self.user = User(login, data_user[0], data_user[2], data_user[1], data_user[3])
        self.prizes_list = Database.get_all_prizes()
        self.update_prizes()
        self.list_login = Database.get_all_prizes_by_login(login)
        self.set_prizes_view()

    def update_prizes(self):
        points = self.user.points
        for i in range(len(self.prizes_list)):
            if self.prizes_list[i][1] is None:
                self.prizes_list[i][1] = 0
            if points >= self.prizes_list[i][1]:
                if not Database.does_user_prize_exist(self.user.id_User, self.prizes_list[i][0]):
                    Database.insert_user_prize(self.user.id_User, self.prizes_list[i][0])

    def set_prizes_view(self):
        treeview = ttk.Treeview(self.window, columns=("Min points", "Description"), show="headings")
        treeview.pack()

        treeview.heading("#1", text="Min Points")
        treeview.heading("#2", text="Description")

        for row in self.list_login:
            treeview.insert("", tkinter.END, values=row)

        self.window.mainloop()
