import tkinter
from Classes.WordSet import WordSet
from Classes.Database import Database


def close_window(window):
    window.destroy()


class AddWordSet:
    def __init__(self, words_list, user):
        self.user = user
        self.words_list = words_list
        self.set_adding()

    def set_adding(self):
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

    def insert_word_set(self, main_password, main_theme, window):
        word_set = WordSet(self.words_list, main_password, main_theme, -1, self.user.id_User)
        Database.insert_wordset(word_set)
        label = tkinter.Label(window, text="Word Set added")
        label.pack()
        button = tkinter.Button(window, text="OK", command=lambda: close_window(window))
        button.pack()
