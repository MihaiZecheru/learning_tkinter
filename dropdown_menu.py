# Dropdown Menus
# main.py

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menu")



def show():
    _ = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

clicked = StringVar()
clicked.set(options[0])


# creating the drowdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()
# 'clicked' is a tkinter variable
# the second arg in OptionMenu will run the 'variable=' command

button = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
