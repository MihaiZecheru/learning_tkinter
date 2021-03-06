# Image Viewer App With Tkinter
# main.py

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Beach Pictures")
root.iconbitmap(os.path.join("images", "umbrella.ico"))
# os.path.join(dir, img) to get the image
# root.iconbitmap("images/umbrella.ico") also works

img1 = ImageTk.PhotoImage(Image.open("images/beach.png"))
img2 = ImageTk.PhotoImage(Image.open("images/umbrella_beach.png"))
img3 = ImageTk.PhotoImage(Image.open("images/wave.png"))
img4 = ImageTk.PhotoImage(Image.open("images/ocean_surface.png"))
img5 = ImageTk.PhotoImage(Image.open("images/kid_with_fish.png"))

images = [img1, img2, img3, img4, img5]

status = Label(root, text="Image 1 of " + str(len(images)), bd=5, relief=SUNKEN)
# bd is a border
status.grid(row=2, column=0, columnspan=3)
# sticky is used for stretching in a direction. W+E means West to East

img_label = Label(image=img1)
img_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global img_label
    global forward_button
    global back_button

    img_label.grid_forget()

    img_label = Label(image=images[image_num - 1])
    forward_button = Button(root, text=">>", command=lambda: forward(image_num + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_num - 1))

    if image_num == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    img_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(images)), bd=5, relief=SUNKEN)
    # bd is a border
    status.grid(row=2, column=0, columnspan=3)
    # sticky is used for stretching in a direction. W+E means West to East
def back(image_num):
    global img_label
    global forward_button
    global back_button

    img_label.grid_forget()

    img_label = Label(image=images[image_num - 1])
    forward_button = Button(root, text=">>", command=lambda: forward(image_num + 1))
    back_button = Button(root, text="<<", command=lambda: back(image_num - 1))

    if image_num == 1:
        back_button =  Button(root, text="<<", state=DISABLED)

    img_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)
    status = Label(root, text="Image " + str(image_num) + " of " + str(len(images)), bd=5, relief=SUNKEN)
    # bd is a border
    status.grid(row=2, column=0, columnspan=3)
    # sticky is used for stretching in a direction. W+E means West to East



back_button = Button(root, text="<<", command=back, state=DISABLED)
back_button.grid(row=1, column=0)
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.grid(row=1, column=1)
forward_button = Button(root, text=">>", pady=10, command=lambda: forward(2))
forward_button.grid(row=1, column=2)

root.mainloop()
