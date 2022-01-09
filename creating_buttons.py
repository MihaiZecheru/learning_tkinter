# Creating Buttons
# main.py

from tkinter import *

root = Tk()

myButton = Button(root, text="Click Me!")
# creates a button; button widget
myButton.pack()

def myClick():
    myLabel = Label(root, text="I clicked a button")
    myLabel.pack()
# "I clicked a button" will be printed on the program when this function is called

myButton1 = Button(root, text="Disabled button", state=DISABLED)
myButton1.pack()
# the button wont be able to be clicked and it will appear grayed out

myButton2 = Button(root, text="Big Button", padx=50, pady=50, command=myClick, fg="blue", bg="black")
myButton2.pack()
# makes a button with the dimensions (50, 50)
# when the button is clicked, it will execute the 'command' arg.
# in this case, the myClick() function will be executed
# remember not to add the () to the end of the command if it is calling a function
# the backround of this button will be black and the color of the text will be blue
# NOTE: the value can be a hex instead of just the color name

root.mainloop()
