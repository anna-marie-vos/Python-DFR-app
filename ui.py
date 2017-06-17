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
        self.renderServices()

        systemsLabel = Label(window, text="Systems:")
        systemsLabel.grid(row=len(self.data)+1, column="0")

    def renderServices(self):
        i = 0
        servicesData = self.data
        self.var = {}
        for key, value in servicesData.items():
            i +=1
            self.var.update({key:IntVar()})
            service = Checkbutton(window, text=key,
                variable=self.var[key], command=self.renderSections)
            service.grid(row = i, column = 1)

    def renderSections(self):
        self.sectionsArray = []
        i = len(self.data)+1

        for key in self.var:
            if self.var[key].get() == 1:
                for k in self.data[key]:
                    i+=2
                    section = Checkbutton(window, text=k)
                    section.grid(row=i+1,column = 1)
                    self.sectionsArray.append(section)
            elif self.var[key].get() == 0:
                self.eraseSections()

    def eraseSections(self):
        for item in self.sectionsArray:
            item.destroy()
            print('sectionsArray',item)

    def Data(self):
        self.data = {
        'Mechanical':{
            'Fan Coil Units': [
            'mech1',
            'mech2, mech2, mech2',
            'mech3, mech3, mech3'
            ],
            'Chilled Beams': [
            'mech1',
            'mech2, mech2, mech2',
            'mech3, mech3, mech3'
            ],
        },
        'Electrical':{
            'Conduits': [
            'Elec1',
            'Elec2, Elec2, Elec2',
            'Elec3, Elec3, Elec3'
            ]
        },
        'Hydraulics':{
            'Pipes': [
            'pipe1',
            'pipe2, pipe2, pipe2',
            'pipe3, pipe3, pipe3'
            ]
        },
        }

window=Tk()
Window(window)
window.mainloop()
