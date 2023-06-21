import tkinter
from Classes.LogIn import LogIn
from tkinter import messagebox
from GUI.GameWindow import GameWindow


class RegisterWindow:

    def __init__(self, welcome):
        self.window = tkinter.Tk()
        window_height = 220
        window_width = 200
        screen_width = self.window.winfo_width()
        screen_height = self.window.winfo_height()
        x_coordinate = int((screen_width / 2) + (window_width * 2) + 195)
        y_coordinate = int((screen_height / 2) + (window_height / 2) + 200)
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
        self.welcome = welcome
        self.register_set()

    def register_set(self):
        self.window.title("Register")
        label_login = tkinter.Label(self.window, text="login")
        label_login.pack()
        input_login = tkinter.Entry(self.window)
        input_login.pack()
        label_password = tkinter.Label(self.window, text="password")
        label_password.pack()
        input_password = tkinter.Entry(self.window, show="*")
        input_password.pack()
        label_password_repeat = tkinter.Label(self.window, text="repeat password")
        label_password_repeat.pack()
        input_password_repeat = tkinter.Entry(self.window, show="*")
        input_password_repeat.pack()
        button_login = tkinter.Button(self.window, text="Register",
                                      command=lambda: self.button_on_click(input_login.get(), input_password.get(), input_password_repeat.get()))
        button_login.pack()
        self.window.mainloop()

    def button_on_click(self, login, password, repeat_password):
        answer = LogIn.register_logic(login, password)
        if answer == "login already exists":
            messagebox.showerror("wrong login", "Login does already exist in database")
        elif password != repeat_password:
            messagebox.showerror("password", "Passwords are not the same")
        elif answer == "wrong password":
            messagebox.showerror("wrong password",
                                 "Password should be at least 8 characters long, "
                                 "at least one big letter, one number, one special sign")
        else:
            self.window.destroy()
            self.welcome.destroy()
            GameWindow(answer)

