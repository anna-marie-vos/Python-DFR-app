import sys
from tkinter import *
from UI.Func import *

window = Tk()

window.title("DFR creator")         #this is the title / can also use wm_title()
window.geometry("500x500+100+100")  #"XDimxYDim+screenDiff+screenDiff"

                                    #fg = foreground, bg=background
TemplateLabel = Label(window,text="TEMPLATE CREATOR",
    fg="#009900", bg="#d9ffb3", relief="raised")
TemplateLabel.pack()                #places things in the centre
TemplateLabel.place(x="5",y="5")    #if you dont use a grid
                                    # TemplateLabel.grid(row="0", column="0")
                                    # sticky = align text W(west), E(east), N(north), S(south)

createWordButton = Button(window, text="CONVERT TO WORD",
    command=say)
createWordButton.pack()



window.mainloop() #loop
