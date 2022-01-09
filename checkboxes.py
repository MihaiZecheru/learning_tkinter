# Checkboxes
# main.py

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CheckBoxes")

var = IntVar()
# creates a tkinter variable--"intvar"

def on_button_press1():
    _ = Label(root, text=string_var.get()).pack()


def on_button_press():
    _ = Label(root, text=var.get()).pack()


c = Checkbutton(root, text="Click me!", variable=var, command=on_button_press)
c.pack()

string_var = StringVar()
string_var.set("Box unchecked")

c1 = Checkbutton(root, text="Click me too", variable=string_var, onvalue="You checked this box",
                 offvalue="Box unchecked", command=on_button_press1)
c1.pack()
# 'string_var.set("Box unchecked")' sets the value of the string_var variable to 'Box unchecked'
# this is an easy workaround the glitch where the checkbox starts off checked

# another workaround to this glitch is to use c1.deselect()
# this will uncheck the checkbox


root.mainloop()
