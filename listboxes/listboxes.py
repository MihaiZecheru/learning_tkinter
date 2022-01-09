# listboxes.py
# Basic Listbox
from tkinter import *

root = Tk()
root.title('Listboxes')
root.geometry('400x400')

# create the listbox
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

# Add item to listbox
my_listbox.insert(END, 'Hello')
my_listbox.insert(END, 'World')
# there are two args to listbox.insert; index and string
# index is what position you want to put it in, int or END
# END is the end of the listbox; the bottom

# Add list of items to listbox
my_list = ['One', 'Two', 'Three', 'Four', 'Five', 6, 7]

for value in my_list:
    my_listbox.insert(END, str(value))
    item_label.config(text='')

def delete():
    my_listbox.delete(ANCHOR)
    item_label.config(text='')
    # when something is highlighted in a listbox, it becomes the 'anchor'

def select():
    item_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0, END)

delete_button = Button(root, text='Delete', command=delete).pack(pady=10)

select_button = Button(root, text='Select', command=select).pack(pady=10)

delete_all_button = Button(root, text='Delete All', command=delete_all).pack(pady=10)

# setup the label, allow it to later be changed
item_label = Label(root, text='')
item_label.pack(pady=5)

root.mainloop()
