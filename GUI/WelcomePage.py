import tkinter
import tkinter as tk
from LogInWindow import LoginWindow

text = "CROSSWORD GAME"
delay = 0.01
step = 2

window = tk.Tk()
window.title("CROSSWORD")
window.geometry("400x400")
canvas = tk.Canvas(window, width=400, height=100)
canvas.pack()


def on_login_button():
    return LoginWindow()


login_button = tkinter.Button(window, text="Log in", command=on_login_button)
login_button.pack()

x = 20
y = 70
velocity = step


def animate_letters():
    global x, y, velocity

    canvas.delete("text")
    canvas.create_text(x, y, text=text, font=("Pacific", 35), tags="text")
    x += velocity

    if x <= 20:
        velocity = abs(velocity)
    elif x >= 380:
        velocity = -abs(velocity)

    if x == 200:
        velocity = 0

    if velocity != 0:
        window.after(int(delay * 1000), animate_letters)


animate_letters()

window.mainloop()
