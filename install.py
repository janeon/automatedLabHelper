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

master = Tk()
master.title('Lab Helper Launcher')
w = Canvas(master, width=50, height=90)
w.pack()
text = "Hi,I'm the launcher window for the lab helper. \n\nI will remain open along with the lab helper's main interface. \n\nAfter clicking launch type \'python3 interface.py\' into terminal to run lab helper.\n\nTo close me, type \'exit\' on your command line interface (terminal window)"
T = Text(master, height=10, width=100) 
T.insert(END,text)
T.pack() 



button = Button(master, text="LAUNCH", command=combine_funcs(install,master.destroy))
button.pack()


mainloop()
