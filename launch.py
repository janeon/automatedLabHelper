# tkinter tutorial https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import *
from subprocess import *
import os

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
def install():
    #os.system("python3 installation.py")
    os.system("virtualenv -p python3 virtual 1> /dev/null")
    os.system("/bin/bash  --rcfile virtual/bin/activate 1> /dev/null")
    os.system("pip3 install pylint")
    os.system("pip3 install beautifulsoup4")

master = Tk()
master.title('Lab Helper Launcher')
w = Canvas(master, width=50, height=100)
w.pack()
text = "Hi,I'm the launcher window for the lab helper. \n\nPlease keep me open along with the lab helper's main interface (even if I seem to be indeterminately loading). \n\nAfter setting up your virtual environment by clicking the launch button below, run \'python3 helper.py\'.\n\nTo close me, run \'exit+ENTER\'"
T = Text(master, height=10, width=110)
T.insert(END,text)
T.pack()



button = Button(master, text="LAUNCH", command=combine_funcs(install,master.destroy))
button.pack()


mainloop()
