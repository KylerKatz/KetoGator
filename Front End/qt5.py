import os
import sys

from PyQt5 import QtWidgets, uic, QtSql, QtCore




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

            
        




class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(ui_path, "mainui.ui"), self) 

        # Sidebar assignments 
        self.logo = self.findChild(QtWidgets.QLabel,"logo")
        self.newpatientbuttion = self.findChild(QtWidgets.QLabel,"newpatientbutton")   
        self.graphlist = self.findChild(QtWidgets.QListWidget, "graphlist") # Not correct 

        #Topbar assignemts
        self.searchbar = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.logoutbutton = self.findChild(QtWidgets.QLabel,"logoutbutton")
        self.confirmbutton = self.findChild(QtWidgets.QPushButton, "confirmbutton")

    #     print(type(self.searchbar))

        # Dashboard
        # Need to create a label for each patient 
        # learn how to do this with code 

        # Trigger events 
        self.logo.mousePressEvent = self.handlelogo
        # self.graphlist.itemSelectionChanged.connect(self.handlelist)
        # self.searchbar

        self.confirmbutton.mousePressEvent = self.handlesearch

       
    
    # Event handling methods 

    def handlelogo(self,event):
        print("Logo Clicked")

    def handlelist(self,event,item):
        print(item.text())

    def handlesearch(self,event):
        self.searchbar.text()
        print("Confirm Clicked")


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    # login = Login()
    # login.show()
    
    window = MainUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()