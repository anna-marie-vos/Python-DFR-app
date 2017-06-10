from tkinter import *
from UI.DFRCreator import DFR

dfr = DFR()

class Window():
    def __init__(self, window):
        self.window = window
        self.window.wm_title('DFR Creator')

        title1 = Label(window, text = "DFR Template Creator")
        title1.grid(row = 0, column = 0, columnspan = 11 )

window=Tk()
Window(window)
window.mainloop()
