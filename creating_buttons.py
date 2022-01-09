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




# Creating Buttons cont
# main.py

from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
# makes an user input widget. (small text box)

e.insert(0, "Enter your name:")
# writes "Enter your name:" into the text box created


def myClick():
    myLabel = Label(root, text=f"Hello {e.get()}")
    myLabel.pack()
# prints the box's input when the function is called.
# Entry.get() takes the value entered in the entry

myButton = Button(root, text="Big Button", padx=50, pady=50, command=myClick, fg="blue", bg="black")
myButton.pack()

root.mainloop()
