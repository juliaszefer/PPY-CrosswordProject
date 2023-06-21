import tkinter
import re
from tkinter import messagebox
from Classes.Word import Word
from Classes.WordSet import WordSet
from Classes.Database import Database


def close_window(window):
    window.destroy()


class AddNewWordSetView:
    def __init__(self, value, user):
        self.value = value
        self.counter = 1
        self.word_list = list()
        self.user = user
        self.set_window()

    def check_input(self, index, word, clue, new_window):
        counter = 0
        regex = '^[0-9]+$'
        index_int = int(index)
        tmp_list = list(word)
        for i in range(len(tmp_list)):
            if index_int == i:
                counter += 1
        if counter == 0 or re.match(regex, index) is None:
            messagebox.showerror("Wrong Index", "The index you passed is out of bounds")
        else:
            word_to_add = Word(word, clue, index)
            self.word_list.append(word_to_add)
            messagebox.showinfo("Success", "Word has been added")
            new_window.destroy()
            value_int = int(self.value)
            if self.counter - 1 != value_int:
                self.show_input()

    def show_input(self):
        new_window = tkinter.Tk()
        new_window.title(f'Word #{self.counter}')
        header_label = tkinter.Label(new_window, text=f"Enter #{self.counter} word")
        header_label.pack()
        self.counter += 1
        word_label = tkinter.Label(new_window, text="word")
        word_label.pack()
        word_input = tkinter.Entry(new_window)
        word_input.pack()
        clue_label = tkinter.Label(new_window, text="clue")
        clue_label.pack()
        clue_input = tkinter.Entry(new_window)
        clue_input.pack()
        idx_label = tkinter.Label(new_window, text="index of key, starting from 0")
        idx_label.pack()
        idx_input = tkinter.Entry(new_window)
        idx_input.pack()
        submit_button = tkinter.Button(new_window, text="Add Word",
                                       command=lambda: self.check_input(idx_input.get(),
                                                                        word_input.get(), clue_input.get(), new_window))
        submit_button.pack()
        new_window.mainloop()

    def insert_word_set(self, main_password, main_theme, window):
        word_set = WordSet(self.word_list, main_password, main_theme, self.user.id_User)
        Database.insert_wordset(word_set)
        label = tkinter.Label(window, text="Word Set added")
        label.pack()
        button = tkinter.Button(window, text="OK", command=lambda: close_window(window))
        button.pack()

    def set_window(self):
        self.show_input()
        window = tkinter.Tk()
        window.title('New Word Set')
        main_password_label = tkinter.Label(window, text="Insert main password")
        main_password_label.pack()
        main_password_input = tkinter.Entry(window)
        main_password_input.pack()
        main_theme_label = tkinter.Label(window, text="Insert crossword theme")
        main_theme_label.pack()
        main_theme_input = tkinter.Entry(window)
        main_theme_input.pack()
        accept_button = tkinter.Button(window, text="OK",
                                       command=lambda: self.insert_word_set(main_password_input.get(),
                                                                            main_theme_input.get(), window))
        accept_button.pack()
        window.mainloop()
