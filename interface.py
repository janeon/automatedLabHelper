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
    command = "python3 cleanOutput.py "+fname+" CWERF"
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

master = Tk()
master.title('Automated CS150 Lab Helper')
#master.geometry("400x800")
frm = Frame(master, width=200, height=200)
frm.pack(side=LEFT)
frm.pack_propagate(0)

buttonb = Button(frm, text="BROWSE & LINT", command=load_file)
buttonb.pack(side=TOP, pady= (0,20))

buttonl = Button(frm, text="LOAD CUSTOM CHECKERS", command=load_checkers)
buttonl.pack(side=TOP, pady= 40)

buttonc = Button(frm, text='CLOSE HELPER', command=master.destroy)
buttonc.pack(side=TOP, pady= (20,0))


mainloop()
