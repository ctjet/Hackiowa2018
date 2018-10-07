from tkinter import *
from dataOrganization import parse

def strToPhenom(s):
    if s=="None":
        return "N"
    elif s=="Flash Flood":
        return "numFF"
    elif s=="Tornado":
        return "numTO"
    elif s=="Severe T-Storm":
        return "numSV"


master = Tk()
top = Scale(master, from_=2010, to=2017, orient=HORIZONTAL)

bottom = Scale(master, from_=2010, to=2017, orient=HORIZONTAL)

button = Button(master,text = "Redraw")

DENOMOPTIONS = ["None","Flash Flood","Severe T-Storm","Tornado"]

NUMEROPTIONS = ["Flash Flood","Severe T-Storm","Tornado"]

numVar = StringVar(master)
denomVar = StringVar(master)
numVar.set(NUMEROPTIONS[0])
denomVar.set(DENOMOPTIONS[2])

numOptMen = OptionMenu(master, numVar, *NUMEROPTIONS)
denomOptMen = OptionMenu(master, denomVar, *DENOMOPTIONS)




def reDraw(event):
    parse(top.get(),bottom.get(), strToPhenom(numVar.get()), strToPhenom (denomVar.get()), "Iowa: "+ numVar.get()+"/"+denomVar.get()+ " For " + str(top.get()) + " - "+ str(bottom.get()))



def bottomSliderRelease(event):
    if bottom.get()<top.get():
        top.set(bottom.get())

def topSliderRelease(event):
    if bottom.get()<top.get():
        bottom.set(top.get())

button.bind("<ButtonRelease-1>",reDraw)

top.bind("<ButtonRelease-1>",topSliderRelease)
bottom.bind("<ButtonRelease-1>",bottomSliderRelease)
toplabel = Label(master, text="Start Date")
toplabel.pack()
top.pack()
bottomLabel = Label(master, text="End Date")
bottomLabel.pack()
bottom.set(2017)
bottom.pack()
numOptMen.pack()
denomOptMen.pack()
button.pack()



mainloop()