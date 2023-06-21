import tkinter
import re
from tkinter import messagebox
from GUI.AddNewWordSetView import AddNewWordSetView


class AddNewWordSet:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("New Word Set")
        self.set_add_new_word_set()

    def ok_button_check_value(self, value):
        regex = '^[0-9]+$'
        if re.match(regex, value) is None:
            messagebox.showerror("wrong input", "The value you passed is not a number")
        else:
            self.window.destroy()
            AddNewWordSetView(value)

    def set_add_new_word_set(self):
        how_many_label = tkinter.Label(self.window, text='How many words will there be in your crossword?')
        how_many_label.pack()
        answer_input = tkinter.Entry(self.window)
        answer_input.pack()
        ok_button = tkinter.Button(self.window, text='OK',
                                   command=lambda: self.ok_button_check_value(answer_input.get()))
        ok_button.pack()

