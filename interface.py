from tkinter import *

window = Tk()

def selectedItem():
    selected = checked

window.wm_title("DFR Creator")

checked = Variable()
check = Checkbutton(window, text = "Hello", variable = checked)
check.grid(row = 1, column = 1,columnspan = 2)
check.pack()



window.mainloop()
