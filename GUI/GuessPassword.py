import tkinter
from tkinter import messagebox
from Classes.Database import Database


class GuessPassword:
    def __init__(self, password, guess, points, user, wrong_guesses, welcome):
        self.password = password
        self.guess = guess
        self.points = points
        self.user = user
        self.welcome = welcome
        self.wrong_guesses = wrong_guesses
        self.window = tkinter.Tk()
        self.window.title("Guess password")
        self.set_window()

    def check_password(self):
        if self.guess != self.password:
            messagebox.showinfo("Wrong guess", "Try again")
            self.window.destroy()
        else:
            if self.wrong_guesses == 0:
                self.points *= 100
            elif self.wrong_guesses != 0 and self.wrong_guesses <= 2:
                self.points *= 20
            if self.user.login != "Guest":
                Database.update_user_points_by_id(self.user.id_User, self.points)
            messagebox.showinfo("Congratulations!", f"You won with {self.points} points")
            self.window.destroy()
            self.welcome.destroy()

    def set_window(self):
        guess_label = tkinter.Label(self.window, text="Guess password")
        guess_label.pack()
        guess_input = tkinter.Entry(self.window)
        guess_input.pack()
        ok_button = tkinter.Button(self.window, text="OK", command=self.check_password)
        ok_button.pack()

