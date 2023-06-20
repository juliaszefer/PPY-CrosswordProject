import tkinter
from tkinter import *
from tkinter.ttk import *
from Classes.Database import Database
from Classes.Level import Level


class GameWindow:
    def __init__(self, user):
        self.window = tkinter.Tk()
        self.user = user
        self.set_window()

    def set_window(self):
        self.window.title(f'{self.user.login} view')
        self.window.geometry("800x600")
        user_level = self.get_level()
        min_points_label = tkinter.Label(self.window, text=f"  {user_level.min_points}   ")
        min_points_label.grid(row=0, column=0, pady=10)
        progress = Progressbar(self.window, orient=HORIZONTAL, length=300, mode='determinate')
        progress.grid(row=0, column=1, pady=10)
        progress['value'] = (self.user.points/user_level.max_points)*100
        max_points_label = tkinter.Label(self.window, text=f"   {user_level.max_points}")
        max_points_label.grid(row=0, column=2, pady=10)
        level_name = tkinter.Label(self.window, text=f'\t{user_level.title}')
        level_name.grid(row=0, column=3, pady=10)

    def get_level(self):
        data = Database.get_level_by_id(self.user.id_Level)
        level = Level(data[0], data[1], data[2], data[3])
        return level

