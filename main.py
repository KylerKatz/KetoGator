import tkinter as tk


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

# All Topbar Widgets 
topbar = tk.Frame(root, width=500, bg='#0C4CAD', height=100)
topbar.pack(expand=False, fill='both', side='top')
topbar.pack_propagate(0)

textbar = tk.Entry(topbar, width=50, justify='center')
textbar.insert(10, "Patient Search")
textbar.place(relx=0.4, rely=0.5)



# All Center Widgets
middle = tk.Frame(root, width=500, bg='#d6d4d0', height=660)
middle.pack(expand=False, fill='both')




# GUI Event Handling

def delete_default(event): # note that you must include the event as an arg, even if you don't use it.
    textbar.delete(0, "end")
    return None

textbar.bind("<Button-1>", delete_default)







root.mainloop()

