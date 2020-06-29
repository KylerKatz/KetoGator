import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *

from SpreadSheetAccess import *


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
        self.setWindowTitle("Keto Gator")
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
        # self.graphlist.setFont(QtGui.QFont("Ariel", 14))
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
       
        self.currentpatienttext = QLabel()
        self.currentpatienttext.setFont(QtGui.QFont("Ariel", 14))

        ################### Middle Profile ###################
        self.patientname = QLabel()
        self.patientname.setFont(QtGui.QFont("Ariel", 35))

        self.patientage = QLabel("Age: ")
        self.patientage.setFont(QtGui.QFont("Ariel", 14))

        self.updateinfobutton = QPushButton("Enter New Data")
        self.updateinfobutton.setStyleSheet("background-color: rgb(12, 76, 173);color:white; border-radius: 10px; padding-left: 15px; padding-right: 15px; padding-top:10px; padding-bottom:10px; font-weight: bold ")
        self.updateinfobutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ################### Add New Patient ###################
        self.newtip = QLabel("Complete The Form Below To Add A New Patient")
        
        self.namelabel = QLabel("Name:")
        self.nameinput = QLineEdit()

        self.agelabel = QLabel("Age:")
        self.ageinput = QLineEdit()


        ################### Update Data ###################
        self.selectgraph = QLabel("Select a Graph Type:")
        self.graphselector = QComboBox()
        self.graphselector.addItems(["", "Alertness","Anthropometrics","Daily Intake","Diet RX Source","Med Load","Seizure Data","Seizure Load","Urine Kt SG Source","Vitals"])

        ################### Update Data - Anthropometrics ###################
        self.AnthropometricsMRNumberL = QLabel("Medical Record Number:")
        self.AnthropometricsMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.AnthropometricsMRNumberF = QLineEdit()
        self.AnthropometricsMRNumberF.setMaxLength(10)


        self.AnthropometricsDateL = QLabel("Date:")
        self.AnthropometricsDateL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsDateF = QLineEdit()
        self.AnthropometricsDateF.setMaxLength(10)

        self.AnthropometricsDayTypeL = QLabel("Day Type:")
        self.AnthropometricsDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsDayTypeF = QLineEdit()

        self.AnthropometricsSourceL = QLabel("Source:")
        self.AnthropometricsSourceL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSoruceF = QLineEdit()

        self.AnthropometricsCPL = QLabel("Cerebral Palsy Energy Factor:")
        self.AnthropometricsCPL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsCPF = QLineEdit()

        self.AnthropometricsPAL = QLabel("Physical Activity Coefficient:")
        self.AnthropometricsPAL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsPAF = QLineEdit()

        self.AnthropometricsHtL = QLabel("Height:")
        self.AnthropometricsHtL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsHtF = QLineEdit()

        self.AnthropometricsWtL = QLabel("Weight:")
        self.AnthropometricsWtL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsWtF = QLineEdit()

        self.AnthropometricsHCL = QLabel("Head Circumference:")
        self.AnthropometricsHCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsHCF = QLineEdit()

        self.AnthropometricsUACL = QLabel("Upper Arm Circumference:")
        self.AnthropometricsUACL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUACF = QLineEdit()

        self.AnthropometricsTSFL = QLabel("Triceps Skinfold:")
        self.AnthropometricsTSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsTSFF = QLineEdit()

        self.AnthropometricsSSFL = QLabel("Subscapular Skinfold:")
        self.AnthropometricsSSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSSFF = QLineEdit()

        self.AnthropometricsUSFL = QLabel("Umbilicus Skinfold:")
        self.AnthropometricsUSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUSFF = QLineEdit()

        self.AnthropometricsSISFL = QLabel("Suprailiac Skinfold:")
        self.AnthropometricsSISFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSISFF = QLineEdit()

        self.AnthropometricsMBSFL = QLabel("Midback Skinfold:")
        self.AnthropometricsMBSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsMBSFF = QLineEdit()

        self.AnthropometricsUCL = QLabel("Umbilical Circumference:")
        self.AnthropometricsUCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUCF = QLineEdit()

        self.AnthropometricsEnteredL = QLabel("Entered:")
        self.AnthropometricsEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsEnteredF = QLineEdit()

        self.AnthropometricsCommentsL = QLabel("Comments:")
        self.AnthropometricsCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsCommentsF = QTextEdit()

        self.AnthropometricsSaveButton = QPushButton("Save")
        

        self.closeanthropometrics()
        
        self.currentpatient =""
        self.currentpatientMR =""
        
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
        self.graphinputformtop = QFormLayout()
        self.graphinputformanthropometrics = QGridLayout()



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
        self.middle.addWidget(self.currentpatienttext)
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
        

        ################### Update Data Anthropometrics ###################
        
        self.graphinputformtop.addRow(self.selectgraph,self.graphselector)
        # self.graphinputformanthropometrics.setColumnStretch(3,3)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMRNumberL,0,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMRNumberF,0,1)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsMRNumberD,0,2)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsDateL,1,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsDateF,1,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsDayTypeL,2,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsDayTypeF,2,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSourceL,3,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSoruceF,3,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCPL,4,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCPF,4,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsPAL,5,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsPAF,5,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsHtL,6,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsHtF,6,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsWtL,7,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsWtF,7,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsHCL,8,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsHCF,8,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUACL,9,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUACF,9,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsTSFL,10,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsTSFF,10,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSSFL,11,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSSFF,11,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUSFL,12,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUSFF,12,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSISFL,13,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSISFF,13,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMBSFL,14,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMBSFF,14,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUCL,15,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsUCF,15,1)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsRL,16,0)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsRF,16,1)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsXL,17,0)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsXF,17,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsEnteredL,18,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsEnteredF,18,1)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsAuditedL,19,0)
        # self.graphinputformanthropometrics.addWidget(self.AnthropometricsAuditedF,19,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCommentsL,20,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCommentsF,20,1)
        
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSaveButton,21,1)

       

        self.middle.addLayout(self.graphinputformtop)
        # self.middle.addLayout(self.graphinputformanthropometrics)
        # self.middle.removeItem(self.graphinputformanthropometrics)
        
        
        



        
        
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

        self.graphselector.currentIndexChanged.connect (self.handlegraphselection)

        self.AnthropometricsSaveButton.mousePressEvent = self.submitAnthropometrics

        self.loadpatients()
        self.closeprofile()
        self.closenewpatient()
        self.graphselector.close()
        self.selectgraph.close()
        self.closeanthropometrics()

        # self.closedashboard()




