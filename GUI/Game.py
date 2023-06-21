import tkinter
import random
from tkinter import messagebox
from Classes.Database import Database
from Classes.WordSet import WordSet
from Classes.Word import Word
from GUI.GuessPassword import GuessPassword


class Game:
    def __init__(self, id_wordset, user, mode):
        self.id_wordset = id_wordset
        wordset_data = Database.get_wordset_by_id(id_wordset)
        word = Database.get_words_from_wordset_by_id(id_wordset)
        self.words = list()
        for wrd in word:
            wrdd = Word(wrd[0], wrd[1], wrd[2])
            self.words.append(wrdd)
        self.wordset = WordSet(self.words, wordset_data[1], wordset_data[2])
        self.user = user
        self.mode = mode
        self.wrong_guesses = 0
        self.game_points = 0
        self.seconds = 60
        self.window = tkinter.Tk()
        self.window.title("Crossword")
        self.canvas = tkinter.Canvas(self.window)
        max_lenght_left = max(word.key_index for word in self.words) + 1
        max_lenght_right = max(len(word.entry) for word in self.words) - min(word.key_index for word in self.words) - 1
        self.grid_size = max_lenght_right + max_lenght_left + 1
        self.grid_center = self.grid_size // 2
        self.points_label = tkinter.Label(self.window, text=f"{self.game_points} points")
        self.set_window()

    def set_window(self):
        if self.mode == 'standard':
            self.standard()
        elif self.mode == 'race_the_time':
            self.race()
        elif self.mode == 'first_mistake':
            self.first()

    def button_check_entry(self, id_entry, value, canvas):
        if self.words[int(id_entry)].entry != value.upper():
            print(f'{self.words[int(id_entry)].entry} != {value}')
            self.wrong_guesses += 1
            if self.mode == 'first_mistake':
                self.end_game()
            messagebox.showerror("Try Again", "wrong guess")
        else:
            self.game_points += len(self.words[int(id_entry)].entry)*2
            word_list = list(self.words[int(id_entry)].entry)
            password_label = tkinter.Label(canvas, text=f"[ {word_list[self.words[int(id_entry)].key_index]} ]")
            password_label.config(fg="red")
            password_label.grid(row=id_entry, column=self.grid_center)
            counter = 0
            for j in range(self.grid_center - self.words[int(id_entry)].key_index - 1, self.grid_center - 1):
                label_nor = tkinter.Label(canvas, text=f"[ {word_list[counter]} ]")
                counter += 1
                label_nor.grid(row=id_entry, column=j)
            counter = self.words[int(id_entry)].key_index + 1
            for j in range(self.grid_center + 1,
                           self.grid_center + (len(self.words[int(id_entry)].entry) -
                                               self.words[int(id_entry)].key_index)):
                label_nor = tkinter.Label(canvas, text=f"[ {word_list[counter]} ]")
                counter += 1
                label_nor.grid(row=id_entry, column=j)
            self.points_label.config(text=f'{self.game_points} points')

    def configure_window(self):
        self.points_label.pack()
        self.canvas.pack()
        for i in range(len(self.words)):
            number_label = tkinter.Label(self.canvas, text=f"{i}. ")
            number_label.grid(row=i, column=0)
            label = tkinter.Label(self.canvas, text="[ _ ]")
            label.config(fg="red")
            label.grid(row=i, column=self.grid_center)
            for j in range(self.grid_center - self.words[i].key_index - 1, self.grid_center - 1):
                label_nor = tkinter.Label(self.canvas, text="[ _ ]")
                label_nor.grid(row=i, column=j)
            for j in range(self.grid_center + 1,
                           self.grid_center + (len(self.words[i].entry) - self.words[i].key_index)):
                label_nor = tkinter.Label(self.canvas, text="[ _ ]")
                label_nor.grid(row=i, column=j)
        for i in range(len(self.words)):
            clue_label = tkinter.Label(self.window, text=f'{i}. {self.words[i].clue}')
            clue_label.pack()
        id_label = tkinter.Label(self.window, text="Which password would you like to guess? (id)")
        id_label.pack()
        id_input = tkinter.Entry(self.window)
        id_input.pack()
        guess_label = tkinter.Label(self.window, text="Enter your guess")
        guess_label.pack()
        guess_input = tkinter.Entry(self.window)
        guess_input.pack()
        button_ok = tkinter.Button(self.window, text="OK",
                                   command=lambda: self.button_check_entry(id_input.get(),
                                                                           guess_input.get(), self.canvas))
        button_ok.pack()
        button_password = tkinter.Button(self.window, text="Guess the password", command=self.guess_password)
        button_password.pack()
        hint_button = tkinter.Button(self.window, text="Hint", command=self.get_hint_new_window)
        hint_button.pack()

    def standard(self):
        header_label = tkinter.Label(self.window, text="Standard mode", font=("Arial", 25))
        header_label.pack()
        self.configure_window()

    def race(self):
        header_label = tkinter.Label(self.window, text="First letter of each mode", font=("Arial", 25))
        header_label.pack()
        self.configure_window()
        for i in range(len(self.words)):
            words_list = list(self.words[i].entry)
            label_nor = tkinter.Label(self.canvas, text=f"[ {words_list[0]} ]")
            if self.words[i].key_index == 0:
                label_nor.config(fg="red")
                label_nor.grid(row=i, column=self.grid_center)
            else:
                label_nor.grid(row=i, column=self.grid_center - self.words[i].key_index - 1)

    def first(self):
        header_label = tkinter.Label(self.window, text="First mistake mode", font=("Arial", 25))
        header_label.pack()
        self.configure_window()

    def guess_password(self, value):
        GuessPassword(self.wordset.main_answer, value, self.game_points, self.user, self.wrong_guesses, self.window)

    def end_game(self):
        messagebox.showinfo("The End", f"You have earned {self.game_points} points.")
        self.window.destroy()

    def get_hint(self, row_value):
        if self.game_points < 20:
            messagebox.showinfo("Can't buy hint", "You don't have enough (20) points to buy a hint")
        else:
            random_column = random.randint(0, len(self.words[row_value].entry))
            letter_list = list(self.words[row_value].entry)
            hint_letter = letter_list[random_column]
            hint_label = tkinter.Label(self.canvas, text=f"[ {hint_letter} ]")
            if self.words[row_value].key_index == 0:
                hint_label.config(fg="red")
            random_column += self.grid_center
            hint_label.grid(row=row_value, column=random_column)
            self.game_points -= 20
            self.points_label.config(text=f"{self.game_points} points")

    def close_hint_row(self, new_window, value):
        if value >= len(self.words):
            messagebox.showerror("Wrong index", "Index out of bounds")
        else:
            self.get_hint(value)
            new_window.destroy()

    def get_hint_new_window(self):
        new_window = tkinter.Tk()
        new_window.title("Hint")
        input_label = tkinter.Label(new_window, text="In which row would you like to get a hint?")
        input_label.pack()
        input_input = tkinter.Entry(new_window)
        input_input.pack()
        button_ok = tkinter.Button(new_window, text="OK",
                                   command=lambda: self.close_hint_row(new_window, int(input_input.get())))
        button_ok.pack()
