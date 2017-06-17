import sys
from tkinter import *

window = Tk()

window.title("DFR creator") #this is the title / can also use wm_title()
window.geometry("500x500+100+100") #"XDimxYDim+screenDiff+screenDiff"

#fg = foreground, bg=background
TemplateLabel = Label(text="Template Creator",
    fg="#009900", bg="#d9ffb3", relief="raised")
TemplateLabel.pack()
TemplateLabel.place(x="10",y="10")

window.mainloop() #loop
