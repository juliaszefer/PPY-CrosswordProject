import tkinter
from tkinter import *
from tkinter.ttk import *
from Classes.Database import Database
from Classes.Level import Level
from GUI.Leaderboard import Leaderboard
from GUI.PrizesView import PrizesView
from GUI.AddNewWordSet import AddNewWordSet
from GUI.ChooseWordSet import ChooseWordSet
from Classes.User import User


def open_leaderboard():
    Leaderboard()


class GameWindow:
    def __init__(self, tmp_user):
        self.window = tkinter.Tk()
        self.tmp_user = tmp_user
        Database.update_user_level(self.tmp_user.id_User)
        user_data = Database.get_user(self.tmp_user.login)
        self.user = User(self.tmp_user.login, user_data[0], user_data[2], user_data[1], user_data[3])
        self.set_window()

    def set_window(self):
        self.window.title(f'{self.user.login} view')
        user_level = self.get_level()
        min_points_label = tkinter.Label(self.window, text=f"  {user_level.min_points}   ")
        min_points_label.grid(row=0, column=0, pady=10)
        progress = Progressbar(self.window, orient=HORIZONTAL, length=300, mode='determinate')
        progress.grid(row=0, column=1, pady=10)
        progress['value'] = (self.user.points/user_level.max_points)*100
        max_points_label = tkinter.Label(self.window, text=f"  {user_level.max_points}")
        max_points_label.grid(row=0, column=2, pady=10)
        level_name = tkinter.Label(self.window, text=f'\t{user_level.title}')
        level_name.grid(row=0, column=3, pady=10)
        welcome_label = tkinter.Label(self.window, text=f'\tWelcome {self.user.login}!  ')
        welcome_label.grid(row=0, column=4, pady=10)
        current_points_label = tkinter.Label(self.window, text=f'  Your points: {self.user.points}')
        current_points_label.grid(row=1, column=0)
        play_button = tkinter.Button(self.window, text='Play', command=self.open_choose_word_set)
        play_button.grid(row=2, column=2)
        if self.user.login != 'Guest':
            add_button = tkinter.Button(self.window, text='New word set', command=self.open_add_new_word_set_view)
            add_button.grid(row=3, column=2)
            prizes_button = tkinter.Button(self.window, text='Show prizes', command=self.open_prizes_view)
            prizes_button.grid(row=4, column=2)
        leaderboard_button = tkinter.Button(self.window, text='Leaderboard', command=open_leaderboard)
        leaderboard_button.grid(row=5, column=2)
        log_out_button = tkinter.Button(self.window, text='Log out', command=self.logout)
        log_out_button.grid(row=7, column=2)
        self.window.mainloop()

    def get_level(self):
        data = Database.get_level_by_id(self.user.id_Level)
        level = Level(data[0], data[1], data[2], data[3])
        return level

    def logout(self):
        self.window.destroy()

    def open_prizes_view(self):
        PrizesView(self.user.login)

    def open_add_new_word_set_view(self):
        AddNewWordSet(self.user)

    def open_choose_word_set(self):
        ChooseWordSet(self.user)
