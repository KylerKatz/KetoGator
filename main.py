import tkinter as tk
from tkinter import ttk

# Classes
class PatientIcons():
    def __init__(self,xcord,ycord):
        patienticon = tk.Label(middle, height=15, width=30)
        patienticon.place(x=xcord, y=ycord)



root = tk.Tk()
root.title("Keto Gator")
root.geometry("1280x720")

# Set Up GUI Frames 

# All Sidebar Widgets 
sidebar = tk.Frame(root, width=200, bg='#D16618', height=500)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
sidebar.pack_propagate(0)

lefttitle = tk.Label(sidebar, text="Keto Gator", bg='#D16618')
lefttitle.config(font=("Avant Garde", 15))
lefttitle.place(relx =0.25, rely=0.05)


firstdivider = ttk.Separator(sidebar)
firstdivider.place(x=0, y=99, relwidth=1)

addpatient = tk.Label(sidebar, text="Add New Patient", bg='#D16618', fg="#FFFFFF")
addpatient.config(font=("Roboto", 10, "bold"))
addpatient.place(x=30, y=115)

seconddivider = ttk.Separator(sidebar)
seconddivider.place(x=0, y=150, relwidth=1)

# All Topbar Widgets 
topbar = tk.Frame(root, width=500, bg='#0C4CAD', height=100)
topbar.pack(expand=False, fill='both', side='top')
topbar.pack_propagate(0)

textbar = ttk.Entry(topbar, width=50, justify='center')
textbar.insert(10, "Patient Search")
textbar.place(relx=0.4, rely=0.5)

# All Center Widgets
middle = tk.Canvas(root, width=500, bg='#d6d4d0', height=660)
middle.pack(expand=False, fill='both')


# GUI Event Handling

def delete_default(event): # note that you must include the event as an arg, even if you don't use it.
    textbar.delete(0, "end")
    return None

textbar.bind("<Button-1>", delete_default)

def addnewpatient(even):
    print("Clicked")

def hover(event=None):
    addpatient.config(fg="grey", cursor="center_ptr")
   

def leave(event=None):
    addpatient.config(fg="#FFFFFF")

addpatient.bind("<Button-1>",addnewpatient)
addpatient.bind("<Enter>",hover)
addpatient.bind("<Leave>",leave)

def displaypatients():
    x = 50
    y = 10
    for i in range(8):
        patienticonslist.append(PatientIcons(x,y))
        x += 250
        if(x%1050 == 0):
            y += 300
            x = 50
            i=i

patienticonslist = []
displaypatients()


# frame = tk.Scrollbar(middle)
# frame.pack(side="right", fill="y")
# listbox = tk.Listbox(middle, yscrollcommand=frame.set, width=200)

# for i in range(patienticonslist.le):
#     listbox.insert("end", patienticonslist[i])
# listbox.pack(side="left")

# frame.config(command=listbox.yview)

root.mainloop()

