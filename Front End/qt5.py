import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt




class Login (QWidget):
    def __init__(self):
        super().__init__()

    
        # login_path = os.path.dirname(os.path.abspath(__file__))
        # uic.loadUi(os.path.join(login_path, "login.ui"), self) 

        # self.loginbutton = self.findChild(QtWidgets.QPushButton,"loginbutton")
        # self.usernamefield = self.findChild(QtWidgets.QLineEdit, "usernamefield")
        # self.passwordfield = self.findChild(QtWidgets.QLineEdit, "passwordfield")



        # self.loginbutton.mousePressEvent = self.handlelogin
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
        self.setMinimumWidth(1280)

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

        self.logoutbutton = QtWidgets.QPushButton("Log Out",self)
        self.logoutbutton.setStyleSheet("background-color: rgb(209, 102, 24);color:white; border-radius: 10px; padding-left: 15px; padding-right: 15px; padding-top:10px; padding-bottom:10px")
        self.logoutbutton.setFont(QtGui.QFont("Ariel", 14))
        self.logoutbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.confirmbutton = QtWidgets.QPushButton("Confirm",self)
        self.confirmbutton.setStyleSheet("background-color: rgb(209, 102, 24);color:white; border-radius: 10px; padding-left: 15px; padding-right: 15px; padding-top:10px; padding-bottom:10px; font-weight:bold; ")
        self.confirmbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ################### Middle DashBoard ###################
       
        self.dashboardtext = QLabel("Current Patients")
        self.dashboardtext.setFont(QtGui.QFont("Ariel", 14))

        ################### Middle Profile ###################
        self.patientname = QLabel("Patient Name")
        self.patientname.setFont(QtGui.QFont("Ariel", 35))

        self.patientage = QLabel("Age: ")
        self.patientage.setFont(QtGui.QFont("Ariel", 14))

        self.updateinfobutton = QPushButton("Update")
        self.updateinfobutton.setStyleSheet("background-color: rgb(12, 76, 173);color:white; border-radius: 10px; padding-left: 15px; padding-right: 15px; padding-top:10px; padding-bottom:10px; font-weight: bold ")
        self.updateinfobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ################### Add New Patient ###################
        self.newtip = QLabel("Complete The Form Below To Add A New Patient")
        
        self.namelabel = QLabel("Name:")
        self.nameinput = QLineEdit()

        self.agelabel = QLabel("Age:")
        self.ageinput = QLineEdit()
        


        ################### Layouts ###################
        self.mainlayout = QHBoxLayout()
        self.rightlayout = QVBoxLayout()
        self.topbar = QHBoxLayout()
        self.sidebar = QVBoxLayout()
        self.middle = QVBoxLayout()
        self.middlegrid = QGridLayout()
        self.groupbox = QGroupBox()
        self.profiletop = QHBoxLayout()
        self.newpatientform = QFormLayout()



        self.groupbox.setLayout(self.middlegrid)
        self.groupbox.setContentsMargins(0,0,0,0)

        self.middlescrollarea = QScrollArea(self)
        self.middlescrollarea.setWidget(self.groupbox)
        self.middlescrollarea.setWidgetResizable(True)

        self.topbarmid1 = QVBoxLayout()
        self.topbarmid2 = QHBoxLayout()

        self.topbarmid1.addWidget(self.searchbar)
        self.topbarmid1.addLayout(self.topbarmid2)
        self.topbarmid1.setContentsMargins(350,0,300,0)

        self.topbarmid2.addStretch()
        self.topbarmid2.addWidget(self.confirmbutton)

        self.topbar.addLayout(self.topbarmid1)
        self.topbar.addWidget(self.logoutbutton)
        self.topbar.setContentsMargins(0,50,50,20)
        self.topbar.setAlignment(QtCore.Qt.AlignTop)

        ################### Middle DashBoard ###################
        self.middle.addWidget(self.dashboardtext)
        self.middle.addWidget(self.middlescrollarea)
        
        ################### Middle Profile ###################
        self.profiletop.addWidget(self.patientname)
        self.profiletop.addWidget(self.updateinfobutton)


        self.middle.addLayout(self.profiletop)
        self.middle.addWidget(self.patientage)
        

        ################### Add New Patient ###################
        
        self.newpatientform.setContentsMargins(200,0,200,0)
        self.newpatientform.addRow(self.namelabel,self.nameinput)
        self.newpatientform.addRow(self.agelabel,self.ageinput)
        
        self.middle.addWidget(self.newtip)
        self.middle.addLayout(self.newpatientform)
        
        
        
        self.middle.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        self.rightlayout.addLayout(self.topbar,10)
        self.rightlayout.addLayout(self.middle,90)

        self.sidebar.setContentsMargins(0,0,200,0)

        # self.middlegrid.addWidget(self.middlescrollarea)

        self.mainlayout.addLayout(self.sidebar,10)
        self.mainlayout.addLayout(self.rightlayout,90)

        self.setLayout(self.mainlayout)


        ################### Event Calling ###################
        self.logo.mousePressEvent = self.handlelogo
        self.newpatientbuttion.mousePressEvent = self.handlenewpatient
        self.graphlist.itemClicked.connect(self.handlelist)    

        self.confirmbutton.mousePressEvent = self.handlesearch
        self.logoutbutton.mousePressEvent = self.handlelogout
        
        self.updateinfobutton.mousePressEvent = self.handleupdate

        self.loadpatients()
        self.closeprofile()
        self.closenewpatient()

        # self.closedashboard()




################### Event Handling ###################

    def handlelogo(self,event):
        print("Logo Clicked")
        self.opendashboard()
        self.closeprofile()
        self.closenewpatient()
        
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
        
        # Close everything else
        self.closedashboard()
        self.closeprofile()
        self.opennewpatient()

    def handleupdate(self, event):
        pass


        # self.confirmbutton.close()

    def loadpatients(self):
        for i in range (0,30):
            for j in range (0,5):
                self.patientbtn = QPushButton("Name:{}{}\n ID: ".format(i,j))
                self.patientbtn.setFont(QtGui.QFont("Ariel", 12))
                self.patientbtn.setStyleSheet("font-weight: bold;")

                self.middlegrid.addWidget(self.patientbtn,i,j)
                self.patientbtn.clicked.connect(self.openprofile)
    
    def loadgraphnames(self):
        
        newlist = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve","One", "Two", "Three"]
        temp = []
        temp.clear()
        temp.extend(newlist)
        self.graphlist.clear()
        self.graphlist.addItems(newlist)
        return temp
        

    def closedashboard(self):
        self.dashboardtext.close()
        self.middlescrollarea.close()

    def opendashboard(self):
        self.dashboardtext.show()
        self.middlescrollarea.show()

    def openprofile(self):
        print(self.sender().text())
        self.loadgraphnames()
        self.closedashboard()
        self.patientname.show()
        self.patientage.show()
        self.updateinfobutton.show()
        
    def closeprofile(self):
        self.patientname.close()
        self.patientage.close()
        self.updateinfobutton.close()

    def opennewpatient(self):
        self.newtip.show()
        self.namelabel.show()
        self.nameinput.show()
        self.agelabel.show()
        self.ageinput.show()

    def closenewpatient(self):
        self.newtip.close()
        self.namelabel.close()
        self.nameinput.close()
        self.agelabel.close()
        self.ageinput.close()


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