import tkinter
from GUI.Game import Game


class ChooseMode:
    def __init__(self, id_wordset, user):
        self.id_wordset = id_wordset
        self.window = tkinter.Tk()
        self.window.title("Choose Mode")
        self.user = user

    def set_window(self):
        label = tkinter.Label(self.window, text="Choose mode")
        button_standard = tkinter.Button(self.window, text="Standard", command=self.standard_mode)
        button_race_the_time = tkinter.Button(self.window, text="Race the time", command=self.race_mode)
        button_first_mistake = tkinter.Button(self.window, text="First Mistake", command=self.first_mistake_mode)
        label.pack()
        button_standard.pack()
        button_race_the_time.pack()
        button_first_mistake.pack()

    def standard_mode(self):
        self.window.destroy()
        Game(self.id_wordset, self.user, 'standard')

    def race_mode(self):
        self.window.destroy()
        Game(self.id_wordset, self.user, 'race_the_time')

    def first_mistake_mode(self):
        self.window.destroy()
        Game(self.id_wordset, self.user, 'first_mistake')
