# Grid System
# main.py

from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My name is Chris Zecheru")

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)
# sets the two label widgets at the above "coordinates"
# grid() is all relative. If column=1 was changed to column=5, you would have the same result
# because there's nothing in column 2, 3, 4, and 5

root.mainloop()
