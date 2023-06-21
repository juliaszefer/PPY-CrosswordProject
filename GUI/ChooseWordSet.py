import tkinter
from tkinter import ttk
import re
from tkinter import messagebox
from Classes.Database import Database
from GUI.ChooseMode import ChooseMode


class ChooseWordSet:
    def __init__(self, user):
        self.window = tkinter.Tk()
        self.window.title('Choose Word Set')
        self.word_set_list = list()
        self.user = user
        self.set_window()

    def button_on_click(self, id_word_set):
        regex = '^[0-9]+$'
        id_word_set_int = int(id_word_set)
        if id_word_set_int >= len(self.word_set_list) or id_word_set_int < 0 or re.match(regex, id_word_set) is None:
            messagebox.showerror("Wrong id", "The id you passed is incorrect")
        else:
            self.window.destroy()
            ChooseMode(id_word_set, self.user)

    def set_window(self):
        self.word_set_list = Database.get_all_wordsets(self.user.id_User)
        treeview = ttk.Treeview(self.window, columns=("Index", "Theme"), show="headings")
        treeview.pack()

        treeview.heading("#1", text="Index")
        treeview.heading("#2", text="Theme")

        for row in self.word_set_list:
            treeview.insert("", tkinter.END, values=row)

        idx_label = tkinter.Label(self.window, text="Select Word Set's id")
        idx_label.pack()
        idx_input = tkinter.Entry(self.window)
        idx_input.pack()
        ok_button = tkinter.Button(self.window, text="OK", command=lambda: self.button_on_click(idx_input.get()))
        ok_button.pack()
        self.window.mainloop()
