import tkinter


class Game:
    def __init__(self, id_wordset, user, mode):
        self.id_wordset = id_wordset
        self.user = user
        self.mode = mode
        self.window = tkinter.Tk()
        self.window.title("Crossword")
