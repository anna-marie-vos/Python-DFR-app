import sys
from tkinter import *

class Window(object):
    def __init__(self,window):
        self.Data()

        self.window = window
        self.window.geometry("500x500+100+100")
        self.window.wm_title("DFR Creator")

        self.title1 = Label(window,text = "DFR Template maker")
        self.title1.grid(row="0",column="0")

        serviceLabel = Label(window, text="Services:")
        serviceLabel.grid(row="1", column="0")

        self.renderChecks()

    def Data(self):
        self.data = {
        'Mechanical':{
            '1.1':'Fan Coil Units',
            'paragraphs':[
                'mech1 mech1 mech1',
                'mech2',
                'mech3 mech3 mech3 mech3 mech3',
                ]
            },
        'Electrical':{
            '1.1':'conduits',
            'paragraphs':[
                'elec elec elec',
                'elec1',
                'elec2 elec2 elec2 elec2',
                ]
            },
        }

    def renderChecks(self):
        i = 0
        servicesData = self.data
        self.var = {}
        for key, value in servicesData.items():
            i +=1
            self.var.update({key:IntVar()})
            service = Checkbutton(window, text=key,
                variable=self.var[key], command=self.recordTick)
            service.grid(row = i, column = 1)

    def recordTick(self):
        print('electrical',self.var['Electrical'].get())
        print('Mechanical',self.var['Mechanical'].get())

window=Tk()
Window(window)
window.mainloop()
