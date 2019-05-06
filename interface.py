# tkinter tutorial https://www.geeksforgeeks.org/python-gui-tkinter/
from tkinter import *
from subprocess import *
import subprocess
import os
def install():
    os.system("source installation.sh")
    # subprocess.check_call(['./installation.sh'])
    result = check_output(['python3', '--version']).decode("utf-8").split(' ')
    version = result[1][0:3]
    # print("cp -R checkers/* virtual/lib/python"+str(version)+"/site-packages/pylint/checkers/")
    os.system("cp -R checkers/* virtual/lib/python"+str(version)+"/site-packages/pylint/checkers/")
    # subprocess.check_call(command.split(' '))


master = Tk()
master.title('Automated CS150 Lab Helper')
w = Canvas(master, width=50*15, height=40*15)
w.pack()
canvas_height=40*15
canvas_width=50*15
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
button = Button(master, text="INSTALL", width=20, command=install)
button.pack()
button = Button(master, text='CLOSE', width=20, fg ='red', bg = 'black', command=master.destroy)
button.pack()
mainloop()
