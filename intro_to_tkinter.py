# Into to Tkinter
# main.py

from tkinter import *

root = Tk()
# this is the first thing you gotta do when making a kinter program
# in kinter, everything is a widget. This is the root widget

myLabel = Label(root, text="Hello World")
# creates a label; label widget

myLabel.pack()
# takes the myLabel widget and shoves it onto the screen

root.mainloop()
# keeps the program looping


# window can be resized, the buttons at the top work too.
