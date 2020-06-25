import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *




class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        login_path = os.path.dirname(os.path.abspath(__file__))
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
        self.label.setStyleSheet("background-color: black; border-radius: 10px")
        


class Test (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,200,1280,720)

        ################### Side Bar ###################
        self.line1 = QFrame(self)
        self.line1.setGeometry(0,135,200,1)
        self.line1.setStyleSheet("background-color: black; border:none; color:black")

        self.line2 = QFrame(self)
        self.line2.setGeometry(0,182,200,1)
        self.line2.setStyleSheet("background-color: black; border:none; color:black")
        
        self.sidebar = QFrame(self)
        self.sidebar.setGeometry(0,0,200,2000)
        self.sidebar.setStyleSheet("background-color: rgb(209, 102, 24); border:none; color:black")
        self.sidebar.lower()

        self.logo = QLabel(self)
        self.logo.setGeometry(10,17,180,98)
        ui_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(ui_path, "Keto-Gator-V3.png")
        print(img_path)
        self.logo.setPixmap(QPixmap(img_path)) 
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.newpatientbuttion = QLabel("Add New Patient", self)
        self.newpatientbuttion.move(30,150)
        self.newpatientbuttion.resize(140,20)
        self.newpatientbuttion.setFont(QtGui.QFont("Ariel", 14))
        self.newpatientbuttion.setStyleSheet("color:white")
        self.newpatientbuttion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.graphlist = QListWidget(self)
        temp = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve","One", "Two", "Three"]
        self.graphlist.addItems(temp)
        self.graphlist.setGeometry(8,190,191,400)
        self.graphlist.setStyleSheet("background-color: rgb(209, 102, 24); border:none; color:white")
        self.graphlist.setFont(QtGui.QFont("Ariel", 14))
        self.graphlist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        

        ################### Top Bar ###################
        self.topbar = QtWidgets.QFrame(self)
        self.topbar.setGeometry(200,0,1920,135)
        self.topbar.setStyleSheet("background-color:rgb(12, 76, 173); border:none; color:black")
        
        self.searchbar = QtWidgets.QLineEdit(self)
        self.searchbar.setPlaceholderText("Patient Search")
        self.searchbar.setStyleSheet("background-color:rgb(255, 255, 255);border-radius: 10px;")
        
        self.logoutbutton = QtWidgets.QLabel("Log Out",self)
        self.logoutbutton.setStyleSheet("color:white")
        self.logoutbutton.setFont(QtGui.QFont("Ariel", 14))
        self.logoutbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.confirmbutton = QtWidgets.QPushButton("Confirm",self)
        self.confirmbutton.setStyleSheet("background-color: rgb(209, 102, 24);color:white; border-radius: 10px; padding-left: 15px; padding-right: 15px; padding-top:10px; padding-bottom:10px ")
        self.confirmbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ################### Middle ###################
        self.one = QtWidgets.QLabel("one",self)
        self.two = QtWidgets.QLabel("two",self)
        self.three = QtWidgets.QLabel("three",self)
        self.four = QtWidgets.QLabel("four",self)
        self.five = QtWidgets.QLabel("five",self)

        self.one.resize(5,5)
        self.one.setStyleSheet("background: black")

        ################### Layouts ###################
        mainlayout = QHBoxLayout()
        rightlayout = QVBoxLayout()
        topbar = QHBoxLayout()
        sidebar = QVBoxLayout()
        middle = QGridLayout()
        
        middle.addWidget(self.one)
        middle.addWidget(self.two)
        middle.addWidget(self.three)
        middle.addWidget(self.four)
        middle.addWidget(self.five)

        topbarmid1 = QVBoxLayout()
        topbarmid2 = QHBoxLayout()
        topbarmid3 = QHBoxLayout()
        topbarmid4 = QVBoxLayout()

        topbarmid1.addWidget(self.searchbar)
        topbarmid1.addLayout(topbarmid2)
        topbarmid1.setContentsMargins(300,30,350,0)

        topbarmid2.addStretch()
        topbarmid2.addWidget(self.confirmbutton)


        topbarmid4.addWidget(self.logoutbutton)
        
        topbarmid3.addLayout(topbarmid4)
        topbarmid3.addLayout(topbarmid1)

        topbar.addLayout(topbarmid3)
        # topbar.addWidget(self.topbar)

        rightlayout.addLayout(topbar, 20)
        rightlayout.addLayout(middle,80)

        middle.setContentsMargins(10,50,10,10)

        mainlayout.addLayout(sidebar,17)
        mainlayout.addLayout(rightlayout,83)

        self.setLayout(mainlayout)

        ################### Event Calling ###################
        self.logo.mousePressEvent = self.handlelogo
        self.newpatientbuttion.mousePressEvent = self.handlenewpatient
        self.graphlist.itemClicked.connect(self.handlelist)    

        self.confirmbutton.mousePressEvent = self.handlesearch
        self.logoutbutton.mousePressEvent = self.handlelogout


################### Event Handling ###################

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
    app = QApplication(sys.argv)
    
    # login = Login()
    # login.show()
    
    # window = MainUI()
    # window.show()
    test = Test()
    test.show()
    app.exec_()


if __name__ == "__main__":
    main()