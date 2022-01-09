# Listboxes
# Adding Scrollbar to Listbox
from tkinter import *

root = Tk()
root.title('Listbox with Scrollbar')
root.geometry('400x400')

# add a scrollbar to my_frame
my_frame = LabelFrame(root)
my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)

# create the listbox
my_listbox = Listbox(root, yscrollcommand=my_scrollbar.set)
# on yscroll, command=my_scrollbar.set

'''
another arg to add: selectmode
selectmode on default is single. the ANCHOR will be the only selected thing.
In MULTIPLE mode, left clicking will highlight the item and will be added to the ANCHOR. Multiple may be selected
In EXTENDED mode, interacting with items will be like single mode, however, if you press shift while you click, it will get highlighted like 'MULTIPLE' mode.
EXTENDED mode is like a halfway point between SINGLE and MULTIPLE mode.

The modes are: SINGLE (default), MULTIPLE, BROWSE, EXTENDED
BROWSE is a mode that allows you to move stuff around, but it requires some extra coding.
'''

my_listbox.pack(pady=15)

# configure scrollbar
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()
