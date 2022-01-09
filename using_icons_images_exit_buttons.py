# Using Icons, Images, and Exit Buttons
# main.py

from tkinter import *
from PIL import ImageTk, Image
# pillow module (PIL) is needed because tkinter only supports .gif files.
# This module will circumvent that

root = Tk()
root.title("Icons, Images, and Exit Buttons")

root.iconbitmap("cookie.ico")
# adding an icon next to the title

my_image = ImageTk.PhotoImage(Image.open("cookie.png").resize((300, 300)))
my_label = Label(image=my_image).pack()
# image.resize(()) will resize the image to the dimensions in the tuple
# works with pillow module

quit_button = Button(root, text="Exit Program", command=root.quit).pack()
# when this button is pressed, the program will close

root.mainloop()
