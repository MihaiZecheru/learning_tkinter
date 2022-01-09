# Message Boxes
# main.py

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")


def popup():
    response = messagebox.askyesno("This is a popup", "Hello World")
    Label(root, text=response).pack()
    # makes a label with the answer of the user.
    # if the user clicks 'yes', respone = 1. If the user clicks 'no', response = 0.

    # essentially, the response var we made stores the input of the user.
    if response == 1:
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()

    # askokcancel() also returns a '1' or a '0'
    # askquestion() returns 'yes' or 'no'
    # showerror() returns 'ok'
    # showwarning() returns 'ok'
    # showinfo() returns 'ok'

# When the button is pressed, a popup will open up with the name "This is a popup".
# The popup message will contain "Hello World"
# arg1 is popup name, arg2 is the popup info

# If the messagebox.showinfo() is changed to messagebox.showwarning()
# The popup icon will be the warning triangle with the ! on it, instead of the blue circle with the 'i'

# messagebox.showerror() also works; the icon will be changed to a red circle with an 'X' in the middle.

# messagebox.askquestion() will show the question mark in the blue circle symbol.
# on default, it will give 2 buttons, yes and no. These can be customized.

# messagebox.askokcancel() will give 2 buttons; 'ok' and 'cancel'

#IMPORTANT:
# NOTE: messagebox.func() options are:
# showinfo(), showwarning(), showerror(), askquestion(), askokcancel(), askyesno(), askyesnocancel(), askretrtycancel()

Button(root, text="Popup", command=popup).pack()

root.mainloop()
