import tkinter
import re
from tkinter import ttk
from tkinter import messagebox
from Classes.Database import Database
from Classes.UserSettings import UserSettings


class ChangeBackground:
    def __init__(self, user, canvas):
        self.window = tkinter.Tk()
        self.window.title("Select new background")
        self.user = user
        self.canvas = canvas
        self.colors_list = Database.get_all_colors()
        self.set_window()

    def check_button(self, id_color):
        counter = 0
        regex = '^[0-9]+$'
        for color in self.colors_list:
            if color[0] == int(id_color):
                counter += 1

        if counter == 0:
            messagebox.showerror("Wrong index", "Index out of bounds")
        elif re.match(regex, id_color) is None:
            messagebox.showerror("Input error", "Index should be a number")
        else:
            self.canvas.config(bg=self.colors_list[int(id_color)][1])

            user_set = UserSettings(self.user.id_User, int(id_color)+1, 2, 2)
            Database.update_usersettings(user_set)

            self.window.destroy()

    def set_window(self):
        treeview = ttk.Treeview(self.window, columns=("Index", "Color"), show="headings")
        treeview.pack()

        treeview.heading("#1", text="Index")
        treeview.heading("#2", text="Color")

        for i in range(len(self.colors_list)):
            self.colors_list[i][0] -= 1

        for row in self.colors_list:
            treeview.insert("", tkinter.END, values=row)

        input_label = tkinter.Label(self.window, text="Which color would you like to choose? (id)")
        input_label.pack()
        input_input = tkinter.Entry(self.window)
        input_input.pack()
        button_ok = tkinter.Button(self.window, text="Save", command=lambda: self.check_button(input_input.get()))
        button_ok.pack()
        self.window.mainloop()
