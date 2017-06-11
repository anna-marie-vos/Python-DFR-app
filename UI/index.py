from tkinter import *
from UI.DFRCreator import DFR
from db.state import Service

Dfr = DFR()
service = Service('service')


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

        self.mapContent()

        keys = service.content
        for index,key in enumerate(keys):
            self.renderServices(index,key)

    def mapContent(self):
        content = service.content
        serviceNames = []
        self.serviceNames = serviceNames
        for index, serviceName in enumerate(content):
            self.serviceNames.append(serviceName)            


    def renderServices(self,index,key):
        services = self.serviceNames
        services = Variable()
        name = key

        name = Checkbutton(window, text=key, variable=services)
        name.grid(row = (2+index), column = 0, columnspan = 3)
        self.renderSubject(key)

    def renderSubject(self,key):
        subjects = service.content[key]

        for i,para in enumerate(subjects):
            name = para
            heading = subjects[para]['heading']
            heading = Variable()
            name = Checkbutton(window, text=key, variable=heading)
            name.grid(row = (2+i), column = (4+i), columnspan = 3)



window=Tk()
Window(window)
window.mainloop()
