import tkinter
from tkinter import messagebox
from Classes.LogIn import LogIn
from GUI.GameWindow import GameWindow


class LoginWindow:

    def __init__(self, welcome):
        self.window = tkinter.Tk()
        self.welcome = welcome
        self.login_set()

    def button_on_click(self, login_value, password_value):
        answer = LogIn.login_logic(login_value, password_value)
        if "wrong login" == answer:
            messagebox.showerror("wrong login", "Login does not exists in database")
        elif "wrong password" == answer:
            messagebox.showerror("wrong password", "You have entered a wrong password")
        else:
            self.window.destroy()
            self.welcome.destroy()
            GameWindow(answer)

    def login_set(self):
        self.window.title("Log in")
        label_login = tkinter.Label(self.window, text="login")
        label_login.pack()
        input_login = tkinter.Entry(self.window)
        input_login.pack()
        label_password = tkinter.Label(self.window, text="password")
        label_password.pack()
        input_password = tkinter.Entry(self.window, show="*")
        input_password.pack()
        button_login = tkinter.Button(self.window, text="Log in",
                                      command=lambda: self.button_on_click(input_login.get(), input_password.get()))
        button_login.pack()
        self.window.mainloop()
