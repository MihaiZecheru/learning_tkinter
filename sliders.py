# Sliders
# main.py

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.geometry("400x400")
# root.geometry() sets the screen size.
# in this case it's 400x400 pixels


def slide(x):
    a_label = Label(root, text=horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x{verticle.get()}")
    # when the button is pressed, the screen size will be changed to the value in the sliders


verticle = Scale(root, from_=0, to=400)
# the "from_=" argument must have the underscore
# 'Scale' is a GUI slider, as is seen on most websites.
# The default slider type is verticle.
# If you want a horizontal slider you must specify with orient=HORIZONTAL
verticle.pack()

# make sure to pack the slider on its own line.


horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
# you can also add the command onto a slide widget.
horizontal.pack()

a_label = Label(root, text=horizontal.get()).pack()

a_button = Button(root, text="Click Me", command=slide).pack()

root.mainloop()