################### Event Handling ###################

    def handlelogo(self,event):
        print("Logo Clicked")
        self.opendashboard()
        self.closeprofile()
        self.closenewpatient()
        
        self.graphselector.setCurrentIndex(0)
        self.graphselector.close()
        self.selectgraph.close()
        self.closeanthropometrics()
        self.middle.removeItem(self.graphinputformtop)
        self.middle.removeItem(self.graphinputformanthropometrics)
        self.resetinputs()


        
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
        self.graphselector.close()
        self.selectgraph.close()
        self.closeanthropometrics()
        


    def handleupdate(self, event):
        self.closeprofile()
        self.middle.addLayout(self.graphinputformtop)

        self.graphselector.show()
        self.selectgraph.show()


        # self.confirmbutton.close()


    def handlegraphselection(self, event):
        selection = (self.graphselector.currentText())

        if (selection == "Anthropometrics"):
            self.middle.addLayout(self.graphinputformanthropometrics)
            self.graphinputformanthropometrics.setContentsMargins(200,0,200,0)
            self.openanthropometrics()



    def loadpatients(self):

        self.allpatients = getAllPatients()
        
        i = 0
        j = 0

        for patient in self.allpatients:
            self.patientbtn = QPushButton("MRN: " + patient)
            self.middlegrid.addWidget(self.patientbtn,i,j)
            self.patientbtn.clicked.connect(self.openprofile)

            j+=1


            if(j%5 == 0):
                i+=1
                j=0
           

        
        # for patient in self.allpatients:
        #     for j in range (0,5):
                                
        #         self.patientbtn = QPushButton("Name: " + patient)
        #         self.middlegrid.addWidget(self.patientbtn,0,j)
        #         print(patient)
                
                # self.patientbtn.setFont(QtGui.QFont("Ariel", 12))
                # self.patientbtn.setStyleSheet("font-weight: bold;")
                # self.patientbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


    
    def loadgraphnames(self):
        
        # newlist = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve","One", "Two", "Three"]
        newlist = getPatientGraphs(self.currentpatient)
        temp = []
        temp.clear()
        temp.extend(newlist)
        self.graphlist.clear()
        self.graphlist.addItems(newlist)
        return temp
        

    def closedashboard(self):
        self.currentpatienttext.close()
        self.middlescrollarea.close()

    def opendashboard(self):
        self.currentpatienttext.show()
        self.middlescrollarea.show()

    def openprofile(self):
        # temp = self.sender().text()
        # temp = temp[5:]
        # temp1 = temp.split("\n")
        # self.currentpatient = temp1[0][1:]
        # self.currentpatientMR = temp1[1][5:]
        
        self.currentpatient = self.sender().text()[5:]
               
        self.currentpatienttext.setText("Selected Patient: " + self.currentpatient) 

        self.patientname.setText(self.currentpatient)

        print(self.currentpatient)
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

    def closeanthropometrics(self):
        
        self.AnthropometricsMRNumberL.close()
        self.AnthropometricsMRNumberF.close()
        self.AnthropometricsDateL.close()
        self.AnthropometricsDateF.close()
        self.AnthropometricsDayTypeL.close()
        self.AnthropometricsDayTypeF.close()
        self.AnthropometricsSourceL.close()
        self.AnthropometricsSoruceF.close()
        self.AnthropometricsCPL.close()
        self.AnthropometricsCPF.close()
        self.AnthropometricsPAL.close()
        self.AnthropometricsPAF.close()
        self.AnthropometricsHtL.close()
        self.AnthropometricsHtF.close()
        self.AnthropometricsWtL.close()
        self.AnthropometricsWtF.close()
        self.AnthropometricsHCL.close()
        self.AnthropometricsHCF.close()
        self.AnthropometricsUACL.close()
        self.AnthropometricsUACF.close()
        self.AnthropometricsTSFL.close()
        self.AnthropometricsTSFF.close()
        self.AnthropometricsSSFL.close()
        self.AnthropometricsSSFF.close()
        self.AnthropometricsUSFL.close()
        self.AnthropometricsUSFF.close()
        self.AnthropometricsSISFL.close()
        self.AnthropometricsSISFF.close()
        self.AnthropometricsMBSFL.close()
        self.AnthropometricsMBSFF.close()
        self.AnthropometricsUCL.close()
        self.AnthropometricsUCF.close()
        # self.AnthropometricsRL.close()
        # self.AnthropometricsRF.close()
        # self.AnthropometricsXL.close()
        # self.AnthropometricsXF.close()
        self.AnthropometricsEnteredL.close()
        self.AnthropometricsEnteredF.close()
        # self.AnthropometricsAuditedL.close()
        # self.AnthropometricsAuditedF.close()
        self.AnthropometricsCommentsL.close()
        self.AnthropometricsCommentsF.close()
        self.AnthropometricsSaveButton.close()

    def openanthropometrics(self):
        self.AnthropometricsMRNumberL.show()
        self.AnthropometricsMRNumberF.show()
        self.AnthropometricsDateL.show()
        self.AnthropometricsDateF.show()
        self.AnthropometricsDayTypeL.show()
        self.AnthropometricsDayTypeF.show()
        self.AnthropometricsSourceL.show()
        self.AnthropometricsSoruceF.show()
        self.AnthropometricsCPL.show()
        self.AnthropometricsCPF.show()
        self.AnthropometricsPAL.show()
        self.AnthropometricsPAF.show()
        self.AnthropometricsHtL.show()
        self.AnthropometricsHtF.show()
        self.AnthropometricsWtL.show()
        self.AnthropometricsWtF.show()
        self.AnthropometricsHCL.show()
        self.AnthropometricsHCF.show()
        self.AnthropometricsUACL.show()
        self.AnthropometricsUACF.show()
        self.AnthropometricsTSFL.show()
        self.AnthropometricsTSFF.show()
        self.AnthropometricsSSFL.show()
        self.AnthropometricsSSFF.show()
        self.AnthropometricsUSFL.show()
        self.AnthropometricsUSFF.show()
        self.AnthropometricsSISFL.show()
        self.AnthropometricsSISFF.show()
        self.AnthropometricsMBSFL.show()
        self.AnthropometricsMBSFF.show()
        self.AnthropometricsUCL.show()
        self.AnthropometricsUCF.show()
        self.AnthropometricsEnteredL.show()
        self.AnthropometricsEnteredF.show()
        self.AnthropometricsCommentsL.show()
        self.AnthropometricsCommentsF.show()
        self.AnthropometricsSaveButton.show()

    def resetinputs(self):
        self.AnthropometricsMRNumberF.setText(""),
        self.AnthropometricsDateF.setText(""),
        self.AnthropometricsDayTypeF.setText(""),
        self.AnthropometricsSoruceF.setText(""),
        self.AnthropometricsCPF.setText(""),
        self.AnthropometricsPAF.setText(""),
        self.AnthropometricsHtF.setText(""),
        self.AnthropometricsWtF.setText(""),
        self.AnthropometricsHCF.setText(""),
        self.AnthropometricsUACF.setText(""), 
        self.AnthropometricsTSFF.setText(""),
        self.AnthropometricsSSFF.setText(""),
        self.AnthropometricsUSFF.setText(""),
        self.AnthropometricsSISFF.setText(""),
        self.AnthropometricsMBSFF.setText(""),
        self.AnthropometricsUCF.setText(""),
        self.AnthropometricsEnteredF.setText(""),
        self.AnthropometricsCommentsF.setText(""), 


    def submitAnthropometrics(self,event):
        saveAnthropometrics(
            self.AnthropometricsMRNumberF.text(),
            self.AnthropometricsDateF.text(),
            self.AnthropometricsDayTypeF.text(),
            self.AnthropometricsSoruceF.text(),
            self.AnthropometricsCPF.text(),
            self.AnthropometricsPAF.text(),
            self.AnthropometricsHtF.text(),
            self.AnthropometricsWtF.text(),
            self.AnthropometricsHCF.text(),
            self.AnthropometricsUACF.text(), 
            self.AnthropometricsTSFF.text(),
            self.AnthropometricsSSFF.text(),
            self.AnthropometricsUSFF.text(),
            self.AnthropometricsSISFF.text(),
            self.AnthropometricsMBSFF.text(),
            self.AnthropometricsUCF.text(),
            self.AnthropometricsEnteredF.text(),
            self.AnthropometricsCommentsF.toPlainText(), 
            )

        self.resetinputs()

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


class NewAnthropometrics():
    def __init__(self, MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC,Entered,Comments):
        pass