'''
Databases in tkinter
using sqlite
main.py
'''

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases")
root.geometry("360x500")

# create a database or connect to a database
# both creating or connecting to a database uses the same command
connection = sqlite3.connect("address_book.db")
# since this file does not exist yet, it will create it in whatever directory we're already in

"""
a cursor is the thing you send off to do things with the database
whenever you want to execute any sort of command, the cursor will do that
"""
# Create Cursor
cursor = connection.cursor()

'''
we have the cursor and the database, now we want to create a table
a table is like a spreadsheet. It has rows and columns, we now just need to create a table and
designate those rows and columns
'''
# create the table:
'''
cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
I commented out this table because I only want to create the table once.
'''
'''
creates a tables named 'addresses'.
sqlite only has 5 datatypes: 
text, integers, real (decimal numbers), null (doesn't exist), blob (image files, video files, etc)
'''


# delete a record function
def delete():
    if delete_box.get() not in ["", "Select an ID first"]:
        # we need to connect to the db and a cursor when we're inside a function
        connection = sqlite3.connect("address_book.db")
        cursor = connection.cursor()

        cursor.execute("DELETE from addresses WHERE oid= " + delete_box.get())

        '''
        IMPORTANT NOTE: 'oid=delete_box.get()' won't work. 
        You gotta concatenate 'delete_box.get()' to an empty string
        We add a space before the end quote so that oid="" before we concatenate delete_box.get()

        cursor command; from the addresses db, delete anything where the oid=
        we could also write:
        cursor.execute("DELETE from addresses WHERE first_name="Chris")
        this would delete anybody with the first name Chris from the addresses db
        '''

        connection.commit()
        connection.close()
    else:
        delete_box.delete(0, END)
        delete_box.insert(0, "Select an ID first")


def update():
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()

    record_id = delete_box.get()

    cursor.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid= :oid""",
                   {
                       'first': first_name_editor.get(),
                       'last': last_name_editor.get(),
                       'address': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'zipcode': zipcode_editor.get(),
                       'oid': record_id
                   })
    # update the addressed db with the values below, where the oid= the oid we set.
    # the second arg just replaced the first name, last name, address, city, state, zip, with the dictionary values

    connection.commit()
    connection.close()

    editor.destroy()
    delete_box.delete(0, END)


# Creating an edit function to update the record
def edit():
    if delete_box.get() not in ["", "Select an ID first"]:
        global editor
        editor = Tk()
        editor.title("Update Records")
        editor.geometry("400x400")

        record_id = delete_box.get()
        # we made the 'delete_box' be a select ID box instead.
        # this stores the oid of the data the user requested in the variable 'record_id'

        # we need to connect to the db and a cursor when we're inside a function
        connection = sqlite3.connect("address_book.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM addresses WHERE oid= " + record_id)

        records = cursor.fetchall()

        # Creating globals
        global first_name_editor
        global last_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        # creating the text boxes
        first_name_editor = Entry(editor, width=30)
        first_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        last_name_editor = Entry(editor, width=30)
        last_name_editor.grid(row=1, column=1)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1)

        # creating the text box labels
        first_name_label_editor = Label(editor, text="First Name")
        first_name_label_editor.grid(row=0, column=0, pady=(10, 0))
        last_name_label_editor = Label(editor, text="Last Name")
        last_name_label_editor.grid(row=1, column=0)
        address_label_editor = Label(editor, text="Address")
        address_label_editor.grid(row=2, column=0)
        city_label_editor = Label(editor, text="City")
        city_label_editor.grid(row=3, column=0)
        state_label_editor = Label(editor, text="State")
        state_label_editor.grid(row=4, column=0)
        zipcode_label_editor = Label(editor, text="Zipcode")
        zipcode_label_editor.grid(row=5, column=0)

        # Creating a save button for the editor window
        update_button = Button(editor, text="Update Record", command=update)
        update_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

        for record in records:
            first_name_editor.insert(0, record[0])
            last_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[0])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        connection.commit()
        connection.close()
    else:
        delete_box.delete(0, END)
        delete_box.insert(0, "Select an ID first")


def submit():
    if first_name.get() != "" or last_name.get() != "" or address.get() != "" or city.get() != "" or state.get() != "" or zipcode.get() != "":
        # we need to connect to the db and a cursor when we're inside a function
        connection = sqlite3.connect("address_book.db")
        cursor = connection.cursor()

        # Insert into table
        cursor.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
                       {
                           "first_name": first_name.get(),
                           "last_name": last_name.get(),
                           "address": address.get(),
                           "city": city.get(),
                           "state": state.get(),
                           "zipcode": zipcode.get()
                       })

        connection.commit()
        connection.close()

        # Clear the text boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)


# Creating query function
def query():  # sourcery skip: use-join
    # we need to connect to the db and a cursor when we're inside a function
    connection = sqlite3.connect("address_book.db")
    cursor = connection.cursor()

    cursor.execute("SELECT *, oid FROM addresses")
    # oid is the specific record id.
    # we wouldn't want to remove all of John Elder from the db because there could be multiple John Elders
    records = cursor.fetchall()

    # 'print(records)'
    # prints: [('Chris', 'Zecheru', '4734 Millard St', 'Moorpark', 'California', 93021, 1)]
    # the final value of the tuple is 1 because it's the first oid

    # these two lines select everything under every (because of the *) oid, and then fetches it

    # NOTE: The oid is the '1' or '2' or '3' (etc) at the end of the tuple of records

    # loop through results
    print_records = ""
    for record in records:
        # if record not in [i for i in range(100)]:
        #    - this 'if' statement would prevent the final element, the oid, from being printed

        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
        # prints the specified values

        # NOTE: I can make this print the entire tuple from the db[oid]
        # by changing the above statement to:
        # print_records += str(record) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    connection.commit()
    connection.close()


# creating the text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
# NOTE: pady=() <-- tuple
# you can put a tuple into the arg of pad to modify only one side
# in this case, we're only modifying the top by 10
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, pady=5)

# creating the text box labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10, 0))
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID:")
delete_box_label.grid(row=10, column=0, pady=5)

# creating the submission button
submit_button = Button(root, text="Add Record to Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Creating a query button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Creating a delete button
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Creating an Update button
update_button = Button(root, text="Edit Record", command=edit)
update_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

connection.commit()
# anytime we make a change in the database, we want to commit those changes to the database

connection.close()
# close the connection


root.mainloop()
