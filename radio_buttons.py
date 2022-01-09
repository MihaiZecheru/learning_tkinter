# Radio Buttons
# main.py

# Goal: creating a menu for a pizza place online
# and we want users to select the type of topping they want on their pizza

from tkinter import *
from PIL import ImageTk, Image

# Radio Buttons are the option/choice circular buttons usually seen in forms.

root = Tk()
root.title("insert title")

order = LabelFrame(root, text="Your Order:", padx=5, pady=5)
order.pack()

r = IntVar()
# returns the value of a variable as an integer
r.set("2")
# makes r = "2"

toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Olives", "Olives"),
]
# makes a list with all four values being tuples.
# the first value is text, and the second one is mode (in each indv tuple)
# (text, mode)

pizza = StringVar()
pizza.set("Pepperoni")

label = Label(order, text=pizza.get())
label.grid(row=1, column=0)

for text, mode in toppings:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()


def clicked(value):
    _ = Label(order, text=value).grid(row=1, column=0)


# Radiobutton(root, text="option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option3", variable=r, value=3, command=lambda: clicked(r.get())).pack()
# Assigns a variable to each of the buttons.
# So then we know when someone clicks on the button that gets put in to the variable
# NOTE: tkinter has its own form of variables.
# they are different from basic python variables.


button = Button(order, text="Place Order", command=lambda: clicked(pizza.get()))
button.grid(row=0, column=0)

root.mainloop()
