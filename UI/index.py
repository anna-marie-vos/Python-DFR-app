from tkinter import *
from UI.DFRCreator import DFR
from db.state import Service

Dfr = DFR()
service = Service('service')

print(service.service)

class Window():
    def __init__(self, window):
        self.window = window
        self.window.wm_title('DFR Creator')

        title1 = Label(window, text = "DFR Template Creator")
        title1.grid(row = 0, column = 0, columnspan = 11 )

        title2 = Label(window, text="Service")
        title2.grid(row = 1, column = 0, columnspan = 6 )

        title3 = Label(window, text="Components")
        title3.grid(row = 1, column = 7, columnspan = 6 )

        checked = Variable()
        item = Checkbutton(window, text="item1", variable=checked)
        item.grid(row=2, column = 0, columnspan = 3)

window=Tk()
Window(window)
window.mainloop()
