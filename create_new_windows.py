# Create New Windows in Tkinter
# main.py

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Creating New Windows in Tkinter")


def open_window():
    top = Toplevel()
    # creates a new window
    top.title("New Window")
    # titles the top window 'New Window'

    _ = Label(top, text="Hello World").pack()
    # adds this label to the new window named top

    global image
    # this is an important step; you have to make the image a global variable!!

    image = ImageTk.PhotoImage(Image.open("cookie.png"))
    image_label = Label(top, image=image).pack()
    # adds the cookie.png to the 'top' window

    _ = Button(top, text="Exit Window", command=top.destroy).pack()
    # window.destroy() is a tkinter func that will close a window.
    # in this case, we're closing the new window that we made.

image1 = ImageTk.PhotoImage(Image.open("Chrissy.PNG"))
image_label1 = Label(root, image=image1).pack()

button_that_opens_the_new_window = Button(root, text="Open New Window", command=open_window)
button_that_opens_the_new_window.pack()

root.mainloop()
