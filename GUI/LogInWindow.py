import tkinter
from tkinter import messagebox
from Classes.LogIn import LogIn


class LoginWindow:

    def __init__(self):
        self.window = tkinter.Tk()
        login_set(self)


def button_on_click(login_value, password_value):
    if "wrong login" == LogIn.login_logic(login_value, password_value):
        messagebox.showerror("wrong login", "Login does not exists in database")
    elif "wrong password" == LogIn.login_logic(login_value, password_value):
        messagebox.showerror("wrong password", "You have entered a wrong password")


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
    button = tkinter.Button(self.window, text="Log in", command=button_on_click(input_login.get(),
                                                                                input_password.get()))
    button.pack()
    self.window.mainloop()
