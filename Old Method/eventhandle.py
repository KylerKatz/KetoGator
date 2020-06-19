# import tkinter as tk
# import gui


# # Delete the defualt text in the search bar when clicked
# def delete_default(event, arg):
#     arg.delete(0, "end")
#     return None

# # Bring up add patient page when addnewpatient text is clicked
# def addnewpatient(event, arg):
#     print("Clicked")

# def hoversidebar(event, arg):
#     arg.config(fg="black", cursor="center_ptr")

# def leavesidebar(event, arg):
#     arg.config(fg="#FFFFFF")

# def hoverIcon(event, arg, patientname, name):
#     arg.config(background="#e3e1e1")
#     patientname.config(text=name, bg="#e3e1e1")

# def leaveIcon(event, arg, patientname, name):
#     arg.config(bg="white") 
#     patientname.config(text=name, bg="white")  

# def clickIcon(event, frame):
#     # frame.pack_forget()
#     # patienticon.pack_forget()

#     frame.config(background="red")
#     print(frame)

#     # bio = displaypatientbio(parentchange)
#     # bio.pack(expand=False, fill='both')
#     print("Test")





# #Helper Functions
# def displaypatients(patient):
#     x = 50
#     y = 10
#     for i in range(8):
#         (patient(x, y))
#         x += 250
#         if(x % 1050 == 0):
#             y += 300
#             x = 50
#             i = i
#             print("In here")


# def displaygraphs(names, listofgraphs):
#     x = 30
#     y = 160
#     for i in listofgraphs:
#         names(x,y,i)
#         y+=30

