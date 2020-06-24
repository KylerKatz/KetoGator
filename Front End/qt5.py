import os
import sys

from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui




# Questions
# 1) How to trigger event when ListWidget item is clicked 
# self.graphlist.itemSelectionChanged.connect(self.handlelist)
# 2) How to get trigger event when enter is hit
# 3) How to get text from LineEdit 
# self.searchbar.text()


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        # login_path = os.path.dirname(os.path.abspath(__file__))
        login_path = ".//UI Files//login.ui"
        uic.loadUi(os.path.join(login_path, "login.ui"), self) 

        self.loginbutton = self.findChild(QtWidgets.QPushButton,"loginbutton")
        self.usernamefield = self.findChild(QtWidgets.QLineEdit, "usernamefield")
        self.passwordfield = self.findChild(QtWidgets.QLineEdit, "passwordfield")



        self.loginbutton.mousePressEvent = self.handlelogin
    def handlelogin(self,event):
    
        # Do credential checking here 
        print("Hello")
        # window = MainUI()
        # window.show()
        # If they are vaild, show MainUI

            
        
class PatientLabel(QtWidgets.QLabel):
    def __init__(self):
        super(PatientLabel,self).__init__()
        self.label = QtWidgets.QLabel("test dsfsff sdfsd fdsfsdf sfs fsdfsfsf",self)
        self.label.setGeometry(500,200,200,200)
        self.label.setStyleSheet("background-color: white; border-radius: 10px")
        



class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "mainui.ui"), self) 

        # Sidebar assignments 
        self.logo = self.findChild(QtWidgets.QLabel,"logo")
        self.newpatientbuttion = self.findChild(QtWidgets.QLabel,"newpatientbutton")   

        
        self.graphlist = QtWidgets.QListWidget(self)
        temp = ["One", "Two", "Three"]
        self.graphlist.addItems(temp)
        self.graphlist.setGeometry(8,190,191,241)
        self.graphlist.setStyleSheet("background-color: rgb(209, 102, 24); border:none; color:white")
        self.graphlist.setFont(QtGui.QFont("Ariel", 14))
        self.graphlist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #Topbar assignemts
        self.searchbar = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.logoutbutton = self.findChild(QtWidgets.QLabel,"logoutbutton")
        self.confirmbutton = self.findChild(QtWidgets.QPushButton, "confirmbutton")

        # Trigger events 
        self.logo.mousePressEvent = self.handlelogo
        self.newpatientbuttion.mousePressEvent = self.handlenewpatient
        self.graphlist.itemClicked.connect(self.handlelist)    

        self.confirmbutton.mousePressEvent = self.handlesearch
        self.confirmbutton.hover = print("Hello")
        self.logoutbutton.mousePressEvent = self.handlelogout


        
        

        temp = PatientLabel()
        temp.show()


        patient = QtWidgets.QLabel()

        patient.linkHovered.connect(self.handlelogo)
    
    # Event handling methods 

    def handlelogo(self,event):
        print("Logo Clicked")

    def handlelist(self,item):
        print(item.text())

    def handlesearch(self,event):
        search = self.searchbar.text()
        if search != "":
            print(search)
        self.searchbar.setText("")
    
    def handlelogout(self,event):
        print("Log Out Clicked")
    
    def handlenewpatient (self,event):
        print("New Patient Clicked")
        # self.confirmbutton.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # login = Login()
    # login.show()
    
    window = MainUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()