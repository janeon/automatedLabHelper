# tkinter tutorial https://www.geeksforgeeks.org/python-gui-tkinter/
from tkinter import *
import subprocess

def install():
    subprocess.check_call(['./installation.sh'])

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
