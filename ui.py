import sys
from tkinter import *


class Window(object):
    def __init__(self,window):
        self.Data()
        self.allServices = []
        self.allSections = []
        self.allText = []
        self.servicesVar = {}
        self.sectionsAdded = []
        self.activeServices = []
        self.activeServiceLabels = []
        self.sectionsVar = {}

        self.window = window
        self.window.geometry("500x500+100+100")
        self.window.wm_title("DFR Creator")

        title1 = Label(window,text = "DFR Template maker")
        title1.grid(row="0",column="0")

        servicesLabel = Label(window, text="Services:")
        servicesLabel.grid(row="1", column="0")
        self.renderServices()

        systemsLabel = Label(window, text="Systems:")
        systemsLabel.grid(row=len(self.data)+1, column="0")

    # def populateData(self):
    #     for service in self.data:
    #         self.allServices.append(service)
    #         for section in self.data[service]:
    #             self.allSections.append(section)
    #             for para in self.data[service][section]:
    #                 self.allText.append(para)
    #     print('services: ',self.allServices)
    #     print('sections: ',self.allSections)
    #     print('text: ',self.allText)

    def renderServices(self):
        '''renders all se services Checkbuttons'''
        i = 0

        for key, value in self.data.items():
            i +=1
            self.servicesVar.update({key:IntVar()})
            service = Checkbutton(window, text=key,
                variable=self.servicesVar[key],
                command=self.findActiveService)
            service.grid(row = i, column = 1)

    def findActiveService(self):
        '''Addes the active services to an array'''
        del self.activeServices[:]
        i = len(self.data)+1

        for key in self.servicesVar:
            if self.servicesVar[key].get() == 1:
                self.activeServices.append(key)

        self.renderSections()

    def renderSections(self):
        '''Checks which services are active
        and renders all the relevent sections'''
        self.clearSections()
        self.clearText()
        i = len(self.data)+1

        for service in self.activeServices:
            systemsLabel = Label(window, text=service+":")
            systemsLabel.grid(row=i+2, column="0")
            self.sectionsAdded.append(systemsLabel)

            for key in self.data[service]:
                i+=2
                self.sectionsVar.update({key:IntVar()})
                section = Checkbutton(window, text=key,
                variable=self.sectionsVar[key],
                command = self.renderSectionInfo)
                section.grid(row=i+1,column = 1)
                self.sectionsAdded.append(section)

    def clearSections(self):
        '''Clears the selected sections '''
        for obj in self.sectionsAdded:
            obj.destroy()

    def clearText(self):
        for obj in self.allText:
            obj.destroy()

    def renderSectionInfo(self):
        for key in self.sectionsVar:
            if self.sectionsVar[key].get() ==1:
                print(key," : ", self.sectionsVar[key].get())
                self.generateText()
        print('---------------')


    def generateText(self):
        self.clearText()
        i = len(self.data)+len(self.allSections)+2
        print(i)
        generalText = Text(window, width=4,height=4)
        generalText.grid(
            row= i,
            column = 3)
        self.allText.append(generalText)

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
            'VAV system': [
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
            ],
            'Lights': [
            'Elec1',
            'Elec2, Elec2, Elec2',
            'Elec3, Elec3, Elec3'
            ],
            'Distribution Boards': [
            'Elec1',
            'Elec2, Elec2, Elec2',
            'Elec3, Elec3, Elec3'
            ],
            'Insulation': [
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
