import tkinter as tk
from tkinter import ttk
import eventhandle


# All Topbar Widgets
def displaytopbar(parent):
    topbar = tk.Frame(parent, width=500, bg='#0C4CAD', height=100)
    topbar.pack(expand=False, fill='both', side='top')
    topbar.pack_propagate(0)
    return topbar


def displaytextbar(parent):
    textbar = tk.Entry(parent, width=50, justify='center')
    textbar.insert(10, "Patient Search")
    textbar.place(relx=0.4, rely=0.5)
    textbar.bind("<Button-1>", lambda event, arg=textbar: delete_default(event, arg))
    return textbar


# All Sidebar Widgets

def displaysidebar(parent):
    sidebar = tk.Frame(parent, width=200, bg='#D16618', height=500)
    sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
    sidebar.pack_propagate(0)

    firstdivider = ttk.Separator(sidebar)
    firstdivider.place(x=0, y=99, relwidth=1)

    seconddivider = ttk.Separator(sidebar)
    seconddivider.place(x=0, y=150, relwidth=1)

    return sidebar

def addpatientbutton(parent, parentdisplay):
    addpatient = tk.Label(parent, text="Add New Patient",bg='#D16618', fg="#FFFFFF")
    addpatient.config(font=("Roboto", 10, "bold"))
    addpatient.place(x=30, y=115)
    addpatient.bind("<Button-1>", lambda event, arg=parentdisplay: displayaddnewpatient(arg))
    addpatient.bind("<Enter>", lambda event, arg=addpatient: hoversidebar(event, arg))
    addpatient.bind("<Leave>", lambda event, arg=addpatient: leavesidebar(event, arg))
    return addpatient


# All Center Widgets
def displaydashboard(parent):
    middle = tk.Frame(parent,  bg='#d6d4d0', height=800, width=600)
    middle.pack(expand=False, fill='both')
    return middle

def displaypatientbio(parent):
    bio = tk.Frame(parent,  bg='#000000', height=800, width=600)
    bio.pack(expand=False, fill='both')
    return bio

def displayaddnewpatient(parent):
    patientnew = tk.Frame(parent,  bg='#000000', height=800, width=600)
    patientnew.pack(expand=False, fill='both')




#--------------------------------------------------------------

# Delete the defualt text in the search bar when clicked
def delete_default(event, arg):
    arg.delete(0, "end")
    return None

# Bring up add patient page when addnewpatient text is clicked
def addnewpatient(event, arg):
    print("Clicked")

def hoversidebar(event, arg):
    arg.config(fg="black", cursor="center_ptr")

def leavesidebar(event, arg):
    arg.config(fg="#FFFFFF")

def hoverIcon(event, arg, patientname, name):
    arg.config(background="#e3e1e1")
    patientname.config(text=name, bg="#e3e1e1")

def leaveIcon(event, arg, patientname, name):
    arg.config(bg="white") 
    patientname.config(text=name, bg="white")  

def clickIcon(event, frame):
    # frame.pack_forget()
    # patienticon.pack_forget()

    frame.config(bg="red")
    print(frame)

    # bio = displaypatientbio(parentchange)
    # bio.pack(expand=False, fill='both')
    print("Test")

#Helper Functions
def displaypatients(patient):
    x = 50
    y = 10
    for i in range(8):
        (patient(x, y))
        x += 250
        if(x % 1050 == 0):
            y += 300
            x = 50
            i = i
            print("In here")


def displaygraphs(names, listofgraphs):
    x = 30
    y = 160
    for i in listofgraphs:
        names(x,y,i)
        y+=30