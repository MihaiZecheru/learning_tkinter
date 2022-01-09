# Adding Frames to a Program
# main.py

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("insert title")

frame = LabelFrame(root, text="This is a frame", padx=5, pady=5)
# if you remove the text= in the line above, it will just be a box with no writing above it
frame.pack(padx=10, pady=10)


def cmd():
    _ = Label(frame, text="bruh").grid(row=1, column=0, columnspan=1)
    print("You had one job :|")


b = Button(frame, text="Don't click here!", command=cmd)
b.grid(row=0, column=0)

# typically, in a GUI, you can't use .pack() and .grid() in the same window
# but you can .grid() a widget inside of a frame widget that you did .pack() on
# meaning frames have their own grid system
# BUT: you can't .pack() and .grid() 2 widgets inside of a frame, just like usual.


root.mainloop()
