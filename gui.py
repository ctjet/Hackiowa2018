from tkinter import *
from dataOrganization import parse


master = Tk()
top = Scale(master, from_=2010, to=2017, orient=HORIZONTAL)

bottom = Scale(master, from_=2010, to=2017, orient=HORIZONTAL)

def reDraw():
    parse()



def bottomSliderRelease(event):
    if bottom.get()<top.get():
        top.set(bottom.get())

def topSliderRelease(event):
    if bottom.get()<top.get():
        bottom.set(top.get())

top.bind("<ButtonRelease-1>",topSliderRelease)
bottom.bind("<ButtonRelease-1>",bottomSliderRelease)
toplabel = Label(master, text="Start Date")
toplabel.pack()
top.pack()
bottomLabel = Label(master, text="End Date")
bottomLabel.pack()
bottom.pack()



mainloop()