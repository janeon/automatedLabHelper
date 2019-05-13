# tkinter tutorial
# https://www.geeksforgeeks.org/python-gui-tkinter/

from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
from subprocess import *
import subprocess
import os

canvas_height=40*15
canvas_width=50*15
output = ""

def load_checkers():
    #https://stackoverflow.com/questions/6943208/activate-a-virtualenv-with-a-python-script#comment73979960_14792407
    #os.system("/bin/bash --rcfile installation.sh")
    #path = "virtual/bin/python3"
    #script = "installation.py"
    #subprocess.Popen([path, script])
    #os.system("python3 installation.py")
    #print("activated env")
    # subprocess.check_call(['./installation.sh'])
    result = check_output(['python3', '--version']).decode("utf-8").split(' ')
    version = result[1][0:3]
    # print("cp -R checkers/* virtual/lib/python"+str(version)+"/site-packages/pylint/checkers/")
    os.system("cp -R checkers/* virtual/lib/python"+str(version)+"/site-packages/pylint/checkers/")
    print("loaded checkers")
    # subprocess.check_call(command.split(' '))

#def openfile():
   #filename = askopenfilename(parent=master)
   #f = open(filename)
   #return f

def load_file():
    fname = askopenfilename(filetypes=[("Python files","*.py")])
    options = getRadioValues()
    command = "python3 cleanOutput.py "+fname+" "+options
    output = check_output(command.split(" ")).decode("utf-8").split('\n')
    fm = Frame(master)
    scrollbar = Scrollbar(fm)
    #T = Text(fm, height=50, width = 100)
    T = Listbox(fm, yscrollcommand = scrollbar.set, width=80, height=50)
    scrollbar.pack( side = RIGHT, fill = Y )
    
    for line in output:
        T.insert(END,'     '+line)
    T.pack(side=LEFT)
    scrollbar.config( command = T.yview )

    button = Button(fm, text="Clear errors", command=fm.destroy)
    button.pack(side=BOTTOM)
    #fm.pack_propagate(0)
    fm.pack(side=LEFT)

def getRadioValues():
    return c.get()+w.get()+e.get()+r.get()+f.get()

master = Tk()
master.title('Automated CS150 Lab Helper')

frm = Frame(master, width=250, height=  650)
frm.pack(side=LEFT)
frm.pack_propagate(0)

buttonl = Button(frm, text="LOAD CUSTOM CHECKERS", command=load_checkers)
buttonl.pack(side=TOP, pady= (20,10))

c = StringVar()
c.set("c") # initialize


CONVENTIONMODES = [
        ("Full", "C"),
        ("Shortened", "c"),
        ("None", "")
        ]

ourMessage ='Convention (Style) Reports'
messageVar = Message(frm, text = ourMessage, width=500) 
messageVar.pack( )

for text, mode in CONVENTIONMODES:
    b = Radiobutton(frm, text=text,variable=c, value=mode)
    b.pack(anchor=W)
    
e = StringVar()
e.set("e") # initialize

ERRORMODES = [
        ("Full", "E"),
        ("Shortened", "e"),
        ("None", "")
        ]

ourMessage = '\nError Reports'
messageVar = Message(frm, text = ourMessage, width=500) 
messageVar.pack( )

for text, mode in ERRORMODES:
    b = Radiobutton(frm, text=text,variable=e, value=mode)
    b.pack(anchor=W)

w = StringVar()
w.set("w") # initialize

WARNINGMODES = [
        ("Full", "W"),
        ("Shortened", "w"),
        ("None", "")
        ]

ourMessage = '\nWarning Reports'
messageVar = Message(frm, text = ourMessage, width=500) 
messageVar.pack( )

for text, mode in WARNINGMODES:
    b = Radiobutton(frm, text=text,variable=w, value=mode)
    b.pack(anchor=W)

r = StringVar()
r.set("r") # initialize

REFACTORMODES = [
        ("Full", "R"),
        ("Shortened", "r"),
        ("None", "")
        ]

ourMessage = '\nRefactor Reports'
messageVar = Message(frm, text = ourMessage, width=500) 
messageVar.pack( )

for text, mode in REFACTORMODES:
    b = Radiobutton(frm, text=text,variable=r, value=mode)
    b.pack(anchor=W)


f = StringVar()
f.set("f") # initialize

FATALMODES = [
        ("Full", "F"),
        ("Shortened", "f"),
        ("None", "")
        ]

ourMessage = '\nFatal Reports'
messageVar = Message(frm, text = ourMessage, width=500) 
messageVar.pack( )

for text, mode in FATALMODES:
    b = Radiobutton(frm, text=text,variable=f, value=mode)
    b.pack(anchor=W)


buttonb = Button(frm, text="BROWSE & LINT", command=load_file)
buttonb.pack(side=TOP, pady= 20)

buttonc = Button(frm, text='CLOSE HELPER', command=master.destroy)
buttonc.pack(side=TOP)



mainloop()

