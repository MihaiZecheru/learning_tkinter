'''
create a programming directory including python installation and two IDE applications
then runs them in cmd prompt.
Sets up
'''

import os
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser

root = Tk()
root.title("Start Coding in Python")
root.geometry("600x600")

_ = Label(root,
          text="If this window is not responding, let it be.\nThe operation is running in the backround and the window will restore when the operation completes").pack(
    pady=10)
_ = Label(root, text="Progress:").pack()
progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode="determinate")
progress.pack(pady=10)


def open_FE():
    os.startfile("c:/start_python_programming")
    exit = Button(root, text="quit process", command=root.quit)
    exit.pack()


def run():
    start_button = Button(frame, text="Start", command=run, state=DISABLED).grid(row=0, column=0, pady=2)

    _ = Label(root, text="Setting up your coding environment...").pack()

    messagebox.showwarning("IMPORTANT",
                           "Do not exit the application until 'process complete' appears on the app.\n\nPlease note that you will be prompted to grant admin access to 3 applications.\n\nKeep an eye on your taskbar for this, as the program won't continue until access is granted.\n\nThe program will now proceed")

    programming = "start_python_programming"
    directory = "%s" % programming
    parent = "C:/"

    path = os.path.join(parent, directory)
    # sets the path

    os.mkdir(path)
    # creates a directory named 'start_python_programming' at the specified path.

    programming = "start_python_programming/applications"
    directory = "%s" % programming
    parent = "C:/"
    path = os.path.join(parent, directory)
    os.mkdir(path)
    # creates 'applications' directory

    directory1 = "non-IDE_scripts_and_projects_can_go_here"
    parent1 = "C:/start_python_programming"
    path = os.path.join(parent1, directory1)
    os.mkdir(path)
    # create indie dir for scripts

    with open("C:/start_python_programming/READ_ME.txt", "w") as txt:
        script = """!!! I will be addressing what this folder is and what happened when you ran the program. Read to the end. !!!

        Hopefully, you have granted all three applications admin permission and set them up
        If you haven't done this, no worries--you can open them by double clicking on the .exe files in your "start_python_programming" folder

        ------------------------------------------------------------

        The first application installed was Python; by installing the program language, you can now run code directly from the console (cmd prmpt)
        however, that is not reccomended. An important application that was installed is 'pip'. 
        You can open your console and type 'pip install library.py' to install a library that doesn't come with your installation of python
        Converting your .py scripts (python code) to an exe file is as easy as running this command on the console: 'pip install pyinstaller'. 
        To update pyinstaller, do 'pip install --upgrade pyinstaller'
        To convert your script, set the command directory to the script location; if the script is at the destination C:/start_python_programming/script.py
        then run the command 'cd C:/start_python_programming' to set the command directory to C:/start_python_programming
        TO CONVERT TO EXE: run 'pyinstaller --onefile script.py' at the command directory where your script.py is located
        wait for the console to complete the operation and you'll have your file in a directory (folder) named 'dir'



        The second application installed was PyCharm. This is an IDE, a place where you can write your code.
        It is highly reccomended you watch the video 'Learn Python - Full Course for Beginners [Tutorial]' by FreeCodeCamp.org on youtube
        (https://youtu.be/rfscVS0vtbw)
        and write out the code that the guy in the video is doing it, and write comments that explain what is being written. This can later be used as notes



        The final application installed was Sublime Text Editor. This is a text editor that many use to write their code; it's an IDE and substitute for notepad.
        You can use this to run your code. Check the bottom right corner for a button that reads "Plain text".
        Click this, and change it to 'python' (located right underneath the highlighted option)
        Now you can write your code. Once you're done, title it (in this case we'll call it 'script.py')
        And then copy the file path of the code (let's say our file path is 'C:/programming/script.py'. Open command line (console) and type 'python C:/programming/script.py'

        ------------------------------------------------------------

        While you now have 2 IDE's installed where you can write your code, programs can also be written in a plain text file (txt).
        The 'non-IDE_scripts_and_projects_can_go_here' directory (folder)
        in your 'C:/start_python_programming' directory is meant for you to save .py files (text files with python script in them)
        You can also save your sublime code in this directory.

        ------------------------------------------------------------

        Feel free to change the name of all the directories made by the application. You probably should, considering the inpracticality of the names.
        Ideas: rename 'start_python_programming' to 'programming', and rename 'non-IDE_scripts_and_projects_can_go_here' to 'scripts'
        
        Final note: the 'applications' directory has the .exe files that were installed.
        """
        txt.write(script)
    # create info.txt file

    progress['value'] = 10
    root.update_idletasks()
    _ = Label(root, text="directories created...").pack()

    download_python = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
    req = requests.get(download_python, allow_redirects=True)
    open("C:/%s/python.exe" % programming, "wb").write(req.content)
    # download python.exe

    progress['value'] = 30
    root.update_idletasks()
    _ = Label(root, text="python.exe downloaded...").pack()

    download_pycharm = "https://download.jetbrains.com/python/pycharm-professional-2021.2.3.exe"
    req = requests.get(download_pycharm, allow_redirects=True)
    open("C:/%s/pycharm.exe" % programming, "wb").write(req.content)
    # download pycharm

    progress['value'] = 70
    root.update_idletasks()
    _ = Label(root, text="pycharm.exe downloaded...").pack()

    download_sublime = "https://download.sublimetext.com/sublime_text_build_4121_x64_setup.exe"
    req = requests.get(download_sublime, allow_redirects=True)
    open("C:/%s/sublime.exe" % programming, "wb").write(req.content)
    # download sublime4

    progress['value'] = 100
    root.update_idletasks()
    _ = Label(root, text="sublime.exe downloaded...\n\nProcess finished succesfully.").pack()
    # downloading complete

    path = "C:/%s/sublime.exe" % programming
    os.system(path)
    # runs sublime.exe file

    path = "C:/%s/python.exe" % programming
    os.system(path)
    # runs python.exe file

    path = "C:/%s/pycharm.exe" % programming
    os.system(path)
    # runs pycharm.exe file

    open_file_explorer = Button(root, text="Open File Location", command=open_FE)
    open_file_explorer.pack(pady=50)

    ans = messagebox.askokcancel("You're good to go!",
                                 "Everything has downloaded succesfully and you're ready to start coding.\n\nI'd reccomend watching this video to get started:\n'Learn Python - Full Course for Beginners' by 'FreeCodeCamp.org'\n\nPress 'ok' to go to the video.")

    if ans == 1:
        webbrowser.open("https://www.youtube.com/watch?v=rfscVS0vtbw")

frame = LabelFrame(root)
frame.pack()

start_button = Button(frame, text="Start", command=run, state=NORMAL).grid(row=0, column=0, pady=2)

root.mainloop()
