import tkinter as tk
from tkinter import ttk
from eventhandle import *
from gui import *


root = tk.Tk()
root.title("Keto Gator")
root.geometry("1280x720")

# Set Up GUI Frames

# All Sidebar Widgets
sidebar = displaysidebar(root)
addpatient = addpatientbutton(sidebar, root)
topbar = displaytopbar(root)
textbar = displaytextbar(topbar)
middle = displaydashboard(root)
bio = displaypatientbio(root)



listofgraphs = [" Graph 1"," Graph 2" ," Graph 3"," Graph 4"," Graph 5"," Graph 6", " Graph 1"," Graph 2" ," Graph 3"," Graph 4"," Graph 5"," Graph 6" ]

# Classes

class PatientIcons():
    def __init__(self, xcord, ycord):
        text = "Name"
        patienticon = tk.Label(middle, height=15, width=30, bg="white")
        patienticon.place(x=xcord, y=ycord)
        patientname = tk.Label(patienticon, text=text, bg="white")
        patientname.place(relx=0.5,rely=0.2, anchor="center")
        patienticon.bind("<Enter>", lambda event, arg=patienticon, patientname =patientname, name=text : hoverIcon(event, arg, patientname, name))
        patienticon.bind("<Leave>", lambda event, arg=patienticon, patientname =patientname, name=text: leaveIcon(event, arg, patientname, name))
        # patienticon.bind("<Button-1>", lambda event, frame=middle: clickIcon(event, frame))
        # patientname.bind("<Button-1>", lambda event, frame=middle: clickIcon(event, frame))
    

class GraphNames():
    def __init__(self, xcord, ycord, names):  
        graphbutton = tk.Label(sidebar, text=names,bg='#D16618', fg="#FFFFFF")
        graphbutton.config(font=("Roboto", 10, "bold"))
        graphbutton.place(x=xcord, y=ycord) 
        graphbutton.bind("<Enter>", lambda event, arg=graphbutton: hoversidebar(event, arg))
        graphbutton.bind("<Leave>", lambda event, arg=graphbutton: leavesidebar(event, arg))

displaygraphs(GraphNames, listofgraphs)



def click_start(event):
    
    bio.pack_forget()
    print("Deleting Bio")
    # displaydashboard(root)
    if middle is None:
        displaydashboard(middle)
        displaypatients(PatientIcons)

lefttitle = tk.Label(sidebar, text="Keto Gator", bg='#D16618')
lefttitle.config(font=("Avant Garde", 15))
lefttitle.place(relx=0.25, rely=0.05)
lefttitle.bind("<Button-1>", click_start)

displaydashboard(middle)
displaypatients(PatientIcons)



# patienticonslist = []





root.mainloop()
