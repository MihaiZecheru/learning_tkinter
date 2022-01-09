# Open Files Dialog Box
# main.py

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer")

def open():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/Chris/PycharmProjects/toturial/images", title="Select A File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    # initialdir= will be the initial directory you want to show when the box pops up
    # title= will title the box that pops up
    # filetypes=() lists the file types we want to be opened
    # each arg of filetypes=() is a tuple.
    # First value of the tuple is the display name in the file-selection dropdown menu, and the second value is the filetype
    # *.png means open all files that are png.
    # *.* means open all files of all filetypes

    _ = Label(root, text=root.filename).pack()
    # adds a label to the root window, with the label-text being the file path of the image clicked

    global image
    image = ImageTk.PhotoImage(Image.open(root.filename))
    # sets the var 'image' to the image that the user clicked.
    # we get which image the user clicked by opening the image under the filepath the user clicked (root.filename)

    _ = Label(root, image=image).pack()
    # packs the image onto the window




button = Button(root, text="Open File", command=open).pack()

root.mainloop()
