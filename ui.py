import sys
from tkinter import *

data = {
    'Mechanical':{
        '1.1':'Fan Coil Units',
        'paragraphs':['para para prar',
            'parap',
            'para 2 thr thrthrth hththr'
        ]
    },
    'Electrical':{
        '1.1':'Conduit',
        'paragraphs':['elec elec elec',
            'elec2 ele2 ele2',
            'ele3 ele3 elec3'
        ]
    },
}

window = Tk()
window.geometry("500x500+100+100")
window.title("DFR Template Maker")

title1 = Label(window,text = "DFR Template maker")
title1.grid(row="0",column="0")

serviceLabel = Label(window, text="Services:")
serviceLabel.grid(row="1", column="0")

# var = IntVar()
# c = Checkbutton(window, text="Expand", variable=var)
# c.grid(row=1,column=1)

def checkboxes():
    i=0
    for k, v in data.items():
        i += 1
        print (k, ", ","value")
        var = IntVar()
        c = Checkbutton(window, text=k, variable=var)
        c.grid(row=i,column=1)

checkboxes()

window.mainloop()
