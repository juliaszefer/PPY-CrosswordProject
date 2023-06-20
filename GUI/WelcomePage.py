import tkinter as tk
from GUI.LogInWindow import LoginWindow
from GUI.RegisterWindow import RegisterWindow


class WelcomePage:
    def __init__(self):
        self.text = "CROSSWORD GAME"
        self.delay = 0.01
        self.step = 2

        self.window = tk.Tk()
        self.window.title("CROSSWORD")
        self.window.geometry("400x400")

        self.canvas = tk.Canvas(self.window, width=400, height=100)
        self.canvas.pack()

        self.login_button = tk.Button(self.window, text="Log in", command=self.on_login_button)
        self.login_button.pack()

        self.register_button = tk.Button(self.window, text="Register", command=self.on_register_button)
        self.register_button.pack()

        self.x = 20
        self.y = 70
        self.velocity = self.step

    def on_login_button(self):
        LoginWindow(self.window)

    def on_register_button(self):
        RegisterWindow(self.window)

    def animate_letters(self):
        self.canvas.delete("text")
        self.canvas.create_text(self.x, self.y, text=self.text, font=("Pacific", 35), tags="text")
        self.x += self.velocity

        if self.x <= 20:
            self.velocity = abs(self.velocity)
        elif self.x >= 380:
            self.velocity = -abs(self.velocity)

        if self.x == 200:
            self.velocity = 0

        if self.velocity != 0:
            self.window.after(int(self.delay * 1000), self.animate_letters)

    def run(self):
        self.animate_letters()
        self.window.mainloop()
