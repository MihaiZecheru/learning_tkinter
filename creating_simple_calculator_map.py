# Creating a Simple Calculator App
# main.py

from tkinter import *

root = Tk()
root.title("Simple Calculator")
# titles the window

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)
# the entry will span 3 columns

operation = []


def button_click(number):
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))


def button_clear():
    e.delete(0, END)
    for _ in range(len(operation)):
        operation.pop()


def button_add():
    first_number = e.get()
    global num
    global math
    math = "+"
    num = str(first_number)
    operation.append(num)
    operation.append(math)
    e.delete(0, END)


def button_equals():
    last_num = e.get()
    operation.append(last_num)
    evaluation = "".join(operation)
    print(evaluation)
    answer = eval(evaluation)
    e.delete(0, END)
    e.insert(0, f"{evaluation} = {answer}")
    for _ in range(len(operation)):
        operation.pop()


def button_subtract():
    first_number = e.get()
    global num
    global math
    math = "-"
    num = str(first_number)
    operation.append(num)
    operation.append(math)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global num
    global math
    math = "*"
    num = str(first_number)
    operation.append(num)
    operation.append(math)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global num
    global math
    math = "/"
    num = str(first_number)
    operation.append(num)
    operation.append(math)
    e.delete(0, END)


# defines a bunch of button widgets
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="gray", fg="white", padx=40, pady=20, command=lambda: button_click(0))
# lambda: is what is used to allow the 'command=' to have a () in the function that it calls.
# without it, we cannot pass a parameter to the command!

addition_button = Button(root, text="+", bg="gray", fg="white", padx=39, pady=20, command=lambda: button_add())
equals_button = Button(root, text="=", bg="gray", fg="white", padx=95, pady=20, command=lambda: button_equals())
clear_button = Button(root, text="Clear", bg="gray", fg="white", padx=85, pady=20, command=lambda: button_clear())

button_subtraction = Button(root, text="-", bg="gray", fg="white", padx=41, pady=20, command=lambda: button_subtract())
button_multiplication = Button(root, text="*", bg="gray", fg="white", padx=50, pady=20,
                               command=lambda: button_multiply())
button_division = Button(root, text="/", padx=41, pady=20, bg="gray", fg="white", command=lambda: button_divide())

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

clear_button.grid(row=4, column=1, columnspan=2)
addition_button.grid(row=5, column=0)
equals_button.grid(row=5, column=1, columnspan=2)

button_subtraction.grid(row=6, column=0)
button_multiplication.grid(row=6, column=1)
button_division.grid(row=6, column=2)

root.mainloop()
