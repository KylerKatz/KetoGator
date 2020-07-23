import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QFont, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import *
from datetime import datetime


from EmbedMatplotlib import *
from SpreadSheetAccess import *


class Login (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,200,1280,720)
        self.setWindowTitle("Keto Gator")
        self.setMinimumWidth(1280)

        self.usernamelabel = QLabel("Username")
        self.usernameform = QLineEdit()
        
        self.passwordlabel = QLabel("Password")
        self.passwordform = QLineEdit()
        self.passwordform.setEchoMode(QLineEdit.Password)

        self.loginbutton = QPushButton("Submit")

        self.middlebackground = QFrame()
        self.middlebackground.setStyleSheet("background-color:rgb(12, 76, 173); border:none; color:black")
    
        self.logo = QLabel()
        ui_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(ui_path, "Keto-Gator-V3.png")
        self.logo.setPixmap(QPixmap(img_path)) 


        
        self.mainlayout = QVBoxLayout()
        self.logolayout = QHBoxLayout()

        self.formlayout = QFormLayout()
        self.formlayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.formlayout.setContentsMargins(0,0,0,0)

        self.loginbuttonlayout = QHBoxLayout()
        
        self.formlayout.addRow(self.usernamelabel,self.usernameform)
        self.formlayout.addRow(self.passwordlabel,self.passwordform)
        
        self.logolayout.addWidget(self.logo)
        self.logolayout.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.loginbuttonlayout.addWidget(self.loginbutton)
        self.loginbuttonlayout.setContentsMargins(0,0,0,0)
        
        self.mainlayout.addLayout(self.logolayout)
        self.mainlayout.addLayout(self.formlayout)
        self.mainlayout.addWidget(self.middlebackground)
        self.mainlayout.addLayout(self.loginbuttonlayout)
        self.mainlayout.addWidget(self.loginbutton)
        self.mainlayout.setContentsMargins(400,0,400,0)
        self.mainlayout.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter )
        
        self.setLayout (self.mainlayout)

        self.loginbutton.mousePressEvent = self.handlelogin

    def handlelogin(self,event):
        if(self.usernameform.text().lower() == 'user' and self.passwordform.text().lower() == 'pass'):
            self.close()
            temp = Test()
            temp.show()

        elif(self.usernameform.text()!= '' and self.passwordform.text()!= ''):
            self.popup = QMessageBox.question(self,"Warning","Incorrect Credentials", QMessageBox.Retry | QMessageBox.Close)
            
            if self.popup==QMessageBox.Retry:
                self.usernameform.setText('')
                self.passwordform.setText('')
            if self.popup==QMessageBox.Close:
                sys.exit()

    
class Test (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,200,1280,720)
        self.setWindowTitle("Keto Gator")
        self.setMinimumWidth(1280)
        self.setWindowIcon(QtGui.QIcon("Icon.png"))
        
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
        
        self.namelabel = QLabel("Medical Record Number:")
        self.nameinput = QLineEdit()

   

        self.addpatientbutton = QPushButton("Add New Patient")


        ################### Update Data ###################
        self.selectgraph = QLabel("Select a Graph Type:")
        self.graphselector = QComboBox()
        self.graphselector.addItems(["", "Alertness","Anthropometrics", "Clinic GI Issues","Clinical Labs","Daily Intake",
        "Diet RX","Med Data","Menus","Other Med","Seizure Data","Seizure Ranking","Urine Kt SG","Vitals","VNS"])

        ################### Update Data - Alertness ###################
        self.AlertnessMRNumberL = QLabel("Medical Record Number")
        self.AlertnessMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.AlertnessMRNumberF = QLineEdit()
        self.AlertnessMRNumberF.setMaxLength(10)
        self.AlertnessMRNumberF.setPlaceholderText("Required")
        self.AlertnessMRNumberF.setValidator(QIntValidator())
        
        
        self.AlertnessDateL = QLabel("Date - (MM/DD/YYYY)")
        self.AlertnessDateL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessDateL.setToolTip("Date of collection pertaining to the table or parameter")
        self.AlertnessDateF = QDateEdit()
        self.AlertnessDateF.setDisplayFormat("MM/dd/yyyy")
        self.AlertnessDateF.setDate(datetime.date(datetime.now()))
        
        self.AlertnessDayTypeL = QLabel("Day Type")
        self.AlertnessDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessDayTypeL.setToolTip("Description of date of collection")
        self.AlertnessDayTypeF = QComboBox()
        self.AlertnessDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.AlertnessL = QLabel("Alertness")
        self.AlertnessL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessL.setToolTip("Description of the patients alertness at the clinic visit")
        self.AlertnessF = QTextEdit()

        self.AlertnessActivityL = QLabel("Activity")
        self.AlertnessActivityL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessActivityL.setToolTip("Description of the patients activity at the clinic visit")
        self.AlertnessActivityF = QTextEdit()

        self.AlertnessDevelopmentL = QLabel("Development")
        self.AlertnessDevelopmentL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessDevelopmentL.setToolTip("Description of the patients development at the clinic visit")
        self.AlertnessDevelopmentF = QTextEdit()

        self.AlertnessEnteredL = QLabel("Entered")
        self.AlertnessEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessEnteredL.setToolTip("Person who entered the data initials follwed by date entered i.e. HA-07/22/2016")
        self.AlertnessEnteredF = QLineEdit()
        self.AlertnessEnteredF.setPlaceholderText("Required")


        self.AlertnessCommentsL = QLabel("Comments")
        self.AlertnessCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.AlertnessCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.AlertnessCommentsF = QTextEdit()

        self.AlertnessSaveButton = QPushButton("Save")

        ################### Update Data - Anthropometrics ###################
        self.AnthropometricsMRNumberL = QLabel("Medical Record Number")
        self.AnthropometricsMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.AnthropometricsMRNumberF = QLineEdit()
        self.AnthropometricsMRNumberF.setMaxLength(10)
        self.AnthropometricsMRNumberF.setPlaceholderText("Required")
        self.AnthropometricsMRNumberF.setValidator(QIntValidator())
        

        self.AnthropometricsDateL = QLabel("Date - (MM/DD/YYYY)")
        self.AnthropometricsDateL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsDateL.setToolTip("Date of collection pertaining to the table or parameter")
        self.AnthropometricsDateF = QDateEdit()
        self.AnthropometricsDateF.setDisplayFormat("MM/dd/yyyy")
        self.AnthropometricsDateF.setDate(datetime.date(datetime.now()))

        self.AnthropometricsDayTypeL = QLabel("Day Type")
        self.AnthropometricsDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsDayTypeL.setToolTip("Description of date of collection")
        self.AnthropometricsDayTypeF = QComboBox()
        self.AnthropometricsDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.AnthropometricsSourceL = QLabel("Source")
        self.AnthropometricsSourceL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSourceL.setToolTip("Description of location for data collection which indicates quality of data. The categorical value for this can be found in column I \"Options for categorical variables.\"  \nPatients on the prospective study can have 1,2, or 3 as options. Patients before the prospective study only have 2 and 3 as options. ")
        self.AnthropometricsSoruceF = QComboBox()
        self.AnthropometricsSoruceF.addItems(['', '1 = CRC', '2 = Clinic', '3 = Other (e.g home,school)'])

        self.AnthropometricsCPL = QLabel("Cerebral Palsy Energy Factor")
        self.AnthropometricsCPL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsCPL.setToolTip("Ratio used to determine dietary energy needs in neurologically impaired children. Based on energy needs for height. \nThe catgorical value for this can be found incolumn I \"option for categorical variables.\" ")
        self.AnthropometricsCPF = QComboBox()
        self.AnthropometricsCPF.addItems(['', '15 = Children without motor dysfunction', '14 = Children with motor dysfunction who are ambulator','11 = Children who are nonambulatory'])

        self.AnthropometricsPAL = QLabel("Physical Activity Coefficient")
        self.AnthropometricsPAL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsPAL.setToolTip("The physical activity coefficients are used in the EER equations to estimate energy requirements and are based on ranges of physical activity levels. There are 4 coefficients to describe physcial activity: 1) sedentary=non-ambulatory, mild physical therapy, does not do long periods (30 minutes or more) of physical activities; 2)low-active=physical therapy, ambulatory or active non-ambulatory, performs low intensity activities for 30 minutes or less.  Such activities include leisure walking, playing a musical instrument, or horseback riding (walking); 3) active=walks or runs as means of mobility, brisk walking for 30 minutes or longer, intense physical therapy more than twice a week, playing sports, swimming, etc.; 4) very active=constantly doing physical activities, dancing, climbing hills, jogging, tennis, skating, jumping rope, walking (5 mph).  Values for the categorical variable will be in column I \"Option for categorical variables\"  ")
        
        self.model = QtGui.QStandardItemModel()
        
        self.AnthropometricsPAF = QComboBox()
        self.AnthropometricsPAF.setModel(self.model)
        
        
        self.AnthropometricsPAF2 = QComboBox()
        self.AnthropometricsPAF2.setModel(self.model)
        self.AnthropometricsPAF2.setFixedSize(120,20)

        
        self.PA = {
            '':[''],
        'Males 3-18 years':['1.00 = Sedentary','1.13 = Low Active','1.26 = Active','1.42 = Very Active'], 
        'Males ≥19 years':['1.00 = Sedentary', '1.11 = low Active', '1.25 = Active','1.48 = Very Active'],
        'Females 3-18 years':['1.00 = Sedentary','1.16 = Low Active', '1.31 = Active','1.56 = Very Active'],
        'Females ≥19 years':['1.00 = Sedentary','1.12 = Low Active', '1.27 = Active', '1.45 = Very Active']}



        for k, vals in self.PA.items():
            self.person = QtGui.QStandardItem(k)
            self.model.appendRow(self.person)
            for value in vals:
                self.activity = QtGui.QStandardItem(value)
                self.person.appendRow(self.activity)
        
        self.AnthropometricsPAF.currentIndexChanged.connect(self.updateStateCombo)
        self.updateStateCombo(0)    

        self.AnthropometricsHtL = QLabel("Height - cm")
        self.AnthropometricsHtL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsHtL.setToolTip("Measure of linear growth. It is collected in one of 3 ways for patients: 1) patient standing measured using a stadiometer; 2) \nlying down straight measured from head to heel using measuring tape; 3) lying down segmental measured using measuring tape (head to shoulder, shoulder to hip, hip to knee, knee to heel). \nFor patients lying down, the measurement may be taken on the left or right side of the body depending on the patient, but is most routinely collected on the right side of the body.   ")
        self.AnthropometricsHtF = QLineEdit()
        self.AnthropometricsHtF.setValidator(QDoubleValidator())

        self.AnthropometricsWtL = QLabel("Weight - kg")
        self.AnthropometricsWtL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsWtL.setToolTip("Measure of ponderal growth. It is collected in one of 2 ways for patients: 1) patient standing on a scale; 2) patient is weighed with wheelchair and wheelchair weight is subtracted from first weight.")
        self.AnthropometricsWtF = QLineEdit()
        self.AnthropometricsWtF.setValidator(QDoubleValidator())

        self.AnthropometricsHCL = QLabel("Head Circumference - cm")
        self.AnthropometricsHCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsHCL.setToolTip("Measurement of the head around its largest area. It measures the distance from above the eyebrows and ears and around the back of the head. The average of 3 readings is recorded.")
        self.AnthropometricsHCF = QLineEdit()
        self.AnthropometricsHCF.setValidator(QDoubleValidator())

        self.AnthropometricsUACL = QLabel("Upper Arm Circumference - cm")
        self.AnthropometricsUACL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUACL.setToolTip("The circumference of the upper right arm. Measured at the mid-point between the tip of the shoulder and the tip of the elbow (olecranon process and the acromium). \nPatient's elbow should be flexed to 90 degrees with the palm facing superiorly. The average of 3 readings is recorded.")
        self.AnthropometricsUACF = QLineEdit()
        self.AnthropometricsUACF.setValidator(QDoubleValidator())

        self.AnthropometricsTSFL = QLabel("Triceps Skinfold - mm")
        self.AnthropometricsTSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsTSFL.setToolTip("Triceps skinfold thickness measured with a skinfold caliper. Measured at the back of the midpoint of the upper right arm. \nPatient should stand or lie down with right arm hanging loosely by the side. The average of 3 readings is recorded.")
        self.AnthropometricsTSFF = QLineEdit()
        self.AnthropometricsTSFF.setValidator(QDoubleValidator())

        self.AnthropometricsSSFL = QLabel("Subscapular Skinfold - mm")
        self.AnthropometricsSSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSSFL.setToolTip("Subscapular skinfold thickness measured with a skinfold caliper. Measured 1 cm below the inferior angle of the right scapula (shoulder blade). The average of 3 readings is recorded.")
        self.AnthropometricsSSFF = QLineEdit()
        self.AnthropometricsSSFF.setValidator(QDoubleValidator())

        self.AnthropometricsUSFL = QLabel("Umbilicus Skinfold - mm")
        self.AnthropometricsUSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUSFL.setToolTip("Umbilicus skinfold thickness measured with a skinfold caliper. The vertical umbilicus skinfold is measured by pinching the abdominal fat fold vertically \nabout 2.5 cm to the right of the patient’s umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsUSFF = QLineEdit()
        self.AnthropometricsUSFF.setValidator(QDoubleValidator())

        self.AnthropometricsSISFL = QLabel("Suprailiac Skinfold - mm")
        self.AnthropometricsSISFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSISFL.setToolTip("Suprailiac skinfold thickness measured with a skinfold caliper. The vertical supra iliac skinfolds are measured by pinching the side fatfolds vertically \nat the mid-axilary line and at the level of the umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsSISFF = QLineEdit()
        self.AnthropometricsSISFF.setValidator(QDoubleValidator())

        self.AnthropometricsMBSFL = QLabel("Midback Skinfold - mm")
        self.AnthropometricsMBSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsMBSFL.setToolTip("Mid back skinfold thickness measured with a skinfold caliper. The vertical mid-back skinfold is measured by pinching the back fat fold about 2.5 cm to the \nright of the spinal column at the level of the umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsMBSFF = QLineEdit()
        self.AnthropometricsMBSFF.setValidator(QDoubleValidator())
        

        self.AnthropometricsUCL = QLabel("Umbilical Circumference - cm")
        self.AnthropometricsUCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUCL.setToolTip("Circumference of the mid-section of the body at the umbilicus (belly button), perpendicular to the long axis of the body. The average of 3 readings is recorded.")
        self.AnthropometricsUCF = QLineEdit()
        self.AnthropometricsUCF.setValidator(QDoubleValidator())

        self.AnthropometricsEnteredL = QLabel("Entered")
        self.AnthropometricsEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.AnthropometricsEnteredF = QLineEdit()
        self.AnthropometricsEnteredF.setPlaceholderText("Required")


        self.AnthropometricsCommentsL = QLabel("Comments")
        self.AnthropometricsCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.AnthropometricsCommentsF = QTextEdit()

        self.AnthropometricsSaveButton = QPushButton("Save")


        ################### Update Data - Clinic GI Issues ###################
        self.ClinicGIMRNumberL = QLabel("Medical Record Number")
        self.ClinicGIMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.ClinicGIMRNumberF = QLineEdit()
        self.ClinicGIMRNumberF.setMaxLength(10)
        self.ClinicGIMRNumberF.setPlaceholderText("Required")
        
        self.ClinicGIDateL = QLabel("Date - (MM/DD/YYYY)")
        self.ClinicGIDateL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIDateL.setToolTip("Date of collection pertaining to the table or parameter")
        self.ClinicGIDateF = QDateEdit()
        self.ClinicGIDateF.setDisplayFormat("MM/dd/yyyy")
        self.ClinicGIDateF.setDate(datetime.date(datetime.now()))
        
        self.ClinicGIDayTypeL = QLabel("Day Type")
        self.ClinicGIDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIDayTypeL.setToolTip("Description of date of collection")
        self.ClinicGIDayTypeF = QComboBox()
        self.ClinicGIDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.ClinicGIConstL = QLabel("Clinic Constipation")
        self.ClinicGIConstL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIConstL.setToolTip("Response is yes or no for constipation concerns brought up at clinic")
        self.ClinicGIConstF = QComboBox()
        self.ClinicGIConstF.addItems(['','Yes','No'])

        self.ClinicGIDiaL = QLabel("Clinic Diarrhea")
        self.ClinicGIDiaL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIDiaL.setToolTip("Response is yes or no for diarrhea concerns brought up at clinic")
        self.ClinicGIDiaF = QComboBox()
        self.ClinicGIDiaF.addItems(['','Yes','No'])

        self.ClinicGIVomL = QLabel("Clinic Vomitting")
        self.ClinicGIVomL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIVomL.setToolTip("Response is yes or no for vomitting concerns brought up at clinic")
        self.ClinicGIVomF = QComboBox()
        self.ClinicGIVomF.addItems(['','Yes','No'])

        self.ClinicGINauseaL = QLabel("Clinic Nausea")
        self.ClinicGINauseaL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGINauseaL.setToolTip("Response is yes or no for nausea concerns brought up at clinic")
        self.ClinicGINauseaF = QComboBox()
        self.ClinicGINauseaF.addItems(['','Yes','No'])

        self.ClinicGIGagL = QLabel("Clinic Gagging Retching")
        self.ClinicGIGagL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIGagL.setToolTip("Response is yes or no for gagging/retching concerns brought up at clinic")
        self.ClinicGIGagF = QComboBox()
        self.ClinicGIGagF.addItems(['','Yes','No'])

        self.ClinicGINissenL = QLabel("Clinic Nissen")
        self.ClinicGINissenL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGINissenL.setToolTip("Nissen fundoplication, sometimes known as laparoscopic fundoplication \nwhen performed via laparoscopic surgery, is a surgical procedure to treat gastroesophageal \nreflux disease (GERD) and hiatal hernia. Most patients with a G-tube will have a Nissen")
        self.ClinicGINissenF = QComboBox()
        self.ClinicGINissenF.addItems(['','Yes','No'])

        self.ClinicGIConstDesL = QLabel("Clinic Description - Constipation")
        self.ClinicGIConstDesL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIConstDesL.setToolTip("Description of constipation concerns brought up at clinic")
        self.ClinicGIConstDesF = QTextEdit()

        self.ClinicGIDiaDesL = QLabel("Clinic Description - Diarrhea")
        self.ClinicGIDiaDesL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIDiaDesL.setToolTip("Description of diarrhea concerns brought up at clinic")
        self.ClinicGIDiaDesF = QTextEdit()

        self.ClinicGIVomDesL = QLabel("Clinic Description - Vomitting")
        self.ClinicGIVomDesL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIVomDesL.setToolTip("Description of vomitting concerns brought up at clinic")
        self.ClinicGIVomDesF = QTextEdit()

        self.ClinicGINauseaDesL = QLabel("Clinic Description - Nausea")
        self.ClinicGINauseaDesL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGINauseaDesL.setToolTip("Description of nausea concerns brought up at clinic")
        self.ClinicGINauseaDesF = QTextEdit()

        self.ClinicGIGagDesL = QLabel("Clinic Description - Gagging Retching")
        self.ClinicGIGagDesL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIGagDesL.setToolTip("Description of gagging/retching concerns brought up at clinic")
        self.ClinicGIGagDesF = QTextEdit()

        self.ClinicGIEnteredL = QLabel("Entered")
        self.ClinicGIEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGIEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.ClinicGIEnteredF = QLineEdit()
        self.ClinicGIEnteredF.setPlaceholderText("Required")

        self.ClinicGICommentsL = QLabel("Comments")
        self.ClinicGICommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGICommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.ClinicGICommentsF = QTextEdit()

        self.ClinicGISaveButton = QPushButton("Save")
        
        ################### Update Data - Clinical Labs ###################

        ################### Update Data - Daily Intake ###################
        self.DailyIntakeMRNumberL = QLabel("Medical Record Number")
        self.DailyIntakeMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.DailyIntakeMRNumberF = QLineEdit()
        self.DailyIntakeMRNumberF.setMaxLength(10)
        self.DailyIntakeMRNumberF.setPlaceholderText("Required")
        
        self.DailyIntakeDateL = QLabel("Date - (MM/DD/YYYY)")
        self.DailyIntakeDateL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeDateL.setToolTip("Date indicated on records")
        self.DailyIntakeDateF = QDateEdit()
        self.DailyIntakeDateF.setDisplayFormat("MM/dd/yyyy")
        self.DailyIntakeDateF.setDate(datetime.date(datetime.now()))
        
        self.DailyIntakeDayTypeL = QLabel("Day Type")
        self.DailyIntakeDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeDayTypeL.setToolTip("Description of date of collection")
        self.DailyIntakeDayTypeF = QComboBox()
        self.DailyIntakeDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT'])

        self.DailyIntakePKTNUML = QLabel("Precision Ketogenic Therapy Recipe Number")
        self.DailyIntakePKTNUML.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakePKTNUML.setToolTip("The PKT recipe number is a number given to each different PKT recipe and supplement, and it is a unique number. \nWe use the information given to us by records from the family in order to create and enter a PKT recipe number for each meal consumed by the patient.")
        self.DailyIntakePKTNUMF = QLineEdit()
        self.DailyIntakePKTNUMF.setMaxLength(5)
        self.DailyIntakePKTNUMF.setPlaceholderText("Required")


        self.DailyIntakeDataQualityDietL = QLabel("Data Quality Diet")
        self.DailyIntakeDataQualityDietL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeDataQualityDietL.setToolTip("Data quality is entered from a list of categorical values that allows for us to indicate the quality of the data and its source.")
        self.DailyIntakeDataQualityDietF = QComboBox()
        self.DailyIntakeDataQualityDietF.addItems(['1 = Meals consumed by the patient came from our PKT program AND the data comes from records kept by caregivers', 
        '2 = The data comes from records kept by the caregivers; however, we do not have a copy of the patient’s cookbook or meals are not from our PKT program', 
        '3 = Meals consumed by the patient came from our PKT program; however, data was not provided on records by the family',
        '4 = We do not have a copy of the patient’s cookbook or meals are not from our PKT program AND data was not provided on records by the family',
        '5 = The patient is off of PKT and there are no records'])

        self.DailyIntakeDayQualityDietL = QLabel("Day Quality Diet")
        self.DailyIntakeDayQualityDietL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeDayQualityDietL.setToolTip("Day quality is a list of categorical values that allows us to indicate the quality or health of the patient’s day in terms of nutrient intake.")
        self.DailyIntakeDayQualityDietF = QComboBox()
        self.DailyIntakeDayQualityDietF.addItems(['1 = The patient received 100% of what was prescribed to them', 
        '2 = Deviations due to illness',
        '3 = Unauthorized deviations due to improper administration of PKT','4 = Deviations due to a prescribed change', 
        '5 = There is missing data so no assumptions can be made about day quality'])

        self.DailyIntakeEnteredL = QLabel("Entered")
        self.DailyIntakeEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.DailyIntakeEnteredF = QLineEdit()
        self.DailyIntakeEnteredF.setPlaceholderText("Required")

        self.DailyIntakeCommentsL = QLabel("Comments")
        self.DailyIntakeCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.DailyIntakeCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.DailyIntakeCommentsF = QTextEdit()

        self.DailyIntakeSaveButton = QPushButton("Save")
        
        ################### Update Data - Diet RX ###################
        self.DietRXMRNumberL = QLabel("Medical Record Number")
        self.DietRXMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.DietRXMRNumberF = QLineEdit()
        self.DietRXMRNumberF.setMaxLength(10)
        self.DietRXMRNumberF.setPlaceholderText("Required")
        self.DietRXMRNumberF.setValidator(QIntValidator())
        
        
        self.DietRXDateL = QLabel("Date - (MM/DD/YYYY)")
        self.DietRXDateL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXDateL.setToolTip("Date indicated on records")
        self.DietRXDateF = QDateEdit()
        self.DietRXDateF.setDisplayFormat("MM/dd/yyyy")
        self.DietRXDateF.setDate(datetime.date(datetime.now()))
        
        self.DietRXDayTypeL = QLabel("Day Type")
        self.DietRXDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXDayTypeL.setToolTip("Description of date of collection")
        self.DietRXDayTypeF = QComboBox()
        self.DietRXDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.DietRXROFL = QLabel("Route Of Feeding")
        self.DietRXROFL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXROFL.setToolTip("Enter the ROF according to the options for categorical variables column")
        self.DietRXROFF = QComboBox()
        self.DietRXROFF.addItems(['TF = Tube Feeder', 'Oral = Oral Feeder', 'Both = Both Tube and Oral Feeder'])

        self.DietRXRFCDL = QLabel("Reason For Change Diet")
        self.DietRXRFCDL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXRFCDL.setToolTip("Enter the reason for change according to the options for categorical variables column")
        self.DietRXRFCDF = QComboBox()
        self.DietRXRFCDF.addItems(['0 = No diet change','1 = Unspecified','2 = Height','3 = Weight','4 = Seizures','5 = Illness','6 = Family, patients or doctor request',
        '7 = Hunger','8 = Height and weight','9 = GI issues','10 = Weaning off diet','11 = Weight and seizures','12 = Too ketotic','13 = Height and seizures','14 = low ketosis',
        '15 = Low blood sugar','16 = Low albumin','17 = Abnormal lab values','18 = Meal palatability','19 = Protein closer to RDA','20 = Activity','21 = Weight and ketosis',
        '22 = Constipation'])
        
        self.DietRXSnackCalL = QLabel("Total Snack Calories Prescribed - (1 Decimal)")
        self.DietRXSnackCalL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXSnackCalL.setToolTip("Total snack calories for the entire day")
        self.DietRXSnackCalF = QLineEdit()
        self.DietRXSnackCalF.setMaxLength(5)
        self.DietRXSnackCalF.setValidator(QDoubleValidator())
        self.DietRXSnackCalF.setPlaceholderText("Can be blank if the patient does not receive a snack")

        self.DietRXSnackRatioL = QLabel("Snack Ratio Prescribed - (2 Decimals)")
        self.DietRXSnackRatioL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXSnackRatioL.setToolTip("Snack PKT ratio precribed per day")
        self.DietRXSnackRatioF = QLineEdit()
        self.DietRXSnackRatioF.setMaxLength(4)
        self.DietRXSnackRatioF.setValidator(QDoubleValidator())
        self.DietRXSnackRatioF.setPlaceholderText("Can be blank if the patient does not receive a snack")

        self.DietRXSnackNumberL = QLabel("Snack Number Prescribed")
        self.DietRXSnackNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXSnackNumberL.setToolTip("Total number of snacks precribed per day")
        self.DietRXSnackNumberF = QLineEdit()
        self.DietRXSnackNumberF.setMaxLength(2)
        self.DietRXSnackNumberF.setValidator(QIntValidator())
        self.DietRXSnackNumberF.setPlaceholderText("Can be blank if the patient does not receive a snack")

        self.DietRXMealNumberL = QLabel("Meal Number Prescribed")
        self.DietRXMealNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXMealNumberL.setToolTip("Total number of meals prescribed per day")
        self.DietRXMealNumberF = QLineEdit()
        self.DietRXMealNumberF.setMaxLength(2)
        self.DietRXMealNumberF.setPlaceholderText("Required")
        self.DietRXMealNumberF.setValidator(QIntValidator())

        self.DietRXMealRatioL = QLabel("Meal Ratio Prescribed - (2 Decimals)")
        self.DietRXMealRatioL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXMealRatioL.setToolTip("Meal PKT ratio of amount of fat per amount of carbohydrate plus amount of protein prescribed per day")
        self.DietRXMealRatioF = QLineEdit()
        self.DietRXMealRatioF.setMaxLength(4)
        self.DietRXMealRatioF.setPlaceholderText("Required")
        self.DietRXMealRatioF.setValidator(QDoubleValidator())
        
        self.DietRXCalL = QLabel("Calories Prescribed - (2 Decimals)")
        self.DietRXCalL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXCalL.setToolTip("Total calories prescribed per day")
        self.DietRXCalF = QLineEdit()
        self.DietRXCalF.setMaxLength(7)
        self.DietRXCalF.setPlaceholderText("Required")
        self.DietRXCalF.setValidator(QDoubleValidator())

        self.DietRXProL = QLabel("Protein Prescribed - (2 Decimals)")
        self.DietRXProL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXProL.setToolTip("Perecent of intake versus recommended intake for proline")
        self.DietRXProF = QLineEdit()
        self.DietRXProF.setMaxLength(5)
        self.DietRXProF.setPlaceholderText("Required")
        self.DietRXProF.setValidator(QDoubleValidator())

        self.DietRXEnteredL = QLabel("Entered")
        self.DietRXEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.DietRXEnteredF = QLineEdit()
        self.DietRXEnteredF.setPlaceholderText("Required")

        self.DietRXCommentsL = QLabel("Comments")
        self.DietRXCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.DietRXCommentsF = QTextEdit()

        self.DietRXSaveButton = QPushButton("Save")

        ################### Update Data - Med Data ###################
        self.MedDataMRNumberL = QLabel("Medical Record Number")
        self.MedDataMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.MedDataMRNumberF = QLineEdit()
        self.MedDataMRNumberF.setMaxLength(10)
        self.MedDataMRNumberF.setPlaceholderText("Required")
        self.MedDataMRNumberF.setValidator(QIntValidator())
        
        self.MedDataDateL = QLabel("Date - (MM/DD/YYYY)")
        self.MedDataDateL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataDateL.setToolTip("Date indicated on records")
        self.MedDataDateF = QDateEdit()
        self.MedDataDateF.setDisplayFormat("MM/dd/yyyy")
        self.MedDataDateF.setDate(datetime.date(datetime.now()))
        
        self.MedDataDayTypeL = QLabel("Day Type")
        self.MedDataDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataDayTypeL.setToolTip("Description of date of collection")
        self.MedDataDayTypeF = QComboBox()
        self.MedDataDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.MedDataNDIDL = QLabel("Nutrition Facts Database Identification")
        self.MedDataNDIDL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataNDIDL.setToolTip("NDID is the specific number assigned to each food, suplement, or medication product in the Nutrition Facts Database")
        self.MedDataNDIDF = QLineEdit()
        self.MedDataNDIDF.setMaxLength(8)
        
        self.MedDataMedIDL = QLabel("Medication ID")
        self.MedDataMedIDL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataMedIDL.setToolTip("ID number given to each generic or brand name AED, see med ranking sheet in G:\MySQL Database\Meds\Med Ranking for list of ID numbers")
        self.MedDataMedIDF = QLineEdit()
        self.MedDataMedIDF.setMaxLength(8)
        self.MedDataMedIDF.setPlaceholderText("Required")

        self.MedDataRFCML = QLabel("Reason For Change Med")
        self.MedDataRFCML.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataRFCML.setToolTip("Reason for change in medication prescription or administration. ")
        self.MedDataRFCMF = QComboBox()
        self.MedDataRFCMF.addItems(['0 = No change and initiation (include comment for initiation)','1 = Unspecified','2 = Increased seizures','3 = Decreased seizures','4 = Change in seizure type',
        '5 = Carbohydrate content','6 = Weaning','7 = Alertness','8 = Hospitalization','9 = Efficacy','10 = Adverse effects','11 = Family, patient, or doctor request','12 = Weight',
        '13 = Age','14 = GI issues','15 = Non-compliant change by family','16 = Facilitate sleep'])

        self.MedDataProdNameL = QLabel("Product Name")
        self.MedDataProdNameL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataProdNameL.setToolTip("Name of food, supplement or medication product that is assigned to the NDID")
        self.MedDataProdNameF = QLineEdit()
        self.MedDataProdNameF.setMaxLength(100)

        self.MedDataDailyDoseL = QLabel("Daily Med Dose - (Mg)")
        self.MedDataDailyDoseL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataDailyDoseL.setToolTip("Total dose of AED per day in mg either prescribed or consumed")
        self.MedDataDailyDoseF = QLineEdit()
        self.MedDataDailyDoseF.setMaxLength(6)
        self.MedDataDailyDoseF.setValidator(QDoubleValidator())

        self.MedDataMedDosesL = QLabel("Med Doses")
        self.MedDataMedDosesL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataMedDosesL.setToolTip("Total number of doses AED per day either presribed or consumed")
        self.MedDataMedDosesF = QLineEdit()
        self.MedDataMedDosesF.setMaxLength(2)
        self.MedDataMedDosesF.setValidator(QIntValidator())

        self.MedDataMedCommentsL = QLabel("Med Comments")
        self.MedDataMedCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataMedCommentsL.setToolTip("Additional comments on AED prescription")
        self.MedDataMedCommentsF = QTextEdit()
                
        self.MedDataEnteredL = QLabel("Entered")
        self.MedDataEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.MedDataEnteredF = QLineEdit()
        self.MedDataEnteredF.setPlaceholderText("Required")

        self.MedDataCommentsL = QLabel("Comments")
        self.MedDataCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.MedDataCommentsF = QTextEdit()

        self.MedDataSaveButton = QPushButton("Save")

        ################### Update Data - Menus ###################
        self.MenusMRNumberL = QLabel("Medical Record Number")
        self.MenusMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.MenusMRNumberF = QLineEdit()
        self.MenusMRNumberF.setMaxLength(10)
        self.MenusMRNumberF.setPlaceholderText("Required")
        self.MenusMRNumberF.setValidator(QIntValidator())
        
        self.MenusDateL = QLabel("Date - (MM/DD/YYYY)")
        self.MenusDateL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusDateL.setToolTip("Date indicated on records")
        self.MenusDateF = QDateEdit()
        self.MenusDateF.setDisplayFormat("MM/dd/yyyy")
        self.MenusDateF.setDate(datetime.date(datetime.now()))

        self.MenusCalPrcntL = QLabel("Calories Prescribed - (kcal)")
        self.MenusCalPrcntL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusCalPrcntL.setToolTip("Total calories prescribed per day")
        self.MenusCalPrcntF = QLineEdit()
        self.MenusCalPrcntF.setMaxLength(6)
        self.MenusCalPrcntF.setPlaceholderText("Required")
        self.MenusCalPrcntF.setValidator(QDoubleValidator())

        self.MenusProcntPrcntL = QLabel("Protein Prescribed - (g)")
        self.MenusProcntPrcntL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusProcntPrcntL.setToolTip("Percent of intake versus recommended intake for proline")
        self.MenusProcntPrcntF = QLineEdit()
        self.MenusProcntPrcntF.setMaxLength(4)
        self.MenusProcntPrcntF.setPlaceholderText("Required")
        self.MenusProcntPrcntF.setValidator(QDoubleValidator())

        self.MenusRatioPrL = QLabel("Ratio Prescribed")
        self.MenusRatioPrL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRatioPrL.setToolTip("Meal PKT ratio precribed of amount of fat per amount of carbohydrates plus amount of protein")
        self.MenusRatioPrF = QLineEdit()
        self.MenusRatioPrF.setMaxLength(3)
        self.MenusRatioPrF.setPlaceholderText("Required")
        self.MenusRatioPrF.setValidator(QDoubleValidator())

        self.MenusMealNumberL = QLabel("Meal Number Prescribed")
        self.MenusMealNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusMealNumberL.setToolTip("Total number of meals prescribed per day")
        self.MenusMealNumberF = QLineEdit()
        self.MenusMealNumberF.setMaxLength(2)
        self.MenusMealNumberF.setPlaceholderText("Required")
        self.MenusMealNumberF.setValidator(QIntValidator())
        
        self.MenusSnackNumberL = QLabel("Snack Number Prescribed")
        self.MenusSnackNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusSnackNumberL.setToolTip("Total number of snacks precribed per day")
        self.MenusSnackNumberF = QLineEdit()
        self.MenusSnackNumberF.setMaxLength(2)
        self.MenusSnackNumberF.setPlaceholderText("Cell can be blank if the patient does not receive a snack. Otherwise it is required")
        self.MenusSnackNumberF.setValidator(QIntValidator())

        self.MenusRecipeNameL = QLabel("PKT Recipe Name")
        self.MenusRecipeNameL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRecipeNameL.setToolTip("Name of the PKT recipe which includes the PKT recipe number, number of calories, PKT ratio, amount of protein, number of meals and the number of snacks")
        self.MenusRecipeNameF = QLineEdit()
        self.MenusRecipeNameF.setMaxLength(100)
        # self.MenusRecipeNameF.setPlaceholderText("Required")

        self.MenusRecipeNumberL = QLabel("PKT Recipe Number")
        self.MenusRecipeNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRecipeNumberL.setToolTip("number given to each different pkt recipe and supplement and it is a unique number. \n1) if the consumed nutrients are a prescribed meal then it gets a whole number and/or a decimal point, 2) if the consumed nutrients are a deviation of a prescribed meal then it \ngets a whole number followed by a letter (starting with the letter a) to denote a deviation of the meal, if the consumed food is a supplement then it gets the letter s followed by a whole number \nstarting with the number 1, if the consumed nutrients are a deviation of a supplement then it gets the letter s followed by a whole number started with the number 1 and followed \nby a letter (starting with the letter a) to denote a deviation in the supplement")
        self.MenusRecipeNumberF = QLineEdit()
        self.MenusRecipeNumberF.setMaxLength(5)

        self.MenusRecipeIngredientAmountL = QLabel("PKT Recipe Ingredient Amount - (2 Decimals, g)")
        self.MenusRecipeIngredientAmountL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRecipeIngredientAmountL.setToolTip("Amount of ingredient consumed in grams, unless it is a supplement then the number of servings is entered")
        self.MenusRecipeIngredientAmountF = QLineEdit()
        self.MenusRecipeIngredientAmountF.setMaxLength(6)
        self.MenusRecipeIngredientAmountF.setValidator(QDoubleValidator())
        
        self.MenusNDIDL = QLabel("Nutrition Facts Database Identification")
        self.MenusNDIDL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusNDIDL.setToolTip("NDID is the specific number assigned to each food, suplement, or medication product in the Nutrition Facts Database")
        self.MenusNDIDF = QLineEdit()
        self.MenusNDIDF.setMaxLength(8)

        self.MenusProdNameL = QLabel("Product Name")
        self.MenusProdNameL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusProdNameL.setToolTip("Name of food, supplement or medication product that is assigned to the NDID")
        self.MenusProdNameF = QLineEdit()
        self.MenusProdNameF.setMaxLength(100)
        
        self.MenusRecipeTypeL = QLabel("Recipe Type")
        self.MenusRecipeTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRecipeTypeL.setToolTip("Recipe type indicated whether the recipe is for breakfast, lunch, dinner or a snack")
        self.MenusRecipeTypeF = QComboBox()
        self.MenusRecipeTypeF.addItems(['1 = Prescribed meal','2 = Prescribed snack','3 = Deviation meal', '4 = Deviation snack', '5 = Other deviation', '6 = Dietary supplement or medication'])

        self.MenusEnteredL = QLabel("Entered")
        self.MenusEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.MenusEnteredF = QLineEdit()
        self.MenusEnteredF.setPlaceholderText("Required")

        self.MenusCommentsL = QLabel("Comments")
        self.MenusCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.MenusCommentsF = QTextEdit()

        self.MenusSaveButton = QPushButton("Save")

        ################### Update Data - Other Med ###################
        self.OtherMedMRNumberL = QLabel("Medical Record Number")
        self.OtherMedMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.OtherMedMRNumberF = QLineEdit()
        self.OtherMedMRNumberF.setMaxLength(10)
        self.OtherMedMRNumberF.setPlaceholderText("Required")
        self.OtherMedMRNumberF.setValidator(QIntValidator())
        
        self.OtherMedDateL = QLabel("Date - (MM/DD/YYYY)")
        self.OtherMedDateL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedDateL.setToolTip("Date indicated on records")
        self.OtherMedDateF = QDateEdit()
        self.OtherMedDateF.setDisplayFormat("MM/dd/yyyy")
        self.OtherMedDateF.setDate(datetime.date(datetime.now()))
        
        self.OtherMedNDIDL = QLabel("Nutrition Facts Database Identification")
        self.OtherMedNDIDL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedNDIDL.setToolTip("NDID is the specific number assigned to each food, suplement, or medication product in the Nutrition Facts Database")
        self.OtherMedNDIDF = QLineEdit()
        self.OtherMedNDIDF.setMaxLength(8)

        self.OtherMedProdNameL = QLabel("Product Name")
        self.OtherMedProdNameL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedProdNameL.setToolTip("Name of food, supplement or medication product that is assigned to the NDID")
        self.OtherMedProdNameF = QLineEdit()
        self.OtherMedProdNameF.setMaxLength(100)

        self.OtherMedMedAmountL = QLabel("Medication Amount")
        self.OtherMedMedAmountL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedMedAmountF = QLineEdit()
        self.OtherMedMedAmountF.setValidator(QIntValidator())

        self.OtherMedMedUnitL = QLabel("Medication Unit")
        self.OtherMedMedUnitL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedMedUnitF = QLineEdit()
        
        self.OtherMedEnteredL = QLabel("Entered")
        self.OtherMedEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.OtherMedEnteredF = QLineEdit()
        self.OtherMedEnteredF.setPlaceholderText("Required")

        self.OtherMedCommentsL = QLabel("Comments")
        self.OtherMedCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.OtherMedCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.OtherMedCommentsF = QTextEdit()

        self.OtherMedSaveButton = QPushButton("Save")

        ################### Update Data - Seizure Data ###################
        self.SeizureDataMRNumberL = QLabel("Medical Record Number")
        self.SeizureDataMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.SeizureDataMRNumberF = QLineEdit()
        self.SeizureDataMRNumberF.setMaxLength(10)
        self.SeizureDataMRNumberF.setPlaceholderText("Required")
        self.SeizureDataMRNumberF.setValidator(QIntValidator())
        
        self.SeizureDataDateL = QLabel("Date - (MM/DD/YYYY)")
        self.SeizureDataDateL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataDateL.setToolTip("Date indicated on records")
        self.SeizureDataDateF = QDateEdit()
        self.SeizureDataDateF.setDisplayFormat("MM/dd/yyyy")
        self.SeizureDataDateF.setDate(datetime.date(datetime.now()))
        
        self.SeizureDataDayTypeL = QLabel("Day Type")
        self.SeizureDataDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataDayTypeL.setToolTip("Description of date of collection")
        self.SeizureDataDayTypeF = QComboBox()
        self.SeizureDataDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.SeizureDataDataQualityL = QLabel("Data Quality Seizure")
        self.SeizureDataDataQualityL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataDataQualityL.setToolTip("Quality of day pertaining to the options for categorical variables column")
        self.SeizureDataDataQualityF = QComboBox()
        self.SeizureDataDataQualityF.addItems(['1 = Record', '2 = Recall', '3 = Input'])

        self.SeizureDataSeizureSeverityL = QLabel("Seizure Severity")
        self.SeizureDataSeizureSeverityL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureSeverityL.setToolTip("Severity of seizure as written by caregiver")
        self.SeizureDataSeizureSeverityF = QLineEdit()
        self.SeizureDataSeizureSeverityF.setMaxLength(4)

        self.SeizureDataSeizureLengthL = QLabel("Seizure Length - (s)")
        self.SeizureDataSeizureLengthL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureLengthL.setToolTip("Length of seizure as written by caregiver, record in seconds")
        self.SeizureDataSeizureLengthF = QLineEdit()
        self.SeizureDataSeizureLengthF.setMaxLength(4)

        self.SeizureDataSeizureTypeL = QLabel("Seizure Type")
        self.SeizureDataSeizureTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureTypeL.setToolTip("Follow the entry instructions: The caregiver, when possible, described and ranked each seizure type. \nNeurologist classification and/or supporting literature was used to assign ranking points to each seizure types if caregivers ranking and description of seizure type did not exist. \nRanking points 0 through the maximum value were assigned to each seizure type with the maximum value being the most severe and 0 being seizure free. \nThe following scale, provided by the neurologists and/or supporting literature,\n was used to assign ranking points to seizure types: tonic clonic or generalized tonic clonic received the maximum number of points, complex partial and atonic seizures received the second highest value, myoclonic seizures received half of the maximum value, \nsimple partial seizures received the second lowest value, and absence seizures and infantile spasms received 1 point. Enter a letter or number that is associated with the seizure type \nand write the description in the notes section. Enter 0 to indicate seizure freedom. Enter each code in a separate row with SEIZURE TYPE in the SEIZURE_PARAMETER column")
        self.SeizureDataSeizureTypeF = QLineEdit()
        self.SeizureDataSeizureTypeF.setMaxLength(4)
        
        self.SeizureDataSeizureVariableL = QLabel("Seizure Variable")
        self.SeizureDataSeizureVariableL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureVariableL.setToolTip("Seizure variables as recorded by caregivers")
        self.SeizureDataSeizureVariableF = QLineEdit()
        self.SeizureDataSeizureVariableF.setMaxLength(4)

        self.SeizureDataSeizureNumberL = QLabel("Seizure Number")
        self.SeizureDataSeizureNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureNumberL.setToolTip("Seizure number as recorded by caregivers from records or recall")
        self.SeizureDataSeizureNumberF = QLineEdit()
        self.SeizureDataSeizureNumberF.setMaxLength(4)

        self.SeizureDataSeizureClusterL = QLabel("Seizure Cluster")
        self.SeizureDataSeizureClusterL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataSeizureClusterL.setToolTip("Clusters of seizrues within an event as written by caregiver")
        self.SeizureDataSeizureClusterF = QLineEdit()
        self.SeizureDataSeizureClusterF.setMaxLength(4)
        self.SeizureDataSeizureClusterF.setValidator(QIntValidator())
        
        self.SeizureDataEnteredL = QLabel("Entered")
        self.SeizureDataEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.SeizureDataEnteredF = QLineEdit()
        self.SeizureDataEnteredF.setPlaceholderText("Required")

        self.SeizureDataCommentsL = QLabel("Comments")
        self.SeizureDataCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureDataCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.SeizureDataCommentsF = QTextEdit()

        self.SeizureDataSaveButton = QPushButton("Save")

        ################### Update Data - Seizure Ranking ###################
        self.SeizureRankingMRNumberL = QLabel("Medical Record Number")
        self.SeizureRankingMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.SeizureRankingMRNumberF = QLineEdit()
        self.SeizureRankingMRNumberF.setMaxLength(10)
        self.SeizureRankingMRNumberF.setPlaceholderText("Required")
        self.SeizureRankingMRNumberF.setValidator(QIntValidator())

        self.SeizureRankingSeizureParameterL = QLabel("Seizure Parameter")
        self.SeizureRankingSeizureParameterL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingSeizureParameterL.setToolTip("General description of seizures, including severity, seizure length, seizure type, seizure variables, seizure cluster")
        self.SeizureRankingSeizureParameterF = QLineEdit()
        self.SeizureRankingSeizureParameterF.setMaxLength(6)
        
        self.SeizureRankingSeizureEntryL = QLabel("Seizure Entry")
        self.SeizureRankingSeizureEntryL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingSeizureEntryL.setToolTip("Code as recorded by caregivers")
        self.SeizureRankingSeizureEntryF = QLineEdit()
        self.SeizureRankingSeizureEntryF.setMaxLength(6)

        self.SeizureRankingSeizureRankingL = QLabel("Seizure Ranking")
        self.SeizureRankingSeizureRankingL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingSeizureRankingL.setToolTip("Seizure ranking point associated with code provided by caregivers")
        self.SeizureRankingSeizureRankingF = QLineEdit()
        self.SeizureRankingSeizureRankingF.setMaxLength(6)
        self.SeizureRankingSeizureRankingF.setValidator(QIntValidator())

        self.SeizureRankingEnteredL = QLabel("Entered")
        self.SeizureRankingEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.SeizureRankingEnteredF = QLineEdit()
        self.SeizureRankingEnteredF.setPlaceholderText("Required")

        self.SeizureRankingCommentsL = QLabel("Comments")
        self.SeizureRankingCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.SeizureRankingCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.SeizureRankingCommentsF = QTextEdit()

        self.SeizureRankingSaveButton = QPushButton("Save")

        ################### Update Data - Urine Kt SG ###################
        self.UrineKtSGMRNumberL = QLabel("Medical Record Number")
        self.UrineKtSGMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.UrineKtSGMRNumberF = QLineEdit()
        self.UrineKtSGMRNumberF.setMaxLength(10)
        self.UrineKtSGMRNumberF.setPlaceholderText("Required")
        self.UrineKtSGMRNumberF.setValidator(QIntValidator())
        
        self.UrineKtSGDateL = QLabel("Date - (MM/DD/YYYY)")
        self.UrineKtSGDateL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGDateL.setToolTip("Date indicated on records")
        self.UrineKtSGDateF = QDateEdit()
        self.UrineKtSGDateF.setDisplayFormat("MM/dd/yyyy")
        self.UrineKtSGDateF.setDate(datetime.date(datetime.now()))
        
        self.UrineKtSGDayTypeL = QLabel("Day Type")
        self.UrineKtSGDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGDayTypeL.setToolTip("Description of date of collection")
        self.UrineKtSGDayTypeF = QComboBox()
        self.UrineKtSGDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

        self.UrineKtSGUrineKtL = QLabel("Urine Ketones - (1 Decimal)")
        self.UrineKtSGUrineKtL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGUrineKtL.setToolTip("Urine ketone value from daily records from caregivers")
        self.UrineKtSGUrineKtF = QLineEdit()
        self.UrineKtSGUrineKtF.setMaxLength(7)
        self.UrineKtSGUrineKtF.setValidator(QDoubleValidator())

        self.UrineKtSGUrineSGL = QLabel("Urine Specific Gravity - (5 Decimals)")
        self.UrineKtSGUrineSGL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGUrineSGL.setToolTip("Urine specific gravity value from daily records from caregivers")
        self.UrineKtSGUrineSGF = QLineEdit()
        self.UrineKtSGUrineSGF.setMaxLength(7)
        self.UrineKtSGUrineSGF.setValidator(QDoubleValidator())
        
        self.UrineKtSGEnteredL = QLabel("Entered")
        self.UrineKtSGEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.UrineKtSGEnteredF = QLineEdit()
        self.UrineKtSGEnteredF.setPlaceholderText("Required")

        self.UrineKtSGCommentsL = QLabel("Comments")
        self.UrineKtSGCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.UrineKtSGCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.UrineKtSGCommentsF = QTextEdit()

        self.UrineKtSGSaveButton = QPushButton("Save")

        ################### Update Data - Vitals ###################

        self.VitalsMRNumberL = QLabel("Medical Record Number")
        self.VitalsMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.VitalsMRNumberF = QLineEdit()
        self.VitalsMRNumberF.setMaxLength(10)
        self.VitalsMRNumberF.setPlaceholderText("Required")
        self.VitalsMRNumberF.setValidator(QIntValidator())
        
        self.VitalsDateL = QLabel("Date - (MM/DD/YYYY)")
        self.VitalsDateL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsDateL.setToolTip("Date indicated on records")
        self.VitalsDateF = QDateEdit()
        self.VitalsDateF.setDisplayFormat("MM/dd/yyyy")
        self.VitalsDateF.setDate(datetime.date(datetime.now()))
        
        self.VitalsDayTypeL = QLabel("Day Type")
        self.VitalsDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsDayTypeL.setToolTip("Description of date of collection")
        self.VitalsDayTypeF = QComboBox()
        self.VitalsDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])
        
        self.VitalsSourceL = QLabel("Source")
        self.VitalsSourceL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsSourceL.setToolTip("Description of location for data collection which indicates quality of data. Patients on the prospective study can have 1,2, or 3 as options. \nPatients before the prospective study only have 2 and 3 as options")
        self.VitalsSourceF = QComboBox()
        self.VitalsSourceF.addItems(['1 = CRC', '2 = Clinic', '3 = Other (e.g. home,school)'])

        self.VitalsBPSysL = QLabel("Blood Pressure Systolic - (mmHg)")
        self.VitalsBPSysL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsBPSysL.setToolTip("Systolic blood pressure is the pressure when the heart beats while pumping blood")
        self.VitalsBPSysF = QLineEdit()
        self.VitalsBPSysF.setMaxLength(3)
        self.VitalsBPSysF.setValidator(QIntValidator())

        self.VitalsBPDiaL = QLabel("Blood Pressure Diastolic - (mmHg)")
        self.VitalsBPDiaL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsBPDiaL.setToolTip("Diastolic blood pressure is the pressure when the heart is at rest between beats")
        self.VitalsBPDiaF = QLineEdit()
        self.VitalsBPDiaF.setMaxLength(2)
        self.VitalsBPDiaF.setValidator(QIntValidator())

        self.VitalsTempL = QLabel("Temperature - (Celsius)")
        self.VitalsTempL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsTempL.setToolTip("The degree of heat maintained by the body or it is the balance between heat produced in the tissues and heat lost to the environment. It is typically taken axillary for our patients")
        self.VitalsTempF = QLineEdit()
        self.VitalsTempF.setMaxLength(3)
        self.VitalsTempF.setValidator(QDoubleValidator())
        
        self.VitalsRRL = QLabel("Respiratory Rate - (Respirations/minute)")
        self.VitalsRRL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsRRL.setToolTip("The respiration rate is the number of breaths a person takes per minute. The rate is usually measured when a person is at rest and simply involves \ncounting the number of breaths for one minute by counting how many times the chest rises")
        self.VitalsRRF = QLineEdit()
        self.VitalsRRF.setMaxLength(2)
        self.VitalsRRF.setValidator(QIntValidator())

        self.VitalsHRL = QLabel("Heart Rate - (Beats/minute)")
        self.VitalsHRL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsHRL.setToolTip("The number of time the heart beats per minute")
        self.VitalsHRF = QLineEdit()
        self.VitalsHRF.setMaxLength(3)
        self.VitalsHRF.setValidator(QIntValidator())

        self.VitalsEnteredL = QLabel("Entered")
        self.VitalsEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.VitalsEnteredF = QLineEdit()
        self.VitalsEnteredF.setPlaceholderText("Required")

        self.VitalsCommentsL = QLabel("Comments")
        self.VitalsCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.VitalsCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.VitalsCommentsF = QTextEdit()

        self.VitalsSaveButton = QPushButton("Save")

        ################### Update Data - VNS ###################

        self.VNSMRNumberL = QLabel("Medical Record Number")
        self.VNSMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.VNSMRNumberF = QLineEdit()
        self.VNSMRNumberF.setMaxLength(10)
        self.VNSMRNumberF.setPlaceholderText("Required")
        self.VNSMRNumberF.setValidator(QIntValidator())
        
        self.VNSDateL = QLabel("Date - (MM/DD/YYYY)")
        self.VNSDateL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSDateL.setToolTip("Date indicated on records")
        self.VNSDateF = QDateEdit()
        self.VNSDateF.setDisplayFormat("MM/dd/yyyy")
        self.VNSDateF.setDate(datetime.date(datetime.now()))
        
        self.VNSDayTypeL = QLabel("Day Type")
        self.VNSDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSDayTypeL.setToolTip("Description of date of collection")
        self.VNSDayTypeF = QComboBox()
        self.VNSDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])
        
        self.VNSMRMagActL = QLabel("Number Of Magnet Activations")
        self.VNSMRMagActL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSMRMagActL.setToolTip("Number Magnet Activations For Vagul Nerve Stimulator")
        self.VNSMRMagActF = QLineEdit()
        self.VNSMRMagActF.setMaxLength(5)
        self.VNSMRMagActF.setValidator(QIntValidator())

        self.VNSOutputCurrL = QLabel("Output Current - (2 Decimals)")
        self.VNSOutputCurrL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSOutputCurrL.setToolTip("Output Current For Vagul Nerve Stimulator")
        self.VNSOutputCurrF = QLineEdit()
        self.VNSOutputCurrF.setMaxLength(6)
        self.VNSOutputCurrF.setValidator(QDoubleValidator())

        self.VNSVNSFrequencyL = QLabel("Frequency - (2 Decimals)")
        self.VNSVNSFrequencyL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSVNSFrequencyL.setToolTip("Frequency For Vagul Nerve Stimulator")
        self.VNSVNSFrequencyF = QLineEdit()
        self.VNSVNSFrequencyF.setMaxLength(6)
        self.VNSVNSFrequencyF.setValidator(QDoubleValidator())
        
        self.VNSPulseWidthL = QLabel("Pulse Width - (2 Decimals)")
        self.VNSPulseWidthL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSPulseWidthL.setToolTip("Pulse Width For Vagul Nerve Stimulator")
        self.VNSPulseWidthF = QLineEdit()
        self.VNSPulseWidthF.setMaxLength(6)
        self.VNSPulseWidthF.setValidator(QDoubleValidator())
        
        self.VNSSignalOnL = QLabel("Signal On Time - (2 Decimals)")
        self.VNSSignalOnL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSSignalOnL.setToolTip("Signal On Time For Vagul Nerve Stimulator")
        self.VNSSignalOnF = QLineEdit()
        self.VNSSignalOnF.setMaxLength(5)
        self.VNSSignalOnF.setValidator(QDoubleValidator())

        self.VNSSignalOffL = QLabel("Signal Off Time - (2 Decimals)")
        self.VNSSignalOffL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSSignalOffL.setToolTip("Signal Off Time For Vagul Nerve Stimulator")
        self.VNSSignalOffF = QLineEdit()
        self.VNSSignalOffF.setMaxLength(5)
        self.VNSSignalOffF.setValidator(QDoubleValidator())

        self.VNSMagnetCurrentL = QLabel("Magnet Current - (2 Decimals)")
        self.VNSMagnetCurrentL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSMagnetCurrentL.setToolTip("Magnet Current For Vagul Nerve Stimulator")
        self.VNSMagnetCurrentF = QLineEdit()
        self.VNSMagnetCurrentF.setMaxLength(5)
        self.VNSMagnetCurrentF.setValidator(QDoubleValidator())

        self.VNSMagnetOnL = QLabel("Magnet On Time - (2 Decimals)")
        self.VNSMagnetOnL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSMagnetOnL.setToolTip("Magnet On Time For Vagul Nerve Stimulator")
        self.VNSMagnetOnF = QLineEdit()
        self.VNSMagnetOnF.setMaxLength(5)
        self.VNSMagnetOnF.setValidator(QDoubleValidator())

        self.VNSMagnetPulseL = QLabel("Magnet Pulse Width - (2 Decimals)")
        self.VNSMagnetPulseL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSMagnetPulseL.setToolTip("Magnet Pulse Width For Vagul Nerve Stimulator")
        self.VNSMagnetPulseF = QLineEdit()
        self.VNSMagnetPulseF.setMaxLength(5)
        self.VNSMagnetPulseF.setValidator(QDoubleValidator())

        self.VNSLeadTestL = QLabel("Lead Test")
        self.VNSLeadTestL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSLeadTestL.setToolTip("Lead test from the VNS source")
        self.VNSLeadTestF = QLineEdit()
        self.VNSLeadTestF.setMaxLength(30)
        
        self.VNSEnteredL = QLabel("Entered")
        self.VNSEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.VNSEnteredF = QLineEdit()
        self.VNSEnteredF.setPlaceholderText("Required")

        self.VNSCommentsL = QLabel("Comments")
        self.VNSCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.VNSCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.VNSCommentsF = QTextEdit()

        self.VNSSaveButton = QPushButton("Save")

        ################### Update Data - Clinical Labs ###################

        self.ClinicalLabsMRNumberL = QLabel("Medical Record Number")
        self.ClinicalLabsMRNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMRNumberL.setToolTip("Medical record number from UF Health that is unique to each patient")
        self.ClinicalLabsMRNumberF = QLineEdit()
        self.ClinicalLabsMRNumberF.setMaxLength(10)
        self.ClinicalLabsMRNumberF.setPlaceholderText("Required")
        self.ClinicalLabsMRNumberF.setValidator(QIntValidator())
        
        self.ClinicalLabsDateL = QLabel("Date - (MM/DD/YYYY)")
        self.ClinicalLabsDateL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsDateL.setToolTip("Date indicated on records")
        self.ClinicalLabsDateF = QDateEdit()
        self.ClinicalLabsDateF.setDisplayFormat("MM/dd/yyyy")
        self.ClinicalLabsDateF.setDate(datetime.date(datetime.now()))

        self.ClinicalLabsTimeL = QLabel("Time - (hh:mm:ss)")
        self.ClinicalLabsTimeL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsTimeL.setToolTip("Time blood sample was collected")
        self.ClinicalLabsTimeF = QLineEdit()
        self.ClinicalLabsTimeF.setMaxLength(8)
        
        self.ClinicalLabsDayTypeL = QLabel("Day Type")
        self.ClinicalLabsDayTypeL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsDayTypeL.setToolTip("Description of date of collection")
        self.ClinicalLabsDayTypeF = QComboBox()
        self.ClinicalLabsDayTypeF.addItems(['1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])
        
        self.ClinicalLabsSourceL = QLabel("Source")
        self.ClinicalLabsSourceL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsSourceL.setToolTip("Description of location for data collection which indicates quality of data")
        self.ClinicalLabsSourceF = QComboBox()
        self.ClinicalLabsSourceF.addItems(['1 = CRC', '2 = Clinic', '3 = Other (e.g. home,school)'])

        self.ClinicalLabsFastingL = QLabel("Fasting Status")
        self.ClinicalLabsFastingL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsFastingL.setToolTip("Determination of whether or not the patient was fasting at time of blood draw. Patients are asked to fast for at least 8 hours prior to a blood draw.\n Fasting is defined as no Calorie intake, but medications and water are encouraged.")
        self.ClinicalLabsFastingF = QComboBox()
        self.ClinicalLabsFastingF.addItems(['1 = Fasting','2 = Non-Fasting'])

        self.ClinicalLabsTGBloodL = QLabel("Triglyceride Blood - (mg/dL)")
        self.ClinicalLabsTGBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsTGBloodL.setToolTip("A triglyceride (TG, triacylglycerol, TAG, or triacylglyceride) is an ester derived from glycerol and three fatty acids. \nThere are many triglycerides, depending on the oil source, some are highly unsaturated, some less so. \nTriglycerides are the main constituents of vegetable oil (typically more unsaturated) and animal fats (typically more saturated). \nIn humans, triglycerides are a mechanism for storing unused calories, and their high concentrations in blood correlates with the consumption of starchy and fatty foods. \nHigh levels of triglycerides in the bloodstream have been linked to atherosclerosis and, by extension, the risk of heart disease and stroke. \nDiets high in carbohydrates, with carbohydrates accounting for more than 60% of the total energy intake, can increase triglyceride levels.")
        self.ClinicalLabsTGBloodF = QLineEdit()
        self.ClinicalLabsTGBloodF.setMaxLength(4)
        self.ClinicalLabsTGBloodF.setValidator(QIntValidator())

        self.ClinicalLabsHDLBloodL = QLabel("High Density Lipoprotein Blood - (mg/dL)")
        self.ClinicalLabsHDLBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsHDLBloodL.setToolTip("High-density lipoprotein (HDL) is one of the five major groups of lipoproteins (chylomicrons, VLDL, IDL, LDL, HDL) which enable lipids like cholesterol and triglycerides to be transported within the water based blood stream. \nIn healthy individuals, about thirty percent of blood cholesterol is carried by HDL. High levels of cholesterol in the blood have been linked to damage to arteries and cardiovascular disease.")
        self.ClinicalLabsHDLBloodF = QLineEdit()
        self.ClinicalLabsHDLBloodF.setMaxLength(3)
        self.ClinicalLabsHDLBloodF.setValidator(QIntValidator())
        
        self.ClinicalLabsLDLBloodL = QLabel("Low Density Lipoprotein Blood - (mg/dL)")
        self.ClinicalLabsLDLBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLDLBloodL.setToolTip("A small dense LDL fraction, reported as part of LDL Subclasses panel. Seven LDL subclasses and 3 mid-band fractions can be determined by linear polyacrylamide gel electrophoresis and densitometric scanning. \nFormula= Total cholesterol - HDL - (Triglyceride/5)")
        self.ClinicalLabsLDLBloodF = QLineEdit()
        self.ClinicalLabsLDLBloodF.setMaxLength(3)
        self.ClinicalLabsLDLBloodF.setValidator(QIntValidator())
        
        self.ClinicalLabsTCBloodL = QLabel("Total Cholesterol Blood - (mg/dL)")
        self.ClinicalLabsTCBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsTCBloodL.setToolTip("Cholesterol is a lipidic, waxy alcohol found in the cell membranes and transported in the blood plasma of all animals. \nIt is an essential component of mammalian cell membranes where it establishes proper membrane permeability and fluidity. \nCholesterol is the principal sterol synthesized by animals, but small quantities are synthesized in other eukaryotes, such as plants and fungi. \nIt is almost completely absent among prokaryotes, which include bacteria. Cholesterol is classified as a sterol.")
        self.ClinicalLabsTCBloodF = QLineEdit()
        self.ClinicalLabsTCBloodF.setMaxLength(4)
        self.ClinicalLabsTCBloodF.setValidator(QIntValidator())

        self.ClinicalLabsNABloodL = QLabel("Sodium Blood - (mmol/L)")
        self.ClinicalLabsNABloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsNABloodL.setToolTip("Sodium is an essential nutrient that regulates blood volume, blood pressure, osmotic equilibrium and electrolyte balance. \nSodium chloride is the principal source of sodium in the diet, and is used for seasoning and as a preservative. \nIncreased levels of sodium intake can cause hypertension and reportedly leads to 7.6 million premature deaths worldwide. \nSodium is also important in neuron function and osmoregulation between cells and the extracellular fluid.")
        self.ClinicalLabsNABloodF = QLineEdit()
        self.ClinicalLabsNABloodF.setMaxLength(3)
        self.ClinicalLabsNABloodF.setValidator(QIntValidator())

        self.ClinicalLabsKBloodL = QLabel("Potassium Blood - (mmol/L, 1 Decimal)")
        self.ClinicalLabsKBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsKBloodL.setToolTip("Potassium (symbol K from Latin:kalium) is a key chemical element involved in neuron function and influencing osmotic balance between cells and interstitial fluid. \nDepletion in potassium levels results in deficient fluid and electrolyte balance in the body as well as various nervous and cardiac dysfunctions. \nStudies suggest diets high in potassium can reduce the risk of hypertension and possibly stroke. \nFoods rich in potassium include parsley, dried apricots, potatoes, bananas, avocados, soybeans, and bran, as well as most fruits, vegetables, meat and fish. \nOverall, clear cases of potassium deficiency are rare in healthy individuals.")
        self.ClinicalLabsKBloodF = QLineEdit()
        self.ClinicalLabsKBloodF.setMaxLength(4)
        self.ClinicalLabsKBloodF.setValidator(QDoubleValidator())
        
        self.ClinicalLabsChlBloodL = QLabel("Chloride Blood - (mmol/L)")
        self.ClinicalLabsChlBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsChlBloodL.setToolTip("The chloride ion is formed when the element chlorine picks up one electron to form an anion negatively-charged ion Cl−. The salts of hydrochloric acid contain chloride ions and can also be called chlorides.")
        self.ClinicalLabsChlBloodF = QLineEdit()
        self.ClinicalLabsChlBloodF.setMaxLength(3)
        self.ClinicalLabsChlBloodF.setValidator(QIntValidator())

        self.ClinicalLabsCO2BloodL = QLabel("Carbon Dioxide Blood - (mmol/L)")
        self.ClinicalLabsCO2BloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsCO2BloodL.setToolTip("Carbon dioxide content is a measurement of total CO2 in the blood. Most of it is in the form of bicarbonate (HCO3) controlled by the kidney. \nA small amount (5%) of CO2 is dissolved in the blood as insoluble carbonic acid (H2CO3). Changes in CO2 content generally relate to metabolic issues, renal function and unusual losses (diarrhea). \nRespiratory disease can ultimately effect CO2 content, but only slightly and only if prolonged. ")
        self.ClinicalLabsCO2BloodF = QLineEdit()
        self.ClinicalLabsCO2BloodF.setMaxLength(2)
        self.ClinicalLabsCO2BloodF.setValidator(QIntValidator())

        self.ClinicalLabsBUNBloodL = QLabel("Blood Urea Nitrogen Blood - (mg/dL)")
        self.ClinicalLabsBUNBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsBUNBloodL.setToolTip("Urea, also called carbamide, is an organic chemical compound involved in the metabolism of nitrogen-containing compounds and in the re-absorption of water and critical ions from excreted urine, \nan important mechanism in prevention of water loss and maintaining blood pressure. Urea levels are measured to diagnose conditions that affect the kidneys, \nsuch as acute kidney failure or end-stage renal disease (ESRD). The blood urea nitrogen (BUN) test may be used to determine how well a patient's kidneys are functioning. \nIncreased or decreased levels of urea may also suggest dehydration or increased protein intake.")
        self.ClinicalLabsBUNBloodF = QLineEdit()
        self.ClinicalLabsBUNBloodF.setMaxLength(2)
        self.ClinicalLabsBUNBloodF.setValidator(QIntValidator())

        self.ClinicalLabsCrBloodL = QLabel("Creatinine Blood - (mg/dL, 2 Decimals)")
        self.ClinicalLabsCrBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsCrBloodL.setToolTip("Creatinine or creatine anhydride, is a breakdown product of creatine phosphate in muscle. The loss of water molecule from creatine results in the \nformation of creatinine. It is transferred to the kidneys by blood plasma, whereupon it is eliminated by glomular filtration and partial tubular excretion. \nCreatinine is usually produced at a fairly constant rate and measuring its serum level is a simple test. A rise in blood creatinine levels is observed only with marked damage \nto functioning nephrons; therefore this test is not suitable for detecting early kidney disease. Creatine and creatinine are metabolized in the kidneys, muscle, liver and pancreas.")
        self.ClinicalLabsCrBloodF = QLineEdit()
        self.ClinicalLabsCrBloodF.setMaxLength(3)
        self.ClinicalLabsCrBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsGlusBloodL = QLabel("Glucose Blood - (mg/dL, 2 Decimals)")
        self.ClinicalLabsGlusBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsGlusBloodL.setToolTip("Glucose (Glc), a monosaccharide (or simple sugar) also known as grape sugar, blood sugar, or corn sugar, is an important carbohydrate. \nLiving cell uses it as a source of energy and a metabolic intermediate. Glucose is a common medical analyte measured in blood samples. Eating or fasting prior to taking a blood sample has an effect on the result. \nHigher than usual glucose levels may be a sign of prediabetes or diabetes mellitus.")
        self.ClinicalLabsGlusBloodF = QLineEdit()
        self.ClinicalLabsGlusBloodF.setMaxLength(6)
        self.ClinicalLabsGlusBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsCaBloodL = QLabel("Calcium Blood - (mg/dL, 1 Decimal)")
        self.ClinicalLabsCaBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsCaBloodL.setToolTip("Calcium is essential for living organisms, in particular in cell physiology, where movement of the calcium ion Ca2+ into and out of the \ncytoplasm functions as a signal for many cellular processes. It is an important component of a healthy diet and a mineral necessary for life. Dairy products, such as milk and cheese, are a well-known source of calcium \nas well as nuts and seeds, beans, figs, broccoli, kale and fortified products such as orange juice and soy milk. \nApproximately 99 percent of the body's calcium is stored in the bones and teeth. Long-term calcium deficiency can lead to rickets and poor blood clotting. \nIn menopausal woman, it can lead to osteoporosis. While a lifelong deficit can affect bone and tooth formation, over-retention can cause hypercalcemia (elevated levels of calcium in the blood), \nimpaired kidney function and decreased absorption of other minerals. In addition, studies suggest a correlation between high calcium intake (2000 mg per day) and prostate cancer.")
        self.ClinicalLabsCaBloodF = QLineEdit()
        self.ClinicalLabsCaBloodF.setMaxLength(4)
        self.ClinicalLabsCaBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsMagBloodL = QLabel("Magnesium Blood - (mg/dL, 1 Decimal)")
        self.ClinicalLabsMagBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMagBloodL.setToolTip("Magnesium salts are essential in nutrition, being required for the activity of many enzymes, especially those concerned with oxidative phosphorylation. \nPhysiologically, it exists as an ion in the body. It is a component of both intra- and extracellular fluids and is excreted in the urine and feces. Deficiency causes irritability of the nervous system \nwith tetany, vasodilatation, convulsions, tremors, depression, and psychotic behavior. Magnesium ion in large amounts is an ionic laxative, and magnesium sulfate \n(Epsom salts) is sometimes used for this purpose. So-called \"milk of magnesia\" is a water suspension of one of the few insoluble magnesium compounds, magnesium hydroxide; the \nundissolved particles give rise to its appearance and name. Milk of magnesia is a mild base, and is commonly used as an antacid.")
        self.ClinicalLabsMagBloodF = QLineEdit()
        self.ClinicalLabsMagBloodF.setMaxLength(4)
        self.ClinicalLabsMagBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsPhosBloodL = QLabel("Phosphorus Blood - (mg/dL, 1 Decimal)")
        self.ClinicalLabsPhosBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsPhosBloodL.setToolTip("Phosphate levels are checked to see if a patient has a kidney or bone-related disease or to identify problems with certain glands, such as the parathyroid glands. \nPhosphate is a salt of phosphoric acid. In organic chemistry, a phosphate, or organophosphate, is an ester of phosphoric acid. The body needs phosphate to build and repair bones and teeth and \nto help the nervous system function. A high level of phosphate in the blood is usually caused by a kidney problem since they help control the amount of phosphate \nin the blood. Phosphate levels also affects the level of calcium in the blood, so both calcium and phosphate levels are usually measured at the same time.")
        self.ClinicalLabsPhosBloodF = QLineEdit()
        self.ClinicalLabsPhosBloodF.setMaxLength(4)
        self.ClinicalLabsPhosBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsUricAcidBloodL = QLabel("Uric Acid Blood - (mg/dL, 1 Decimal)")
        self.ClinicalLabsUricAcidBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsUricAcidBloodL.setToolTip("Uric acid (urate) is a product of the metabolic breakdown of purine nucleotides.")
        self.ClinicalLabsUricAcidBloodF = QLineEdit()
        self.ClinicalLabsUricAcidBloodF.setMaxLength(4)
        self.ClinicalLabsUricAcidBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsProBloodL = QLabel("Protein Blood - (G/dL, 1 Decimal)")
        self.ClinicalLabsProBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsProBloodL.setToolTip("Protein testing is performed to evaluate and monitor liver and kidney function and to detect and diagnose early kidney damage and various other diseases. \nElevated protein levels may also be due to an infection, medication, vigorous exercise, or emotional or physical stress. Body fluids contain many different proteins that serve diverse functions such as transport of nutrients, removal of toxins, control of metabolic processes, and defense against invaders. \nTesting for protein levels may be done as part of a routine physical, a pregnancy workup, in cased of a suspected UTI, as part of a hospital admission, or to evaluate kidney function.")
        self.ClinicalLabsProBloodF = QLineEdit()
        self.ClinicalLabsProBloodF.setMaxLength(4)
        self.ClinicalLabsProBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsAlbBloodL = QLabel("Albumin Blood - (G/dL, 1 Decimal)")
        self.ClinicalLabsAlbBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsAlbBloodL.setToolTip("Albumin is a non-glycosylated protein that is synthesized in the liver parenchymal cells, regulated by colloid osmotic pressure from interstitial fluid \nsurrounding hepatocytes, and catabolized in nearly all organs.")
        self.ClinicalLabsAlbBloodF = QLineEdit()
        self.ClinicalLabsAlbBloodF.setMaxLength(4)
        self.ClinicalLabsAlbBloodF.setValidator(QDoubleValidator())
        
        self.ClinicalLabsTBilBloodL = QLabel("Total Bilirubin Blood - (mg/dL, 1 Decimal)")
        self.ClinicalLabsTBilBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsTBilBloodL.setToolTip("Bilirubin is an orange-yellow pigment produced by the normal breakdown of heme, a component of the hemoglobin found in red blood cells. ")
        self.ClinicalLabsTBilBloodF = QLineEdit()
        self.ClinicalLabsTBilBloodF.setMaxLength(4)
        self.ClinicalLabsTBilBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsTotalBilirubinBloodL = QLabel("Alkaline Phosphatase Blood - (U/L)")
        self.ClinicalLabsTotalBilirubinBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsTotalBilirubinBloodL.setToolTip("Alkaline phosphatase (ALP, ALKP) is a hydrolase enzyme responsible for removing phosphate groups from many types of molecules, including nucleotides, proteins, and alkaloids.")
        self.ClinicalLabsTotalBilirubinBloodF = QLineEdit()
        self.ClinicalLabsTotalBilirubinBloodF.setMaxLength(3)
        self.ClinicalLabsTotalBilirubinBloodF.setValidator(QIntValidator())

        self.ClinicalLabsAstBloodL = QLabel("Aspartate Amino Transferase Blood - (U/L)")
        self.ClinicalLabsAstBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsAstBloodL.setToolTip("Aspartate transaminase (AST) also called serum glutamic oxaloacetic transaminase (SGOT) or aspartate aminotransferase (ASAT/AAT/AspAT) (EC 2.6.1.1) \nis similar to alanine transaminase (ALT) in that it is another enzyme associated with liver parenchymal cells. ")
        self.ClinicalLabsAstBloodF = QLineEdit()
        self.ClinicalLabsAstBloodF.setMaxLength(3)
        self.ClinicalLabsAstBloodF.setValidator(QIntValidator())

        self.ClinicalLabsAltBloodL = QLabel("Alanine Amino Transferase Blood - (U/L)")
        self.ClinicalLabsAltBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsAltBloodL.setToolTip("Alanine transaminase or ALT is an enzyme (EC 2.6.1.2) also called serum glutamic pyruvic transaminase (SGPT) or alanine aminotransferase (ALAT). \nIt is found in serum and in various bodily tissues, but is most commonly associated with the liver.")
        self.ClinicalLabsAltBloodF = QLineEdit()
        self.ClinicalLabsAltBloodF.setMaxLength(3)
        self.ClinicalLabsAltBloodF.setValidator(QIntValidator())

        self.ClinicalLabsRBCBloodL = QLabel("Red Blood Cell Blood - (10^12/L, 2 Decimals)")
        self.ClinicalLabsRBCBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsRBCBloodL.setToolTip("Red blood cells (RBC), or erythrocytes, are the most common type of blood cells whose function is to transport oxygen throughout the body.")
        self.ClinicalLabsRBCBloodF = QLineEdit()
        self.ClinicalLabsRBCBloodF.setMaxLength(4)
        self.ClinicalLabsRBCBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsHgbBloodL = QLabel("Hemoglobin Blood - (g/dL, 2 Decimals)")
        self.ClinicalLabsHgbBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsHgbBloodL.setToolTip("Hemoglobin (Hb or Hgb) is the iron-containing oxygen-transport metalloprotein in the red blood cells.")
        self.ClinicalLabsHgbBloodF = QLineEdit()
        self.ClinicalLabsHgbBloodF.setMaxLength(4)
        self.ClinicalLabsHgbBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsHctBloodL = QLabel("Hematocrit Blood - (%, 2 Decimals)")
        self.ClinicalLabsHctBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsHctBloodL.setToolTip("The volume of packed red blood cells in a blood sample. The volume is measured by centrifugation in a tube with graduated markings, or with automated blood cell counters. \nIt is an indicator of erythrocyte status in disease. For example, in anemia the volume is low and in polycythemia it is high.")
        self.ClinicalLabsHctBloodF = QLineEdit()
        self.ClinicalLabsHctBloodF.setMaxLength(4)
        self.ClinicalLabsHctBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsPlateletBloodL = QLabel("Platelet Blood - (10^3/μL)")
        self.ClinicalLabsPlateletBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsPlateletBloodL.setToolTip("A platelet count is a lab test to measure how many platelets you have in your blood. Platelets are parts of the blood that help the blood clot. \nThey are smaller than red or white blood cells. The number of platelets in your blood can be affected by many diseases. Platelets may be counted to monitor or diagnose diseases, or to look for the cause of too much bleeding or clotting.")
        self.ClinicalLabsPlateletBloodF = QLineEdit()
        self.ClinicalLabsPlateletBloodF.setMaxLength(3)
        self.ClinicalLabsPlateletBloodF.setValidator(QIntValidator())

        self.ClinicalLabsMCVBloodL = QLabel("Mean Corpuscular Volume Blood - (fL, 1 Decimal)")
        self.ClinicalLabsMCVBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMCVBloodL.setToolTip("The mean corpuscular volume, or MCV, is a measure of the average red blood cell volume. \nMCV measurements classify anemias as either microcytic (MCV below normal range) or macrocytic (MCV above normal range).")
        self.ClinicalLabsMCVBloodF = QLineEdit()
        self.ClinicalLabsMCVBloodF.setMaxLength(4)
        self.ClinicalLabsMCVBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsMCHBloodL = QLabel("Mean Corpuscular Hemoglobin Blood - (pg, 1 Decimal)")
        self.ClinicalLabsMCHBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMCHBloodL.setToolTip("The mean corpuscular hemoglobin, or \"mean cell hemoglobin\" (MCH), is the average mass of hemoglobin per red blood cell in a blood sample. \nIt is decreased in hypochromic anemias, and increased in hyperchromic anemias. MCH is obtained by dividing the total mass of hemoglobin by the number of red blood cells in a volume of blood.")
        self.ClinicalLabsMCHBloodF = QLineEdit()
        self.ClinicalLabsMCHBloodF.setMaxLength(4)
        self.ClinicalLabsMCHBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsMCHCBloodL = QLabel("Mean Corpuscular Hemoglobin Concentration Blood - (g/dL, 1 Decimal)")
        self.ClinicalLabsMCHCBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMCHCBloodL.setToolTip("The mean corpuscular hemoglobin concentration, or MCHC, is a measure of the concentration of hemoglobin in a given volume of packed red blood cell. \nIt is reported as part of a standard complete blood count. It is calculated by dividing the hemoglobin by the hematocrit.")
        self.ClinicalLabsMCHCBloodF = QLineEdit()
        self.ClinicalLabsMCHCBloodF.setMaxLength(4)
        self.ClinicalLabsMCHCBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsMPVBloodL = QLabel("Mean Platelet Volume Blood - (fL, 1 Decimal)")
        self.ClinicalLabsMPVBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMPVBloodL.setToolTip("Platelet size can be measured directly by automated hematology analyzers, expressed as mean platelet volume (MPV). \nPlatelet size is determined at the time of platelet production from megakaryocytes.")
        self.ClinicalLabsMPVBloodF = QLineEdit()
        self.ClinicalLabsMPVBloodF.setMaxLength(4)
        self.ClinicalLabsMPVBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsRDWBloodL = QLabel("Red Blood Cell Distribution Blood - (%, 1 Decimal)")
        self.ClinicalLabsRDWBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsRDWBloodL.setToolTip("The RDW-CV is the ratio of the variation in width to the mean width ot the RBC volume distribution curve taken at +/- 1CV. \nRed Cell Distribution Width (RDW) is a measurement of anisocytosis.")
        self.ClinicalLabsRDWBloodF = QLineEdit()
        self.ClinicalLabsRDWBloodF.setMaxLength(4)
        self.ClinicalLabsRDWBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsWBCBloodL = QLabel("White Blood Cell Blood - (10^3/μL, 1 Decimal)")
        self.ClinicalLabsWBCBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsWBCBloodL.setToolTip("White blood cells are intrinsic components of the blood. They are produced in the bone marrow and help to defend against infectious agents and foreign materials. \nAs part of the immune system, they also help fight against malignant and aberrant cells.")
        self.ClinicalLabsWBCBloodF = QLineEdit()
        self.ClinicalLabsWBCBloodF.setMaxLength(4)
        self.ClinicalLabsWBCBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsAmmoniaBloodL = QLabel("White Blood Cell Blood - (2 Decimals)")
        self.ClinicalLabsAmmoniaBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsAmmoniaBloodL.setToolTip("Ammonia is a colorless alkaline gas with a characteristic sharp smell.")
        self.ClinicalLabsAmmoniaBloodF = QLineEdit()
        self.ClinicalLabsAmmoniaBloodF.setMaxLength(4)
        self.ClinicalLabsAmmoniaBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsBHbBloodL = QLabel("Beta Hydroxybutyrate Blood Mmol L - (mmol/L, 1 Decimal)")
        self.ClinicalLabsBHbBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsBHbBloodL.setToolTip("Beta-hydroxybutyrate from blood mmol/L obtained at fasting state. Increases in beta-hydroxybutyrate are due to excessive fatty acid oxidation.")
        self.ClinicalLabsBHbBloodF = QLineEdit()
        self.ClinicalLabsBHbBloodF.setMaxLength(4)
        self.ClinicalLabsBHbBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsAcacBloodL = QLabel("Acetoacetate Blood - (mg/dL, 2 Decimals)")
        self.ClinicalLabsAcacBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsAcacBloodL.setToolTip("Acetoacetic acid (also known as 3-oxobutanoic acid or diacetic acid) is a beta-keto acid of the keto acid group. \nIt is a weak organic acid produced in the liver under conditions of poor metabolism leading to excessive fatty acid breakdown.")
        self.ClinicalLabsAcacBloodF = QLineEdit()
        self.ClinicalLabsAcacBloodF.setMaxLength(4)
        self.ClinicalLabsAcacBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsNeutrophilsBloodL = QLabel("Neutrophils Blood - (%, 2 Decimals)")
        self.ClinicalLabsNeutrophilsBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsNeutrophilsBloodL.setToolTip("Neutrophils/​100 leukocytes in blood by automated count.  Neutrophil granulocytes, generally referred to as neutrophils, are the most abundant type of white blood cells. ")
        self.ClinicalLabsNeutrophilsBloodF = QLineEdit()
        self.ClinicalLabsNeutrophilsBloodF.setMaxLength(4)
        self.ClinicalLabsNeutrophilsBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsLymphocytesBloodL = QLabel("Lymphocytes Blood - (%, 2 Decimals)")
        self.ClinicalLabsLymphocytesBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLymphocytesBloodL.setToolTip("Lymphocytes/​100 leukocytes in blood by automated count. A lymphocyte is a type of white blood cell in the vertebrate immune system.")
        self.ClinicalLabsLymphocytesBloodF = QLineEdit()
        self.ClinicalLabsLymphocytesBloodF.setMaxLength(4)
        self.ClinicalLabsLymphocytesBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsMonocytesBloodL = QLabel("Monocytes Blood - (%, 2 Decimals)")
        self.ClinicalLabsMonocytesBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsMonocytesBloodL.setToolTip("Monocytes/​100 leukocytes in blood by automated count.  A monocyte is a mononuclear leukocyte, intimately involved in the initiaton of an immune response.")
        self.ClinicalLabsMonocytesBloodF = QLineEdit()
        self.ClinicalLabsMonocytesBloodF.setMaxLength(4)
        self.ClinicalLabsMonocytesBloodF.setValidator(QDoubleValidator())
        
        self.ClinicalLabsEosinophilsBloodL = QLabel("Eosinophils Blood - (%, 2 Decimals)")
        self.ClinicalLabsEosinophilsBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsEosinophilsBloodL.setToolTip("Eosinophils/​100 leukocytes in blood by automated count. Granular leukocytes with a nucleus that usually \nhas two lobes connected by a slender thread of chromatin. The cytoplasm contains coarse, round and uniform granules stainable by eosin.")
        self.ClinicalLabsEosinophilsBloodF = QLineEdit()
        self.ClinicalLabsEosinophilsBloodF.setMaxLength(4)
        self.ClinicalLabsEosinophilsBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsBasophilsBloodL = QLabel("Basophils Blood - (%, 2 Decimals)")
        self.ClinicalLabsBasophilsBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsBasophilsBloodL.setToolTip("Basophils/​100 leukocytes in blood by automated count. Basophils are granular white blood cells \ncharacterized by a pale-staining nucleus with 2 to 3 lobes and a cytoplasm containing coarse, dark-staining granules of variable size. ")
        self.ClinicalLabsBasophilsBloodF = QLineEdit()
        self.ClinicalLabsBasophilsBloodF.setMaxLength(4)
        self.ClinicalLabsBasophilsBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsLargeUnstainedCellsBloodL = QLabel("Large Unstained Cells Blood - (%, 2 Decimals)")
        self.ClinicalLabsLargeUnstainedCellsBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLargeUnstainedCellsBloodL.setToolTip("Large unstained cells/​100 leukocytes in blood. Peroxidase negative cells too large to be classified as lymphocytes or basophils.")
        self.ClinicalLabsLargeUnstainedCellsBloodF = QLineEdit()
        self.ClinicalLabsLargeUnstainedCellsBloodF.setMaxLength(4)
        self.ClinicalLabsLargeUnstainedCellsBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsNeutrophilsAbsoluteBloodL = QLabel("Neutrophils Absolute Blood - (10^3/μL, 2 Decimals)")
        self.ClinicalLabsNeutrophilsAbsoluteBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsNeutrophilsAbsoluteBloodL.setToolTip("Neutrophils [#/​volume] in blood by automated count")
        self.ClinicalLabsNeutrophilsAbsoluteBloodF = QLineEdit()
        self.ClinicalLabsNeutrophilsAbsoluteBloodF.setMaxLength(4)
        self.ClinicalLabsNeutrophilsAbsoluteBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsLymphocytesAbsoluteBloodL = QLabel("Lymphocytes Absolute Blood - (10^3/μL, 2 Decimals)")
        self.ClinicalLabsLymphocytesAbsoluteBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLymphocytesAbsoluteBloodL.setToolTip("Lymphocytes [#/​volume] in blood by automated count")
        self.ClinicalLabsLymphocytesAbsoluteBloodF = QLineEdit()
        self.ClinicalLabsLymphocytesAbsoluteBloodF.setMaxLength(4)
        self.ClinicalLabsLymphocytesAbsoluteBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsEosinophilsAbsoluteBloodL = QLabel("Eosinophils Absolute Blood - (10^3/μL, 2 Decimals)")
        self.ClinicalLabsEosinophilsAbsoluteBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsEosinophilsAbsoluteBloodL.setToolTip("Eosinophils [#/​volume] in blood by automated count")
        self.ClinicalLabsEosinophilsAbsoluteBloodF = QLineEdit()
        self.ClinicalLabsEosinophilsAbsoluteBloodF.setMaxLength(4)
        self.ClinicalLabsEosinophilsAbsoluteBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsBasophilsAbsoluteBloodL = QLabel("Basophils Absolute Blood - (10^3/μL, 2 Decimals)")
        self.ClinicalLabsBasophilsAbsoluteBloodL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsBasophilsAbsoluteBloodL.setToolTip("Basophils [#/​volume] in blood by automated count")
        self.ClinicalLabsBasophilsAbsoluteBloodF = QLineEdit()
        self.ClinicalLabsBasophilsAbsoluteBloodF.setMaxLength(4)
        self.ClinicalLabsBasophilsAbsoluteBloodF.setValidator(QDoubleValidator())

        self.ClinicalLabsGlusBloodCRCL = QLabel("Glucose Clinical Research Center Blood - (mg/dL, 2 Decimals)")
        self.ClinicalLabsGlusBloodCRCL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsGlusBloodCRCL.setToolTip("Glucose (Glc), a monosaccharide (or simple sugar) also known as grape sugar, blood sugar, or corn sugar, is an important carbohydrate. \nLiving cell uses it as a source of energy and a metabolic intermediate.")
        self.ClinicalLabsGlusBloodCRCF = QLineEdit()
        self.ClinicalLabsGlusBloodCRCF.setMaxLength(4)
        self.ClinicalLabsGlusBloodCRCF.setValidator(QDoubleValidator())

        self.ClinicalLabsLactBloodCRCMmolL = QLabel("Lactate Clinical Research Center Blood Mmol L - (mmol/L, 2 Decimals)")
        self.ClinicalLabsLactBloodCRCMmolL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLactBloodCRCMmolL.setToolTip("Lactacte from blood mmol/L obtained at fasting state in CRC lab")
        self.ClinicalLabsLactBloodCRCMmolF = QLineEdit()
        self.ClinicalLabsLactBloodCRCMmolF.setMaxLength(4)
        self.ClinicalLabsLactBloodCRCMmolF.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood1L = QLabel("Lab Parameter Blood 1 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood1L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood1L.setToolTip("Phenobarbital levels in the blood. Phenobarbital (INN) or phenobarbitone (former BAN) is a barbiturate, first marketed as Luminal® by Farbwerke Fr. \nBayer and Co. It is the most widely used anticonvulsant worldwide and the oldest still in use.")
        self.ClinicalLabsLabBlood1F = QLineEdit()
        self.ClinicalLabsLabBlood1F.setMaxLength(4)
        self.ClinicalLabsLabBlood1F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood2L = QLabel("Lab Parameter Blood 2 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood2L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood2L.setToolTip("Valproic Acid levels in the blood. Valproic acid is a compound used as an anticonvulsant and mood-stabilizing drug, primarily in the treatment of \nepilepsy and bipolar disorder. It is also used to treat migraine headaches and schizophrenia.")
        self.ClinicalLabsLabBlood2F = QLineEdit()
        self.ClinicalLabsLabBlood2F.setMaxLength(4)
        self.ClinicalLabsLabBlood2F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood3L = QLabel("Lab Parameter Blood 3 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood3L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood3L.setToolTip("Primidone levels in the blood")
        self.ClinicalLabsLabBlood3F = QLineEdit()
        self.ClinicalLabsLabBlood3F.setMaxLength(4)
        self.ClinicalLabsLabBlood3F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood4L = QLabel("Lab Parameter Blood 4 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood4L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood4L.setToolTip("Phenytoin levels in the blood")
        self.ClinicalLabsLabBlood4F = QLineEdit()
        self.ClinicalLabsLabBlood4F.setMaxLength(4)
        self.ClinicalLabsLabBlood4F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood5L = QLabel("Lab Parameter Blood 5 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood5L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood5L.setToolTip("Lamotrigine levels in the blood")
        self.ClinicalLabsLabBlood5F = QLineEdit()
        self.ClinicalLabsLabBlood5F.setMaxLength(4)
        self.ClinicalLabsLabBlood5F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood6L = QLabel("Lab Parameter Blood 6 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood6L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood6L.setToolTip("Clonazepam levels in the blood")
        self.ClinicalLabsLabBlood6F = QLineEdit()
        self.ClinicalLabsLabBlood6F.setMaxLength(4)
        self.ClinicalLabsLabBlood6F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood7L = QLabel("Lab Parameter Blood 7 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood7L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood7L.setToolTip("Oxcarbazepine levels in the blood")
        self.ClinicalLabsLabBlood7F = QLineEdit()
        self.ClinicalLabsLabBlood7F.setMaxLength(4)
        self.ClinicalLabsLabBlood7F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood8L = QLabel("Lab Parameter Blood 8 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood8L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood8L.setToolTip("Carbamazepine levels in the blood")
        self.ClinicalLabsLabBlood8F = QLineEdit()
        self.ClinicalLabsLabBlood8F.setMaxLength(4)
        self.ClinicalLabsLabBlood8F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood9L = QLabel("Lab Parameter Blood 9 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood9L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood9L.setToolTip("Topiramate levels in the blood")
        self.ClinicalLabsLabBlood9F = QLineEdit()
        self.ClinicalLabsLabBlood9F.setMaxLength(4)
        self.ClinicalLabsLabBlood9F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood10L = QLabel("Lab Parameter Blood 10 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood10L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood10L.setToolTip("Vancomycin levels in the blood")
        self.ClinicalLabsLabBlood10F = QLineEdit()
        self.ClinicalLabsLabBlood10F.setMaxLength(4)
        self.ClinicalLabsLabBlood10F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood11L = QLabel("Lab Parameter Blood 11 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood11L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood11L.setToolTip("Gentamicin levels in the blood")
        self.ClinicalLabsLabBlood11F = QLineEdit()
        self.ClinicalLabsLabBlood11F.setMaxLength(4)
        self.ClinicalLabsLabBlood11F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood12L = QLabel("Lab Parameter Blood 12 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood12L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood12L.setToolTip("Gentamicin trough levels in the blood")
        self.ClinicalLabsLabBlood12F = QLineEdit()
        self.ClinicalLabsLabBlood12F.setMaxLength(4)
        self.ClinicalLabsLabBlood12F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood13L = QLabel("Lab Parameter Blood 13 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood13L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood13L.setToolTip("Phenytoin-free levels in the blood")
        self.ClinicalLabsLabBlood13F = QLineEdit()
        self.ClinicalLabsLabBlood13F.setMaxLength(4)
        self.ClinicalLabsLabBlood13F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood14L = QLabel("Lab Parameter Blood 14 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood14L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood14L.setToolTip("Ethosuximide levels in the blood")
        self.ClinicalLabsLabBlood14F = QLineEdit()
        self.ClinicalLabsLabBlood14F.setMaxLength(4)
        self.ClinicalLabsLabBlood14F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood15L = QLabel("Lab Parameter Blood 15 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood15L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood15L.setToolTip("Vancomycin peak levels in the blood")
        self.ClinicalLabsLabBlood15F = QLineEdit()
        self.ClinicalLabsLabBlood15F.setMaxLength(4)
        self.ClinicalLabsLabBlood15F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood16L = QLabel("Lab Parameter Blood 16 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood16L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood16L.setToolTip("Tobramycin peak levels in the blood")
        self.ClinicalLabsLabBlood16F = QLineEdit()
        self.ClinicalLabsLabBlood16F.setMaxLength(4)
        self.ClinicalLabsLabBlood16F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood17L = QLabel("Lab Parameter Blood 17 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood17L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood17L.setToolTip("Tobramycin trough levels in the blood")
        self.ClinicalLabsLabBlood17F = QLineEdit()
        self.ClinicalLabsLabBlood17F.setMaxLength(4)
        self.ClinicalLabsLabBlood17F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood18L = QLabel("Lab Parameter Blood 18 - (mcg/mL, 2 Decimals)")
        self.ClinicalLabsLabBlood18L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood18L.setToolTip("Mephobarbital levels in the blood")
        self.ClinicalLabsLabBlood18F = QLineEdit()
        self.ClinicalLabsLabBlood18F.setMaxLength(4)
        self.ClinicalLabsLabBlood18F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood19L = QLabel("Lab Parameter Blood 19")
        self.ClinicalLabsLabBlood19L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood19L.setToolTip("Blood value for parameter 19")
        self.ClinicalLabsLabBlood19F = QLineEdit()
        self.ClinicalLabsLabBlood19F.setMaxLength(4)
        self.ClinicalLabsLabBlood19F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood20L = QLabel("Lab Parameter Blood 20")
        self.ClinicalLabsLabBlood20L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood20L.setToolTip("Blood value for parameter 20")
        self.ClinicalLabsLabBlood20F = QLineEdit()
        self.ClinicalLabsLabBlood20F.setMaxLength(4)
        self.ClinicalLabsLabBlood20F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood21L = QLabel("Lab Parameter Blood 21")
        self.ClinicalLabsLabBlood21L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood21L.setToolTip("Blood value for parameter 21")
        self.ClinicalLabsLabBlood21F = QLineEdit()
        self.ClinicalLabsLabBlood21F.setMaxLength(4)
        self.ClinicalLabsLabBlood21F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood22L = QLabel("Lab Parameter Blood 22")
        self.ClinicalLabsLabBlood22L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood22L.setToolTip("Blood value for parameter 22")
        self.ClinicalLabsLabBlood22F = QLineEdit()
        self.ClinicalLabsLabBlood22F.setMaxLength(4)
        self.ClinicalLabsLabBlood22F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood23L = QLabel("Lab Parameter Blood 23")
        self.ClinicalLabsLabBlood23L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood23L.setToolTip("Blood value for parameter 23")
        self.ClinicalLabsLabBlood23F = QLineEdit()
        self.ClinicalLabsLabBlood23F.setMaxLength(4)
        self.ClinicalLabsLabBlood23F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood24L = QLabel("Lab Parameter Blood 24")
        self.ClinicalLabsLabBlood24L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood24L.setToolTip("Blood value for parameter 24")
        self.ClinicalLabsLabBlood24F = QLineEdit()
        self.ClinicalLabsLabBlood24F.setMaxLength(4)
        self.ClinicalLabsLabBlood24F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood25L = QLabel("Lab Parameter Blood 25")
        self.ClinicalLabsLabBlood25L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood25L.setToolTip("Blood value for parameter 25")
        self.ClinicalLabsLabBlood25F = QLineEdit()
        self.ClinicalLabsLabBlood25F.setMaxLength(4)
        self.ClinicalLabsLabBlood25F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood26L = QLabel("Lab Parameter Blood 26")
        self.ClinicalLabsLabBlood26L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood26L.setToolTip("Blood value for parameter 26")
        self.ClinicalLabsLabBlood26F = QLineEdit()
        self.ClinicalLabsLabBlood26F.setMaxLength(4)
        self.ClinicalLabsLabBlood26F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood27L = QLabel("Lab Parameter Blood 27")
        self.ClinicalLabsLabBlood27L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood27L.setToolTip("Blood value for parameter 27")
        self.ClinicalLabsLabBlood27F = QLineEdit()
        self.ClinicalLabsLabBlood27F.setMaxLength(4)
        self.ClinicalLabsLabBlood27F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood28L = QLabel("Lab Parameter Blood 28")
        self.ClinicalLabsLabBlood28L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood28L.setToolTip("Blood value for parameter 28")
        self.ClinicalLabsLabBlood28F = QLineEdit()
        self.ClinicalLabsLabBlood28F.setMaxLength(4)
        self.ClinicalLabsLabBlood28F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood29L = QLabel("Lab Parameter Blood 29")
        self.ClinicalLabsLabBlood29L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood29L.setToolTip("Blood value for parameter 29")
        self.ClinicalLabsLabBlood29F = QLineEdit()
        self.ClinicalLabsLabBlood29F.setMaxLength(4)
        self.ClinicalLabsLabBlood29F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood30L = QLabel("Lab Parameter Blood 30")
        self.ClinicalLabsLabBlood30L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood30L.setToolTip("Blood value for parameter 30")
        self.ClinicalLabsLabBlood30F = QLineEdit()
        self.ClinicalLabsLabBlood30F.setMaxLength(4)
        self.ClinicalLabsLabBlood30F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood31L = QLabel("Lab Parameter Blood 31")
        self.ClinicalLabsLabBlood31L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood31L.setToolTip("Blood value for parameter 31")
        self.ClinicalLabsLabBlood31F = QLineEdit()
        self.ClinicalLabsLabBlood31F.setMaxLength(4)
        self.ClinicalLabsLabBlood31F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood32L = QLabel("Lab Parameter Blood 32")
        self.ClinicalLabsLabBlood32L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood32L.setToolTip("Blood value for parameter 32")
        self.ClinicalLabsLabBlood32F = QLineEdit()
        self.ClinicalLabsLabBlood32F.setMaxLength(4)
        self.ClinicalLabsLabBlood32F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood33L = QLabel("Lab Parameter Blood 33")
        self.ClinicalLabsLabBlood33L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood33L.setToolTip("Blood value for parameter 33")
        self.ClinicalLabsLabBlood33F = QLineEdit()
        self.ClinicalLabsLabBlood33F.setMaxLength(4)
        self.ClinicalLabsLabBlood33F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood34L = QLabel("Lab Parameter Blood 34")
        self.ClinicalLabsLabBlood34L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood34L.setToolTip("Blood value for parameter 34")
        self.ClinicalLabsLabBlood34F = QLineEdit()
        self.ClinicalLabsLabBlood34F.setMaxLength(4)
        self.ClinicalLabsLabBlood34F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood35L = QLabel("Lab Parameter Blood 35")
        self.ClinicalLabsLabBlood35L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood35L.setToolTip("Blood value for parameter 35")
        self.ClinicalLabsLabBlood35F = QLineEdit()
        self.ClinicalLabsLabBlood35F.setMaxLength(4)
        self.ClinicalLabsLabBlood35F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood36L = QLabel("Lab Parameter Blood 36")
        self.ClinicalLabsLabBlood36L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood36L.setToolTip("Blood value for parameter 36")
        self.ClinicalLabsLabBlood36F = QLineEdit()
        self.ClinicalLabsLabBlood36F.setMaxLength(4)
        self.ClinicalLabsLabBlood36F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood37L = QLabel("Lab Parameter Blood 37")
        self.ClinicalLabsLabBlood37L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood37L.setToolTip("Blood value for parameter 37")
        self.ClinicalLabsLabBlood37F = QLineEdit()
        self.ClinicalLabsLabBlood37F.setMaxLength(4)
        self.ClinicalLabsLabBlood37F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood38L = QLabel("Lab Parameter Blood 38")
        self.ClinicalLabsLabBlood38L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood38L.setToolTip("Blood value for parameter 38")
        self.ClinicalLabsLabBlood38F = QLineEdit()
        self.ClinicalLabsLabBlood38F.setMaxLength(4)
        self.ClinicalLabsLabBlood38F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood39L = QLabel("Lab Parameter Blood 39")
        self.ClinicalLabsLabBlood39L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood39L.setToolTip("Blood value for parameter 39")
        self.ClinicalLabsLabBlood39F = QLineEdit()
        self.ClinicalLabsLabBlood39F.setMaxLength(4)
        self.ClinicalLabsLabBlood39F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood40L = QLabel("Lab Parameter Blood 40")
        self.ClinicalLabsLabBlood40L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood40L.setToolTip("Blood value for parameter 40")
        self.ClinicalLabsLabBlood40F = QLineEdit()
        self.ClinicalLabsLabBlood40F.setMaxLength(4)
        self.ClinicalLabsLabBlood40F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood41L = QLabel("Lab Parameter Blood 41")
        self.ClinicalLabsLabBlood41L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood41L.setToolTip("Blood value for parameter 41")
        self.ClinicalLabsLabBlood41F = QLineEdit()
        self.ClinicalLabsLabBlood41F.setMaxLength(4)
        self.ClinicalLabsLabBlood41F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood42L = QLabel("Lab Parameter Blood 42")
        self.ClinicalLabsLabBlood42L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood42L.setToolTip("Blood value for parameter 42")
        self.ClinicalLabsLabBlood42F = QLineEdit()
        self.ClinicalLabsLabBlood42F.setMaxLength(4)
        self.ClinicalLabsLabBlood42F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood43L = QLabel("Lab Parameter Blood 43")
        self.ClinicalLabsLabBlood43L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood43L.setToolTip("Blood value for parameter 43")
        self.ClinicalLabsLabBlood43F = QLineEdit()
        self.ClinicalLabsLabBlood43F.setMaxLength(4)
        self.ClinicalLabsLabBlood43F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood44L = QLabel("Lab Parameter Blood 44")
        self.ClinicalLabsLabBlood44L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood44L.setToolTip("Blood value for parameter 44")
        self.ClinicalLabsLabBlood44F = QLineEdit()
        self.ClinicalLabsLabBlood44F.setMaxLength(4)
        self.ClinicalLabsLabBlood44F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood45L = QLabel("Lab Parameter Blood 45")
        self.ClinicalLabsLabBlood45L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood45L.setToolTip("Blood value for parameter 45")
        self.ClinicalLabsLabBlood45F = QLineEdit()
        self.ClinicalLabsLabBlood45F.setMaxLength(4)
        self.ClinicalLabsLabBlood45F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood46L = QLabel("Lab Parameter Blood 46")
        self.ClinicalLabsLabBlood46L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood46L.setToolTip("Blood value for parameter 46")
        self.ClinicalLabsLabBlood46F = QLineEdit()
        self.ClinicalLabsLabBlood46F.setMaxLength(4)
        self.ClinicalLabsLabBlood46F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood47L = QLabel("Lab Parameter Blood 47")
        self.ClinicalLabsLabBlood47L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood47L.setToolTip("Blood value for parameter 47")
        self.ClinicalLabsLabBlood47F = QLineEdit()
        self.ClinicalLabsLabBlood47F.setMaxLength(4)
        self.ClinicalLabsLabBlood47F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood48L = QLabel("Lab Parameter Blood 48")
        self.ClinicalLabsLabBlood48L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood48L.setToolTip("Blood value for parameter 48")
        self.ClinicalLabsLabBlood48F = QLineEdit()
        self.ClinicalLabsLabBlood48F.setMaxLength(4)
        self.ClinicalLabsLabBlood48F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood49L = QLabel("Lab Parameter Blood 49")
        self.ClinicalLabsLabBlood49L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood49L.setToolTip("Blood value for parameter 49")
        self.ClinicalLabsLabBlood49F = QLineEdit()
        self.ClinicalLabsLabBlood49F.setMaxLength(4)
        self.ClinicalLabsLabBlood49F.setValidator(QDoubleValidator())

        self.ClinicalLabsLabBlood50L = QLabel("Lab Parameter Blood 50")
        self.ClinicalLabsLabBlood50L.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsLabBlood50L.setToolTip("Blood value for parameter 50")
        self.ClinicalLabsLabBlood50F = QLineEdit()
        self.ClinicalLabsLabBlood50F.setMaxLength(4)
        self.ClinicalLabsLabBlood50F.setValidator(QDoubleValidator())

        self.ClinicalLabsEnteredL = QLabel("Entered")
        self.ClinicalLabsEnteredL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsEnteredL.setToolTip("Person who entered the data initials follwed by date entered  i.e. HA-07/22/2016")
        self.ClinicalLabsEnteredF = QLineEdit()
        self.ClinicalLabsEnteredF.setPlaceholderText("Required")

        self.ClinicalLabsCommentsL = QLabel("Comments")
        self.ClinicalLabsCommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicalLabsCommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.ClinicalLabsCommentsF = QTextEdit()

        self.ClinicalLabsSaveButton = QPushButton("Save")

        
        self.closeanthropometrics()
        self.closealertness()

        
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
        self.graphinputformalertness = QGridLayout()
        self.graphinputformanthropometrics = QGridLayout()
        self.graphinputformclinicGI = QGridLayout()
        self.graphinputformclinicallabs = QGridLayout()
        self.graphinputformdailyintake = QGridLayout()
        self.graphinputformdietrx = QGridLayout()
        self.graphinputformmeddata = QGridLayout()
        self.graphinputformmenus = QGridLayout()
        self.graphinputformothermed = QGridLayout()
        self.graphinputformseizuredata = QGridLayout()
        self.graphinputformseizureranking = QGridLayout()
        self.graphinputformurinektsg = QGridLayout()
        self.graphinputformvitals = QGridLayout()
        self.graphinputformvns = QGridLayout()


        self.groupbox.setLayout(self.middlegrid)
        self.groupbox.setContentsMargins(0,0,0,0)
        self.middlegrid.setAlignment(QtCore.Qt.AlignTop)

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

        
        self.middle.addWidget(self.newtip)
        self.middle.addLayout(self.newpatientform)
        self.middle.addWidget(self.addpatientbutton)
        
        self.graphinputformtop.addRow(self.selectgraph,self.graphselector)

        ################### Update Data Alertness ###################
        self.graphinputformalertness.addWidget(self.AlertnessMRNumberL,0,0)
        self.graphinputformalertness.addWidget(self.AlertnessMRNumberF,0,1)
        self.graphinputformalertness.addWidget(self.AlertnessDateL,1,0)
        self.graphinputformalertness.addWidget(self.AlertnessDateF,1,1)
        self.graphinputformalertness.addWidget(self.AlertnessDayTypeL,2,0)
        self.graphinputformalertness.addWidget(self.AlertnessDayTypeF,2,1)
        self.graphinputformalertness.addWidget(self.AlertnessL,3,0)
        self.graphinputformalertness.addWidget(self.AlertnessF,3,1)
        self.graphinputformalertness.addWidget(self.AlertnessActivityL,4,0)
        self.graphinputformalertness.addWidget(self.AlertnessActivityF,4,1)
        self.graphinputformalertness.addWidget(self.AlertnessDevelopmentL,5,0)
        self.graphinputformalertness.addWidget(self.AlertnessDevelopmentF,5,1)
        self.graphinputformalertness.addWidget(self.AlertnessEnteredL,6,0)
        self.graphinputformalertness.addWidget(self.AlertnessEnteredF,6,1)
        self.graphinputformalertness.addWidget(self.AlertnessCommentsL,7,0)
        self.graphinputformalertness.addWidget(self.AlertnessCommentsF,7,1)
        self.graphinputformalertness.addWidget(self.AlertnessSaveButton,8,1)


        ################### Update Data Anthropometrics ###################
        # self.graphinputformanthropometrics.setColumnStretch(3,3)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMRNumberL,0,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsMRNumberF,0,1)
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
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsPAF2,5,2)
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
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsEnteredL,18,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsEnteredF,18,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCommentsL,20,0)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsCommentsF,20,1)
        self.graphinputformanthropometrics.addWidget(self.AnthropometricsSaveButton,21,1)

        ################### Update Data Clinic GI Issues ###################
        self.graphinputformclinicGI.addWidget(self.ClinicGIMRNumberL,0,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIMRNumberF,0,1)    
        self.graphinputformclinicGI.addWidget(self.ClinicGIDateL,1,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDateF,1,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDayTypeL,2,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDayTypeF,2,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstL,3,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstF,3,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaL,4,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaF,4,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomL,5,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomF,5,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaL,6,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaF,6,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagL,7,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagF,7,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINissenL,8,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINissenF,8,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstDesL,9,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstDesF,9,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaDesL,10,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaDesF,10,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomDesL,11,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomDesF,11,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaDesL,12,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaDesF,12,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagDesL,13,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagDesF,13,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIEnteredL,14,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIEnteredF,14,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGICommentsL,15,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGICommentsF,15,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGISaveButton,16,1)

        ################### Update Data Clinical Labs ###################
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMRNumberL,0,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMRNumberF,0,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsDateL,1,0)    
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsDateF,1,1)    
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTimeL,2,0)    
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTimeF,2,1)    
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsDayTypeL,3,0) 
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsDayTypeF,3,1) 
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsSourceL,4,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsSourceF,4,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsFastingL,5,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsFastingF,5,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTGBloodL,6,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTGBloodF,6,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHDLBloodL,7,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHDLBloodF,7,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLDLBloodL,8,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLDLBloodF,8,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTCBloodL,9,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTCBloodF,9,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNABloodL,10,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNABloodF,10,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsKBloodL,11,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsKBloodF,11,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsChlBloodL,12,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsChlBloodF,12,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCO2BloodL,13,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCO2BloodF,13,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBUNBloodL,14,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBUNBloodF,14,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCrBloodL,15,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCrBloodF,15,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsGlusBloodL,16,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsGlusBloodF,16,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCaBloodL,17,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCaBloodF,17,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMagBloodL,18,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMagBloodF,18,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsPhosBloodL,19,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsPhosBloodF,19,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsUricAcidBloodL,20,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsUricAcidBloodF,20,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsProBloodL,21,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsProBloodF,21,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAlbBloodL,22,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAlbBloodF,22,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTBilBloodL,23,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTBilBloodF,23,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTotalBilirubinBloodL,24,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsTotalBilirubinBloodF,24,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAstBloodL,25,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAstBloodF,25,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAltBloodL,26,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAltBloodF,26,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsRBCBloodL,27,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsRBCBloodF,27,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHgbBloodL,28,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHgbBloodF,28,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHctBloodL,29,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsHctBloodF,29,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsPlateletBloodL,30,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsPlateletBloodF,30,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCVBloodL,31,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCVBloodF,31,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCHBloodL,32,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCHBloodF,32,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCHCBloodL,33,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMCHCBloodF,33,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMPVBloodL,34,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMPVBloodF,34,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsRDWBloodL,35,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsRDWBloodF,35,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsWBCBloodL,36,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsWBCBloodF,36,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAmmoniaBloodL,37,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAmmoniaBloodF,37,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBHbBloodL,38,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBHbBloodF,38,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAcacBloodL,39,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsAcacBloodF,39,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNeutrophilsBloodL,40,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNeutrophilsBloodF,40,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLymphocytesBloodL,41,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLymphocytesBloodF,41,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMonocytesBloodL,42,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsMonocytesBloodF,42,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEosinophilsBloodL,43,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEosinophilsBloodF,43,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBasophilsBloodL,44,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBasophilsBloodF,44,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLargeUnstainedCellsBloodL,45,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLargeUnstainedCellsBloodF,45,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNeutrophilsAbsoluteBloodL,46,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsNeutrophilsAbsoluteBloodF,46,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLymphocytesAbsoluteBloodL,47,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLymphocytesAbsoluteBloodF,47,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEosinophilsAbsoluteBloodL,48,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEosinophilsAbsoluteBloodF,48,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBasophilsAbsoluteBloodL,49,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsBasophilsAbsoluteBloodF,49,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsGlusBloodCRCL,50,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsGlusBloodCRCF,50,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLactBloodCRCMmolL,51,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLactBloodCRCMmolF,51,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood1L,53,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood1F,53,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood2L,54,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood2F,54,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood3L,55,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood3F,55,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood4L,56,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood4F,56,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood5L,57,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood5F,57,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood6L,58,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood6F,58,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood7L,59,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood7F,59,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood8L,60,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood8F,60,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood9L,61,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood9F,61,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood10L,62,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood10F,62,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood11L,63,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood11F,63,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood12L,64,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood12F,64,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood13L,65,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood13F,65,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood14L,66,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood14F,66,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood15L,67,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood15F,67,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood16L,68,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood16F,68,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood17L,69,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood17F,69,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood18L,70,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood18F,70,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood19L,71,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood19F,71,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood20L,72,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood20F,72,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood21L,73,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood21F,73,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood22L,74,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood22F,74,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood23L,75,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood23F,75,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood24L,76,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood24F,76,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood25L,77,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood25F,77,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood26L,78,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood26F,78,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood27L,79,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood27F,79,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood28L,80,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood28F,80,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood29L,81,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood29F,81,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood30L,82,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood30F,82,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood31L,83,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood31F,83,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood32L,84,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood32F,84,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood33L,85,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood33F,85,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood34L,86,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood34F,86,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood35L,87,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood35F,87,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood36L,88,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood36F,88,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood37L,89,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood37F,89,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood38L,90,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood38F,90,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood39L,91,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood39F,91,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood40L,92,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood40F,92,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood41L,93,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood41F,93,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood42L,94,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood42F,94,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood43L,95,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood43F,95,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood44L,96,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood44F,96,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood45L,97,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood45F,97,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood46L,98,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood46F,98,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood47L,99,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood47F,99,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood48L,100,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood48F,100,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood49L,101,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood49F,101,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood50L,102,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsLabBlood50F,102,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEnteredL,103,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsEnteredF,103,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCommentsL,104,0)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsCommentsF,104,1)
        self.graphinputformclinicallabs.addWidget(self.ClinicalLabsSaveButton,105,1)


#         names = ["MRNumber","Date","Time","DayType","Source","Fasting","TGBlood","HDLBlood","LDLBlood","TCBlood","NABlood","KBlood","ChlBlood","CO2Blood","BUNBlood","CrBlood","GlusBlood","CaBlood","MagBlood","PhosBlood","UricAcidBlood","ProBlood",
# "AlbBlood","TBilBlood","TotalBilirubinBlood","AstBlood","AltBlood","RBCBlood","HgbBlood","HctBlood","PlateletBlood","MCVBlood","MCHBlood","MCHCBlood","MPVBlood","RDWBlood","WBCBlood","AmmoniaBlood","BHbBlood","AcacBlood", 
# "NeutrophilsBlood","LymphocytesBlood","MonocytesBlood","EosinophilsBlood","BasophilsBlood","LargeUnstainedCellsBlood","NeutrophilsAbsoluteBlood","LymphocytesAbsoluteBlood","EosinophilsAbsoluteBlood","BasophilsAbsoluteBlood",
# "GlusBloodCRC","LactBloodCRCMmol"]
#         for el in names:
#             print("self.ClinicalLabs"+el+"F.text(),")
           

#         for ind in range(1,51):
#             # print("self.ClinicalLabsLabBlood"+str(ind)+"L.text()")
#             print("self.ClinicalLabsLabBlood"+str(ind)+"F.text(),")
            
        
        ################### Update Data Daily Intake ###################
        self.graphinputformdailyintake.addWidget(self.DailyIntakeMRNumberL,0,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeMRNumberF,0,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDateL,1,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDateF,1,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDayTypeL,2,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDayTypeF,2,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakePKTNUML,3,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakePKTNUMF,3,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDataQualityDietL,4,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDataQualityDietF,4,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDayQualityDietL,5,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeDayQualityDietF,5,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeEnteredL,6,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeEnteredF,6,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeCommentsL,7,0)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeCommentsF,7,1)
        self.graphinputformdailyintake.addWidget(self.DailyIntakeSaveButton,8,1)
        
        ################### Update Data Diet RX ###################
        self.graphinputformdietrx.addWidget(self.DietRXMRNumberL,0,0)
        self.graphinputformdietrx.addWidget(self.DietRXMRNumberF,0,1)
        self.graphinputformdietrx.addWidget(self.DietRXDateL,1,0)
        self.graphinputformdietrx.addWidget(self.DietRXDateF,1,1)
        self.graphinputformdietrx.addWidget(self.DietRXDayTypeL,2,0)
        self.graphinputformdietrx.addWidget(self.DietRXDayTypeF,2,1)
        self.graphinputformdietrx.addWidget(self.DietRXROFL,3,0)
        self.graphinputformdietrx.addWidget(self.DietRXROFF,3,1)
        self.graphinputformdietrx.addWidget(self.DietRXRFCDL,4,0)
        self.graphinputformdietrx.addWidget(self.DietRXRFCDF,4,1)
        self.graphinputformdietrx.addWidget(self.DietRXSnackCalL,5,0)
        self.graphinputformdietrx.addWidget(self.DietRXSnackCalF,5,1)
        self.graphinputformdietrx.addWidget(self.DietRXSnackRatioL,6,0)
        self.graphinputformdietrx.addWidget(self.DietRXSnackRatioF,6,1)
        self.graphinputformdietrx.addWidget(self.DietRXSnackNumberL,7,0)
        self.graphinputformdietrx.addWidget(self.DietRXSnackNumberF,7,1)
        self.graphinputformdietrx.addWidget(self.DietRXMealNumberL,8,0)
        self.graphinputformdietrx.addWidget(self.DietRXMealNumberF,8,1)
        self.graphinputformdietrx.addWidget(self.DietRXMealRatioL,9,0)
        self.graphinputformdietrx.addWidget(self.DietRXMealRatioF,9,1)
        self.graphinputformdietrx.addWidget(self.DietRXCalL,10,0)
        self.graphinputformdietrx.addWidget(self.DietRXCalF,10,1)
        self.graphinputformdietrx.addWidget(self.DietRXProL,11,0)
        self.graphinputformdietrx.addWidget(self.DietRXProF,11,1)
        self.graphinputformdietrx.addWidget(self.DietRXEnteredL,12,0)
        self.graphinputformdietrx.addWidget(self.DietRXEnteredF,12,1)
        self.graphinputformdietrx.addWidget(self.DietRXCommentsL,13,0)
        self.graphinputformdietrx.addWidget(self.DietRXCommentsF,13,1)
        self.graphinputformdietrx.addWidget(self.DietRXSaveButton,14,1)
        
        ################### Update Data Med Data ###################
        self.graphinputformmeddata.addWidget(self.MedDataMRNumberL,0,0)
        self.graphinputformmeddata.addWidget(self.MedDataMRNumberF,0,1)
        self.graphinputformmeddata.addWidget(self.MedDataDateL,1,0)
        self.graphinputformmeddata.addWidget(self.MedDataDateF,1,1)
        self.graphinputformmeddata.addWidget(self.MedDataDayTypeL,2,0)
        self.graphinputformmeddata.addWidget(self.MedDataDayTypeF,2,1)
        self.graphinputformmeddata.addWidget(self.MedDataNDIDL,3,0)
        self.graphinputformmeddata.addWidget(self.MedDataNDIDF,3,1)
        self.graphinputformmeddata.addWidget(self.MedDataMedIDL,4,0)
        self.graphinputformmeddata.addWidget(self.MedDataMedIDF,4,1)
        self.graphinputformmeddata.addWidget(self.MedDataRFCML,5,0)
        self.graphinputformmeddata.addWidget(self.MedDataRFCMF,5,1)
        self.graphinputformmeddata.addWidget(self.MedDataProdNameL,6,0)
        self.graphinputformmeddata.addWidget(self.MedDataProdNameF,6,1)
        self.graphinputformmeddata.addWidget(self.MedDataDailyDoseL,7,0)
        self.graphinputformmeddata.addWidget(self.MedDataDailyDoseF,7,1)
        self.graphinputformmeddata.addWidget(self.MedDataMedDosesL,8,0)
        self.graphinputformmeddata.addWidget(self.MedDataMedDosesF,8,1)
        self.graphinputformmeddata.addWidget(self.MedDataMedCommentsL,9,0)
        self.graphinputformmeddata.addWidget(self.MedDataMedCommentsF,9,1)
        self.graphinputformmeddata.addWidget(self.MedDataEnteredL,10,0)
        self.graphinputformmeddata.addWidget(self.MedDataEnteredF,10,1)
        self.graphinputformmeddata.addWidget(self.MedDataCommentsL,11,0)
        self.graphinputformmeddata.addWidget(self.MedDataCommentsF,11,1)
        self.graphinputformmeddata.addWidget(self.MedDataSaveButton,12,1)

        ################### Update Data Menus ###################
        self.graphinputformmenus.addWidget(self.MenusMRNumberL,0,0)
        self.graphinputformmenus.addWidget(self.MenusMRNumberF,0,1)
        self.graphinputformmenus.addWidget(self.MenusDateL,1,0)
        self.graphinputformmenus.addWidget(self.MenusDateF,1,1)
        self.graphinputformmenus.addWidget(self.MenusCalPrcntL,2,0)
        self.graphinputformmenus.addWidget(self.MenusCalPrcntF,2,1)
        self.graphinputformmenus.addWidget(self.MenusProcntPrcntL,3,0)
        self.graphinputformmenus.addWidget(self.MenusProcntPrcntF,3,1)
        self.graphinputformmenus.addWidget(self.MenusRatioPrL,4,0 )
        self.graphinputformmenus.addWidget(self.MenusRatioPrF,4,1)
        self.graphinputformmenus.addWidget(self.MenusMealNumberL,6,0)
        self.graphinputformmenus.addWidget(self.MenusMealNumberF,6,1)
        self.graphinputformmenus.addWidget(self.MenusSnackNumberL,7,0)
        self.graphinputformmenus.addWidget(self.MenusSnackNumberF,7,1)
        self.graphinputformmenus.addWidget(self.MenusRecipeNameL,8,0)
        self.graphinputformmenus.addWidget(self.MenusRecipeNameF,8,1)
        self.graphinputformmenus.addWidget(self.MenusRecipeNumberL,9,0)
        self.graphinputformmenus.addWidget(self.MenusRecipeNumberF,9,1)
        self.graphinputformmenus.addWidget(self.MenusRecipeIngredientAmountL,10,0)
        self.graphinputformmenus.addWidget(self.MenusRecipeIngredientAmountF,10,1)
        self.graphinputformmenus.addWidget(self.MenusNDIDL,11,0)
        self.graphinputformmenus.addWidget(self.MenusNDIDF,11,1)
        self.graphinputformmenus.addWidget(self.MenusProdNameL,12,0)
        self.graphinputformmenus.addWidget(self.MenusProdNameF,12,1)
        self.graphinputformmenus.addWidget(self.MenusRecipeTypeL,13,0)
        self.graphinputformmenus.addWidget(self.MenusRecipeTypeF,13,1)
        self.graphinputformmenus.addWidget(self.MenusEnteredL,14,0)
        self.graphinputformmenus.addWidget(self.MenusEnteredF,14,1)
        self.graphinputformmenus.addWidget(self.MenusCommentsL,15,0)
        self.graphinputformmenus.addWidget(self.MenusCommentsF,15,1)
        self.graphinputformmenus.addWidget(self.MenusSaveButton,16,1)
        
        ################### Update Data Other Med ###################
        self.graphinputformothermed.addWidget(self.OtherMedMRNumberL,0,0)
        self.graphinputformothermed.addWidget(self.OtherMedMRNumberF,0,1)
        self.graphinputformothermed.addWidget(self.OtherMedDateL,1,0)
        self.graphinputformothermed.addWidget(self.OtherMedDateF,1,1)
        self.graphinputformothermed.addWidget(self.OtherMedNDIDL,2,0)
        self.graphinputformothermed.addWidget(self.OtherMedNDIDF,2,1)
        self.graphinputformothermed.addWidget(self.OtherMedProdNameL,3,0)
        self.graphinputformothermed.addWidget(self.OtherMedProdNameF,3,1)
        self.graphinputformothermed.addWidget(self.OtherMedMedAmountL,4,0)
        self.graphinputformothermed.addWidget(self.OtherMedMedAmountF,4,1)
        self.graphinputformothermed.addWidget(self.OtherMedMedUnitL,5,0)
        self.graphinputformothermed.addWidget(self.OtherMedMedUnitF,5,1)
        self.graphinputformothermed.addWidget(self.OtherMedEnteredL,6,0)
        self.graphinputformothermed.addWidget(self.OtherMedEnteredF,6,1)
        self.graphinputformothermed.addWidget(self.OtherMedCommentsL,7,0)
        self.graphinputformothermed.addWidget(self.OtherMedCommentsF,7,1)
        self.graphinputformothermed.addWidget(self.OtherMedSaveButton,8,1)

        ################### Update Data Seizure Data ###################
        self.graphinputformseizuredata.addWidget(self.SeizureDataMRNumberL,0,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataMRNumberF,0,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDateL,1,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDateF,1,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDayTypeL,2,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDayTypeF,2,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDataQualityL,3,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataDataQualityF,3,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureSeverityL,4,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureSeverityF,4,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureLengthL,5,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureLengthF,5,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureTypeL,6,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureTypeF,6,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureVariableL,7,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureVariableF,7,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureNumberL,8,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureNumberF,8,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureClusterL,9,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSeizureClusterF,9,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataEnteredL,10,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataEnteredF,10,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataCommentsL,11,0)
        self.graphinputformseizuredata.addWidget(self.SeizureDataCommentsF,11,1)
        self.graphinputformseizuredata.addWidget(self.SeizureDataSaveButton,12,1)
        
        ################### Update Data Seizure Ranking ###################
        self.graphinputformseizureranking.addWidget(self.SeizureRankingMRNumberL,0,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingMRNumberF,0,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureParameterL,1,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureParameterF,1,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureEntryL,2,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureEntryF,2,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureRankingL,3,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSeizureRankingF,3,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingEnteredL,4,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingEnteredF,4,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingCommentsL,5,0)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingCommentsF,5,1)
        self.graphinputformseizureranking.addWidget(self.SeizureRankingSaveButton,6,1)
        
        ################### Update Data Urine Kt SG ###################
        self.graphinputformurinektsg.addWidget(self.UrineKtSGMRNumberL,0,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGMRNumberF,0,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGDateL,1,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGDateF,1,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGDayTypeL,2,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGDayTypeF,2,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGUrineKtL,3,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGUrineKtF,3,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGUrineSGL,4,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGUrineSGF,4,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGEnteredL,5,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGEnteredF,5,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGCommentsL,6,0)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGCommentsF,6,1)
        self.graphinputformurinektsg.addWidget(self.UrineKtSGSaveButton,7,1)

        ################### Update Data Vitals ###################
        self.graphinputformvitals.addWidget(self.VitalsMRNumberL,0,0)
        self.graphinputformvitals.addWidget(self.VitalsMRNumberF,0,1)
        self.graphinputformvitals.addWidget(self.VitalsDateL,1,0)
        self.graphinputformvitals.addWidget(self.VitalsDateF,1,1)
        self.graphinputformvitals.addWidget(self.VitalsDayTypeL,2,0)
        self.graphinputformvitals.addWidget(self.VitalsDayTypeF,2,1)
        self.graphinputformvitals.addWidget(self.VitalsSourceL,3,0)
        self.graphinputformvitals.addWidget(self.VitalsSourceF,3,1)
        self.graphinputformvitals.addWidget(self.VitalsBPSysL,4,0)
        self.graphinputformvitals.addWidget(self.VitalsBPSysF,4,1)
        self.graphinputformvitals.addWidget(self.VitalsBPDiaL,5,0)
        self.graphinputformvitals.addWidget(self.VitalsBPDiaF,5,1)
        self.graphinputformvitals.addWidget(self.VitalsTempL,6,0)
        self.graphinputformvitals.addWidget(self.VitalsTempF,6,1)
        self.graphinputformvitals.addWidget(self.VitalsRRL,7,0)
        self.graphinputformvitals.addWidget(self.VitalsRRF,7,1)
        self.graphinputformvitals.addWidget(self.VitalsHRL,8,0)
        self.graphinputformvitals.addWidget(self.VitalsHRF,8,1)
        self.graphinputformvitals.addWidget(self.VitalsEnteredL,9,0)
        self.graphinputformvitals.addWidget(self.VitalsEnteredF,9,1)
        self.graphinputformvitals.addWidget(self.VitalsCommentsL,10,0)
        self.graphinputformvitals.addWidget(self.VitalsCommentsF,10,1)
        self.graphinputformvitals.addWidget(self.VitalsSaveButton,11,1)

        ################### Update Data VNS ###################
        self.graphinputformvns.addWidget(self.VNSMRNumberL,0,0)
        self.graphinputformvns.addWidget(self.VNSMRNumberF,0,1)
        self.graphinputformvns.addWidget(self.VNSDateL,1,0)
        self.graphinputformvns.addWidget(self.VNSDateF,1,1)
        self.graphinputformvns.addWidget(self.VNSDayTypeL,2,0)
        self.graphinputformvns.addWidget(self.VNSDayTypeF,2,1)
        self.graphinputformvns.addWidget(self.VNSMRMagActL,3,0)
        self.graphinputformvns.addWidget(self.VNSMRMagActF,3,1)
        self.graphinputformvns.addWidget(self.VNSOutputCurrL,4,0)
        self.graphinputformvns.addWidget(self.VNSOutputCurrF,4,1)
        self.graphinputformvns.addWidget(self.VNSVNSFrequencyL,5,0)
        self.graphinputformvns.addWidget(self.VNSVNSFrequencyF,5,1)
        self.graphinputformvns.addWidget(self.VNSPulseWidthL,6,0)
        self.graphinputformvns.addWidget(self.VNSPulseWidthF,6,1)
        self.graphinputformvns.addWidget(self.VNSSignalOnL,7,0)
        self.graphinputformvns.addWidget(self.VNSSignalOnF,7,1)
        self.graphinputformvns.addWidget(self.VNSSignalOffL,8,0)
        self.graphinputformvns.addWidget(self.VNSSignalOffF,8,1)
        self.graphinputformvns.addWidget(self.VNSMagnetCurrentL,9,0)
        self.graphinputformvns.addWidget(self.VNSMagnetCurrentF,9,1)
        self.graphinputformvns.addWidget(self.VNSMagnetOnL,10,0)
        self.graphinputformvns.addWidget(self.VNSMagnetOnF,10,1)
        self.graphinputformvns.addWidget(self.VNSMagnetPulseL,11,0)
        self.graphinputformvns.addWidget(self.VNSMagnetPulseF,11,1)
        self.graphinputformvns.addWidget(self.VNSLeadTestL,12,0)
        self.graphinputformvns.addWidget(self.VNSLeadTestF,12,1)
        self.graphinputformvns.addWidget(self.VNSEnteredL,13,0)
        self.graphinputformvns.addWidget(self.VNSEnteredF,13,1)
        self.graphinputformvns.addWidget(self.VNSCommentsL,14,0)
        self.graphinputformvns.addWidget(self.VNSCommentsF,14,1)
        self.graphinputformvns.addWidget(self.VNSSaveButton,15,1)

        
        # Set Up Scroll Boxes 
############################### Alertness ###############################
        
        self.alertnessbox = QGroupBox()
        self.alertnessbox.setLayout(self.graphinputformalertness)
        self.alertnessformscroll = QScrollArea()

        self.alertnessformscroll.setWidget(self.alertnessbox)
        self.alertnessformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.alertnessformscroll)

############################### Anthropometrics ###############################

        self.anthropometricsbox = QGroupBox()
        self.anthropometricsbox.setLayout(self.graphinputformalertness)
        self.anthropometricsformscroll = QScrollArea()

        self.anthropometricsformscroll.setWidget(self.anthropometricsbox)
        self.anthropometricsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.anthropometricsformscroll)

############################### Clinic GI ###############################

        self.clinicGIbox = QGroupBox()
        self.clinicGIbox.setLayout(self.graphinputformclinicGI)
        
        self.clinicGIformscroll = QScrollArea()
        self.clinicGIformscroll.setWidget(self.clinicGIbox)
        self.clinicGIformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.clinicGIformscroll)

############################### Clinical Labs ###############################

        self.clinicallabsbox = QGroupBox()
        self.clinicallabsbox.setLayout(self.graphinputformclinicallabs)
        
        self.clinicallabsformscroll = QScrollArea()
        self.clinicallabsformscroll.setWidget(self.clinicallabsbox)
        self.clinicallabsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.clinicallabsformscroll)

############################### Daily Intake ###############################
        
        self.dailyIntakebox = QGroupBox()
        self.dailyIntakebox.setLayout(self.graphinputformdailyintake)
        
        self.dailyIntakeformscroll = QScrollArea()
        self.dailyIntakeformscroll.setWidget(self.dailyIntakebox)
        self.dailyIntakeformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.dailyIntakeformscroll)

############################### Diet Rx ###############################

        self.dietrxbox = QGroupBox()
        self.dietrxbox.setLayout(self.graphinputformdietrx)
        
        self.dietrxformscroll = QScrollArea()
        self.dietrxformscroll.setWidget(self.dietrxbox)
        self.dietrxformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.dietrxformscroll)

############################### Med Data ###############################

        self.meddatabox = QGroupBox()
        self.meddatabox.setLayout(self.graphinputformmeddata)
        
        self.meddataformscroll = QScrollArea()
        self.meddataformscroll.setWidget(self.meddatabox)
        self.meddataformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.meddataformscroll)

############################### Menus ###############################

        self.menusbox = QGroupBox()
        self.menusbox.setLayout(self.graphinputformmenus)
        
        self.menusformscroll = QScrollArea()
        self.menusformscroll.setWidget(self.menusbox)
        self.menusformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.menusformscroll)

############################### Other Med ###############################

        self.othermedbox = QGroupBox()
        self.othermedbox.setLayout(self.graphinputformothermed)
        
        self.othermedformscroll = QScrollArea()
        self.othermedformscroll.setWidget(self.othermedbox)
        self.othermedformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.othermedformscroll)


############################### Seizure Data ###############################

        self.seizuredatabox = QGroupBox()
        self.seizuredatabox.setLayout(self.graphinputformseizuredata)
        
        self.seizuredataformscroll = QScrollArea()
        self.seizuredataformscroll.setWidget(self.seizuredatabox)
        self.seizuredataformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.seizuredataformscroll)

############################### Seizure Ranking ###############################

        self.seizurerankingbox = QGroupBox()
        self.seizurerankingbox.setLayout(self.graphinputformseizureranking)
        
        self.seizurerankingformscroll = QScrollArea()
        self.seizurerankingformscroll.setWidget(self.seizurerankingbox)
        self.seizurerankingformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.seizurerankingformscroll)

############################### Urine Kt SG ###############################

        self.urineKtSGbox = QGroupBox()
        self.urineKtSGbox.setLayout(self.graphinputformurinektsg)
        
        self.urineKtSGformscroll = QScrollArea()
        self.urineKtSGformscroll.setWidget(self.urineKtSGbox)
        self.urineKtSGformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.urineKtSGformscroll)

############################### Vitals ###############################

        self.vitalsbox = QGroupBox()
        self.vitalsbox.setLayout(self.graphinputformvitals)
        
        self.vitalsformscroll = QScrollArea()
        self.vitalsformscroll.setWidget(self.vitalsbox)
        self.vitalsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.vitalsformscroll)           

############################### VNS ###############################

        self.vnsbox = QGroupBox()
        self.vnsbox.setLayout(self.graphinputformvns)
        
        self.vnsformscroll = QScrollArea()
        self.vnsformscroll.setWidget(self.vnsbox)
        self.vnsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.vnsformscroll)  
        

#####################################################    
        self.middle.addLayout(self.graphinputformtop)
    
        
        
        self.middle.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        self.rightlayout.addLayout(self.topbar,10)
        self.rightlayout.addLayout(self.middle,90)

        self.sidebar.setContentsMargins(0,0,200,0)

        # self.middlegrid.addWidget(self.middlescrollarea)

        self.mainlayout.addLayout(self.sidebar,10)
        self.mainlayout.addLayout(self.rightlayout,90)

        self.setLayout(self.mainlayout)

#################################################################################################################################################################
        ################### Event Calling ###################
        self.logo.mousePressEvent = self.handlelogo
        self.newpatientbuttion.mousePressEvent = self.handlenewpatient
        self.addpatientbutton.mousePressEvent = self.addnewpatient
        self.graphlist.itemClicked.connect(self.handlelist)    

        self.confirmbutton.mousePressEvent = self.handlesearch
        self.logoutbutton.mousePressEvent = self.handlelogout
        # self.searchbar.textChanged.connect(self.handlesearch)
    
        self.updateinfobutton.mousePressEvent = self.handleupdate

        self.graphselector.currentIndexChanged.connect (self.handlegraphselection)

        self.AlertnessSaveButton.mousePressEvent = self.submitAlertness
        self.AnthropometricsSaveButton.mousePressEvent = self.submitAnthropometrics
        self.ClinicGISaveButton.mousePressEvent = self.submitClinicGI
        self.ClinicalLabsSaveButton.mousePressEvent = self.submitClinicalLabs
        self.DailyIntakeSaveButton.mousePressEvent = self.submitDailyIntake
        self.DietRXSaveButton.mousePressEvent = self.submitDietRX
        self.MedDataSaveButton.mousePressEvent = self.submitMedData
        self.MenusSaveButton.mousePressEvent = self.submitMenus
        self.OtherMedSaveButton.mousePressEvent = self.submitOtherMed
        self.SeizureDataSaveButton.mousePressEvent = self.submitSeizureData
        self.SeizureRankingSaveButton.mousePressEvent = self.submitSeizureRanking
        self.UrineKtSGSaveButton.mousePressEvent = self.submitUrineKtSG
        self.VitalsSaveButton.mousePressEvent = self.submitVitals
        self.VNSSaveButton.mousePressEvent = self.submitVNS




        self.loadpatients()
        self.closeprofile()
        self.closenewpatient()
        self.graphselector.close()
        self.selectgraph.close()
        self.closeallfroms()
        self.removeallforms()


        # self.closedashboard()

        self.foundpatients = [] 
        self.foundpatientbuttons = []




################### Event Handling ###################

    def handlelogo(self,event):
        self.opendashboard()
        self.closeprofile()
        self.closenewpatient()
        self.loadpatients()
        
        self.graphselector.setCurrentIndex(0)
        self.graphselector.close()
        self.selectgraph.close()
        self.closeallfroms()
        self.removeallforms()
        self.resetinputs()
        
        try:
            self.anthropometricsGraph.close()
        except AttributeError:
            pass
    


        
    def handlelist(self,item):
        
        self.closedashboard()
        self.closeprofile()
        self.closeallfroms()
        self.removeallforms()
        self.graphselector.close()

        self.closenewpatient()
    
        
        try: 
            if(self.anthropometricsGraph):
                self.anthropometricsGraph.close()
        
        except AttributeError:
            print("Creating First Graph")
        
        if("Anthropometrics" in item.text()):
            self.anthropometricsGraph = Canvas(self.currentpatient)
            # self.anthropometricsGraph.move(0,0)
            self.anthropometricsGraph.close()
            self.middle.addWidget(self.anthropometricsGraph)


        # print(item.text())

    def handlesearch(self,event):
        search = self.searchbar.text()
        i = 0
        j = 0
       
        if search != "":
            
            #### Close All Patient Buttons & Delete them ####
            num = 1
            # Close full list  
            for p in self.allpatientbuttons:
                print(str(num) +p.text())
                p.deleteLater()
                num += 1
            
            self.allpatientbuttons.clear()

            #### Close Found Patients if Previous Ones exist ####
            if(len(self.foundpatientbuttons) > 0):
                print("Deleting Previous Found Buttons")
                for f in self.foundpatientbuttons:
                    print("Closing "+ f.text())
                    self.middlegrid.removeWidget(f)
                    f.deleteLater()
                self.foundpatientbuttons.clear()  
            
            # Clear Found Patients list
            self.foundpatients.clear()
                      
            #### Search for Matches ####
        
            for p in self.allpatients:
                if (p.find(search) > -1):
                    self.foundpatients.append(p)
                    
            #### Create Buttons For Each Match ####
            for patient in self.foundpatients:
                print("Created New Button for " + patient)
                self.patientbtn2 = QPushButton("Patient ID: " + patient)
                self.middlegrid.addWidget(self.patientbtn2,i,j)
                self.patientbtn2.clicked.connect(self.openprofile)
                self.foundpatientbuttons.append(self.patientbtn2)

                j+=1

                if(j%5 == 0):
                    i+=1
                    j=0
            
            self.middlescrollarea.close()
            self.middlescrollarea.show()
            
            print("--------------------------------------------")
            print("Total Patients " + str(len(self.allpatients)))
            print("Total old buttons " + str(len(self.allpatientbuttons)))

            print("Total Patients found that match " + str(len(self.foundpatients)))
            print("Number of new buttons " + str(len(self.foundpatientbuttons)))

        self.searchbar.setText("")
        self.closeallfroms()
        self.removeallforms()
        self.closenewpatient()
        self.closeprofile()
        try:
            self.anthropometricsGraph.close()
        except AttributeError:
            print("No Graph to delete")
    
    def handlelogout(self,event):
        log = Login()
        self.close()
        log.show()
    
    def handlenewpatient (self,event):
        print("New Patient Clicked")
        
        # Close everything else
        self.closedashboard()
        self.closeprofile()
        self.opennewpatient()
        self.graphselector.setCurrentIndex(0)
        self.graphselector.close()
        self.selectgraph.close()
        self.closeallfroms()
        self.removeallforms()
        self.resetinputs()

        try:
            self.anthropometricsGraph.close()
        except AttributeError:
            print("No Graph to delete")


                
    def addnewpatient(self,event):
        if (self.nameinput.text != ''):
            setNewPatient(self.nameinput.text())
            self.nameinput.setText('')

        # Eventually I need to make sure it can only be 10 chars, but for now this is ok 
      
    def handleupdate(self, event):
        self.closeprofile()
        self.middle.addLayout(self.graphinputformtop)
        self.currentpatienttext.show()
        self.graphselector.show()
        self.selectgraph.show()
        

    def handlegraphselection(self, event):
        selection = (self.graphselector.currentText())
        

        if (selection == "Alertness"):
            self.closeallfroms()
            self.removeallforms()

            # self.middle.addLayout(self.graphinputformalertness)
            self.alertnessbox = QGroupBox()
            self.alertnessbox.setLayout(self.graphinputformalertness)
            
            self.alertnessformscroll = QScrollArea()
            self.alertnessformscroll.setWidget(self.alertnessbox)
            self.alertnessformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.alertnessformscroll)

            # self.graphinputformalertness.setContentsMargins(200,0,200,0)
            self.openalertness()

        if (selection == "Anthropometrics"): 
            self.closeallfroms()
            self.removeallforms()

            # self.middle.addLayout(self.graphinputformanthropometrics)
            self.anthropometricsbox = QGroupBox()
            self.anthropometricsbox.setLayout(self.graphinputformanthropometrics)
            
            self.anthropometricsformscroll = QScrollArea()
            self.anthropometricsformscroll.setWidget(self.anthropometricsbox)
            self.anthropometricsformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.anthropometricsformscroll)

            # self.graphinputformanthropometrics.setContentsMargins(200,0,200,0)
            self.openanthropometrics()

        if (selection == "Clinic GI Issues"):
            self.closeallfroms()
            self.removeallforms()

            # self.middle.addLayout(self.graphinputformclinicGI)
            self.clinicGIbox = QGroupBox()
            self.clinicGIbox.setLayout(self.graphinputformclinicGI)
            
            self.clinicGIformscroll = QScrollArea()
            self.clinicGIformscroll.setWidget(self.clinicGIbox)
            self.clinicGIformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.clinicGIformscroll)

            # self.graphinputformclinicGI.setContentsMargins(200,0,200,0)
            self.openclinicgi()

        if (selection == "Clinical Labs"):
            self.closeallfroms()
            self.removeallforms()

            self.clinicallabsbox = QGroupBox()
            self.clinicallabsbox.setLayout(self.graphinputformclinicallabs)
            
            self.clinicallabsformscroll = QScrollArea()
            self.clinicallabsformscroll.setWidget(self.clinicallabsbox)
            self.clinicallabsformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.clinicallabsformscroll)

            self.openclinicallabs()

        if (selection == "Daily Intake"):
            self.closeallfroms()
            self.removeallforms()

            self.dailyIntakebox = QGroupBox()
            self.dailyIntakebox.setLayout(self.graphinputformdailyintake)
            
            self.dailyIntakeformscroll = QScrollArea()
            self.dailyIntakeformscroll.setWidget(self.dailyIntakebox)
            self.dailyIntakeformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.dailyIntakeformscroll)

            # self.graphinputformdailyintake.setContentsMargins(200,0,200,0)
            self.opendailyintake()

        if (selection == "Diet RX"):
            self.closeallfroms()
            self.removeallforms()


            self.dietrxbox = QGroupBox()
            self.dietrxbox.setLayout(self.graphinputformdietrx)
            
            self.dietrxformscroll = QScrollArea()
            self.dietrxformscroll.setWidget(self.dietrxbox)
            self.dietrxformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.dietrxformscroll)

            self.opendietrx()

        if (selection == "Med Data"):
            self.closeallfroms()
            self.removeallforms()

            self.meddatabox = QGroupBox()
            self.meddatabox.setLayout(self.graphinputformmeddata)
            
            self.meddataformscroll = QScrollArea()
            self.meddataformscroll.setWidget(self.meddatabox)
            self.meddataformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.meddataformscroll)

            self.openmeddata()
        
        if (selection == "Menus"):
            self.closeallfroms()
            self.removeallforms()

            self.menusbox = QGroupBox()
            self.menusbox.setLayout(self.graphinputformmenus)
            
            self.menusformscroll = QScrollArea()
            self.menusformscroll.setWidget(self.menusbox)
            self.menusformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.menusformscroll)

            self.openmenus()

        if (selection == "Other Med"):
            self.closeallfroms()
            self.removeallforms()

            self.othermedbox = QGroupBox()
            self.othermedbox.setLayout(self.graphinputformothermed)
            
            self.othermedformscroll = QScrollArea()
            self.othermedformscroll.setWidget(self.othermedbox)
            self.othermedformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.othermedformscroll)

            self.openothermed()

        if (selection == "Seizure Data"):
            self.closeallfroms()
            self.removeallforms()

            self.seizuredatabox = QGroupBox()
            self.seizuredatabox.setLayout(self.graphinputformseizuredata)
            
            self.seizuredataformscroll = QScrollArea()
            self.seizuredataformscroll.setWidget(self.seizuredatabox)
            self.seizuredataformscroll.setWidgetResizable(True)
            
            self.middle.addWidget(self.seizuredataformscroll)

            self.openseizuredata()

        
        if (selection == "Seizure Ranking"):
            self.closeallfroms()
            self.removeallforms()

            self.seizurerankingbox = QGroupBox()
            self.seizurerankingbox.setLayout(self.graphinputformseizureranking)
            
            self.seizurerankingformscroll = QScrollArea()
            self.seizurerankingformscroll.setWidget(self.seizurerankingbox)
            self.seizurerankingformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.seizurerankingformscroll)
            
            self.openseizureranking()


        if (selection == "Urine Kt SG"):
            self.closeallfroms()
            self.removeallforms()

            self.urineKtSGbox = QGroupBox()
            self.urineKtSGbox.setLayout(self.graphinputformurinektsg)
            
            self.urineKtSGformscroll = QScrollArea()
            self.urineKtSGformscroll.setWidget(self.urineKtSGbox)
            self.urineKtSGformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.urineKtSGformscroll) 

            self.openurinektsg()
        
        if (selection == "Vitals"):
            
            self.closeallfroms()
            self.removeallforms()

            self.vitalsbox = QGroupBox()
            self.vitalsbox.setLayout(self.graphinputformvitals)
        
            self.vitalsformscroll = QScrollArea()
            self.vitalsformscroll.setWidget(self.vitalsbox)
            self.vitalsformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.vitalsformscroll) 

            self.openvitals()
        
        if (selection == "VNS"):
            
            self.closeallfroms()
            self.removeallforms()

            self.vnsbox = QGroupBox()
            self.vnsbox.setLayout(self.graphinputformvns)
            
            self.vnsformscroll = QScrollArea()
            self.vnsformscroll.setWidget(self.vnsbox)
            self.vnsformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.vnsformscroll) 

            self.openvns()

        if (selection == ""):
            self.closeallfroms()
            self.removeallforms()               

    def updateStateCombo(self, index):
            indx = self.model.index(index, 0, self.AnthropometricsPAF.rootModelIndex())
            self.AnthropometricsPAF2.setRootModelIndex(indx)
            self.AnthropometricsPAF2.setCurrentIndex(0)

    def loadpatients(self):
        self.allpatients = getAllPatients()
        
        i = 0
        j = 0
        self.allpatientbuttons = []
        self.allpatientbuttons.clear()

        for patient in self.allpatients:
            self.patientbtn = QPushButton("Patient ID: " + patient)
            self.middlegrid.addWidget(self.patientbtn,i,j)
            self.patientbtn.clicked.connect(self.openprofile)

            
            self.allpatientbuttons.append(self.patientbtn)

            j+=1

            if(j%5 == 0):
                i+=1
                j=0


    
    def loadgraphnames(self):
        newlist = getPatientGraphs(self.currentpatient)
        temp = []
        temp.clear()
        # temp.extend(newlist)

        graphnames = ["Alertness","Anthropometrics", "Clinic GI Issues","Clinical Labs","Daily Intake",
        "Diet RX","Med Data","Menus","Other Med","Seizure Data","Seizure Ranking","Urine Kt SG","Vitals","VNS"]
        
        for string in newlist:
            for name in graphnames:
                if name in string:
                        temp.append(name) 


        self.graphlist.clear()
        self.graphlist.addItems(temp)
        
        

    def closedashboard(self):
        self.currentpatienttext.close()
        self.middlescrollarea.close()

    def opendashboard(self):
        self.currentpatienttext.show()
        self.middlescrollarea.show()

    def openprofile(self):
      
        self.currentpatient = self.sender().text()[12:]      
        self.currentpatienttext.setText("Selected Patient: " + self.currentpatient) 

        self.patientname.setText(self.currentpatient)

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

        self.addpatientbutton.show()

######################## Closing ##########################
    def closenewpatient(self):
        self.newtip.close()
        self.namelabel.close()
        self.nameinput.close()
        self.addpatientbutton.close()

    def closeallfroms(self):
        self.closealertness()
        self.closeanthropometrics()
        self.closeclinicgi()
        self.closeclinicallabs()
        self.closedailyintake()
        self.closedietrx()
        self.closemenus()
        self.closeothermed()
        self.closeseizuredata()
        self.closeseizureranking()
        self.closeurinektsg()
        self.closevitals()
        self.closevns()
        

        self.alertnessbox.close()
        self.alertnessformscroll.close()

        self.anthropometricsbox.close()
        self.anthropometricsformscroll.close()   

        self.clinicGIbox.close()
        self.clinicGIformscroll.close() 
        
        self.clinicallabsbox.close()
        self.clinicallabsformscroll.close()

        self.dailyIntakebox.close()
        self.dailyIntakeformscroll.close()

        self.dietrxbox.close()
        self.dietrxformscroll.close()

        self.meddatabox.close()
        self.meddataformscroll.close()

        self.menusbox.close()
        self.menusformscroll.close()

        self.othermedbox.close()
        self.othermedformscroll.close()

        self.seizuredatabox.close()
        self.seizuredataformscroll.close()

        self.seizurerankingbox.close()
        self.seizurerankingformscroll.close()

        self.urineKtSGbox.close()
        self.urineKtSGformscroll.close()

        self.vitalsbox.close()
        self.vitalsformscroll.close()

        self.vnsbox.close()
        self.vnsformscroll.close()


    def removeallforms(self):
        self.middle.removeWidget(self.alertnessformscroll)

        self.middle.removeWidget(self.anthropometricsformscroll)

        self.middle.removeWidget(self.clinicGIformscroll)

        self.middle.removeWidget(self.clinicallabsformscroll)
        
        self.middle.removeWidget(self.dailyIntakeformscroll)

        self.middle.removeWidget(self.dietrxformscroll)

        self.middle.removeWidget(self.meddataformscroll)

        self.middle.removeWidget(self.menusformscroll)

        self.middle.removeWidget(self.vitalsformscroll)

        self.middle.removeWidget(self.vnsformscroll)



    def closealertness(self):
        self.AlertnessMRNumberL.close()
        self.AlertnessMRNumberF.close()
        self.AlertnessDateL.close()
        self.AlertnessDateF.close()
        self.AlertnessDayTypeL.close()
        self.AlertnessDayTypeF.close()
        self.AlertnessL.close()
        self.AlertnessF.close()
        self.AlertnessActivityL.close()
        self.AlertnessActivityF.close()
        self.AlertnessDevelopmentL.close()
        self.AlertnessDevelopmentF.close()
        self.AlertnessEnteredL.close()
        self.AlertnessEnteredF.close()
        self.AlertnessCommentsL.close()
        self.AlertnessCommentsF.close()
        self.AlertnessSaveButton.close()

    def closeanthropometrics(self):
        self.selectgraph.close()
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
        self.AnthropometricsPAF2.close()
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
        self.AnthropometricsEnteredL.close()
        self.AnthropometricsEnteredF.close()
        self.AnthropometricsCommentsL.close()
        self.AnthropometricsCommentsF.close()
        self.AnthropometricsSaveButton.close()

    def closeclinicgi(self):
        self.ClinicGIMRNumberL.close()
        self.ClinicGIMRNumberF.close()   
        self.ClinicGIDateL.close()
        self.ClinicGIDateF.close()
        self.ClinicGIDayTypeL.close()
        self.ClinicGIDayTypeF.close()
        self.ClinicGIConstL.close()
        self.ClinicGIConstF.close()
        self.ClinicGIDiaL.close()
        self.ClinicGIDiaF.close()
        self.ClinicGIVomL.close()
        self.ClinicGIVomF.close()
        self.ClinicGINauseaL.close()
        self.ClinicGINauseaF.close()
        self.ClinicGIGagL.close()
        self.ClinicGIGagF.close()
        self.ClinicGINissenL.close()
        self.ClinicGINissenF.close()
        self.ClinicGIConstDesL.close()
        self.ClinicGIConstDesF.close()
        self.ClinicGIDiaDesL.close()
        self.ClinicGIDiaDesF.close()
        self.ClinicGIVomDesL.close()
        self.ClinicGIVomDesF.close()
        self.ClinicGINauseaDesL.close()
        self.ClinicGINauseaDesF.close()
        self.ClinicGIGagDesL.close()
        self.ClinicGIGagDesF.close()
        self.ClinicGIEnteredL.close()
        self.ClinicGIEnteredF.close()
        self.ClinicGICommentsL.close()
        self.ClinicGICommentsF.close()
        self.ClinicGISaveButton.close()

    def closeclinicallabs(self):
        self.ClinicalLabsMRNumberL.close()
        self.ClinicalLabsMRNumberF.close()
        self.ClinicalLabsDateL.close()    
        self.ClinicalLabsDateF.close()    
        self.ClinicalLabsTimeL.close()    
        self.ClinicalLabsTimeF.close()    
        self.ClinicalLabsDayTypeL.close() 
        self.ClinicalLabsDayTypeF.close() 
        self.ClinicalLabsSourceL.close()
        self.ClinicalLabsSourceF.close()
        self.ClinicalLabsFastingL.close()
        self.ClinicalLabsFastingF.close()
        self.ClinicalLabsTGBloodL.close()
        self.ClinicalLabsTGBloodF.close()
        self.ClinicalLabsHDLBloodL.close()
        self.ClinicalLabsHDLBloodF.close()
        self.ClinicalLabsLDLBloodL.close()
        self.ClinicalLabsLDLBloodF.close()
        self.ClinicalLabsTCBloodL.close()
        self.ClinicalLabsTCBloodF.close()
        self.ClinicalLabsNABloodL.close()
        self.ClinicalLabsNABloodF.close()
        self.ClinicalLabsKBloodL.close()
        self.ClinicalLabsKBloodF.close()
        self.ClinicalLabsChlBloodL.close()
        self.ClinicalLabsChlBloodF.close()
        self.ClinicalLabsCO2BloodL.close()
        self.ClinicalLabsCO2BloodF.close()
        self.ClinicalLabsBUNBloodL.close()
        self.ClinicalLabsBUNBloodF.close()
        self.ClinicalLabsCrBloodL.close()
        self.ClinicalLabsCrBloodF.close()
        self.ClinicalLabsGlusBloodL.close()
        self.ClinicalLabsGlusBloodF.close()
        self.ClinicalLabsCaBloodL.close()
        self.ClinicalLabsCaBloodF.close()
        self.ClinicalLabsMagBloodL.close()
        self.ClinicalLabsMagBloodF.close()
        self.ClinicalLabsPhosBloodL.close()
        self.ClinicalLabsPhosBloodF.close()
        self.ClinicalLabsUricAcidBloodL.close()
        self.ClinicalLabsUricAcidBloodF.close()
        self.ClinicalLabsProBloodL.close()
        self.ClinicalLabsProBloodF.close()
        self.ClinicalLabsAlbBloodL.close()
        self.ClinicalLabsAlbBloodF.close()
        self.ClinicalLabsTBilBloodL.close()
        self.ClinicalLabsTBilBloodF.close()
        self.ClinicalLabsTotalBilirubinBloodL.close()
        self.ClinicalLabsTotalBilirubinBloodF.close()
        self.ClinicalLabsAstBloodL.close()
        self.ClinicalLabsAstBloodF.close()
        self.ClinicalLabsAltBloodL.close()
        self.ClinicalLabsAltBloodF.close()
        self.ClinicalLabsRBCBloodL.close()
        self.ClinicalLabsRBCBloodF.close()
        self.ClinicalLabsHgbBloodL.close()
        self.ClinicalLabsHgbBloodF.close()
        self.ClinicalLabsHctBloodL.close()
        self.ClinicalLabsHctBloodF.close()
        self.ClinicalLabsPlateletBloodL.close()
        self.ClinicalLabsPlateletBloodF.close()
        self.ClinicalLabsMCVBloodL.close()
        self.ClinicalLabsMCVBloodF.close()
        self.ClinicalLabsMCHBloodL.close()
        self.ClinicalLabsMCHBloodF.close()
        self.ClinicalLabsMCHCBloodL.close()
        self.ClinicalLabsMCHCBloodF.close()
        self.ClinicalLabsMPVBloodL.close()
        self.ClinicalLabsMPVBloodF.close()
        self.ClinicalLabsRDWBloodL.close()
        self.ClinicalLabsRDWBloodF.close()
        self.ClinicalLabsWBCBloodL.close()
        self.ClinicalLabsWBCBloodF.close()
        self.ClinicalLabsAmmoniaBloodL.close()
        self.ClinicalLabsAmmoniaBloodF.close()
        self.ClinicalLabsBHbBloodL.close()
        self.ClinicalLabsBHbBloodF.close()
        self.ClinicalLabsAcacBloodL.close()
        self.ClinicalLabsAcacBloodF.close()
        self.ClinicalLabsNeutrophilsBloodL.close()
        self.ClinicalLabsNeutrophilsBloodF.close()
        self.ClinicalLabsLymphocytesBloodL.close()
        self.ClinicalLabsLymphocytesBloodF.close()
        self.ClinicalLabsMonocytesBloodL.close()
        self.ClinicalLabsMonocytesBloodF.close()
        self.ClinicalLabsEosinophilsBloodL.close()
        self.ClinicalLabsEosinophilsBloodF.close()
        self.ClinicalLabsBasophilsBloodL.close()
        self.ClinicalLabsBasophilsBloodF.close()
        self.ClinicalLabsLargeUnstainedCellsBloodL.close()
        self.ClinicalLabsLargeUnstainedCellsBloodF.close()
        self.ClinicalLabsNeutrophilsAbsoluteBloodL.close()
        self.ClinicalLabsNeutrophilsAbsoluteBloodF.close()
        self.ClinicalLabsLymphocytesAbsoluteBloodL.close()
        self.ClinicalLabsLymphocytesAbsoluteBloodF.close()
        self.ClinicalLabsEosinophilsAbsoluteBloodL.close()
        self.ClinicalLabsEosinophilsAbsoluteBloodF.close()
        self.ClinicalLabsBasophilsAbsoluteBloodL.close()
        self.ClinicalLabsBasophilsAbsoluteBloodF.close()
        self.ClinicalLabsGlusBloodCRCL.close()
        self.ClinicalLabsGlusBloodCRCF.close()
        self.ClinicalLabsLactBloodCRCMmolL.close()
        self.ClinicalLabsLactBloodCRCMmolF.close()
        self.ClinicalLabsLabBlood1L.close()
        self.ClinicalLabsLabBlood1F.close()
        self.ClinicalLabsLabBlood2L.close()
        self.ClinicalLabsLabBlood2F.close()
        self.ClinicalLabsLabBlood3L.close()
        self.ClinicalLabsLabBlood3F.close()
        self.ClinicalLabsLabBlood4L.close()
        self.ClinicalLabsLabBlood4F.close()
        self.ClinicalLabsLabBlood5L.close()
        self.ClinicalLabsLabBlood5F.close()
        self.ClinicalLabsLabBlood6L.close()
        self.ClinicalLabsLabBlood6F.close()
        self.ClinicalLabsLabBlood7L.close()
        self.ClinicalLabsLabBlood7F.close()
        self.ClinicalLabsLabBlood8L.close()
        self.ClinicalLabsLabBlood8F.close()
        self.ClinicalLabsLabBlood9L.close()
        self.ClinicalLabsLabBlood9F.close()
        self.ClinicalLabsLabBlood10L.close()
        self.ClinicalLabsLabBlood10F.close()
        self.ClinicalLabsLabBlood11L.close()
        self.ClinicalLabsLabBlood11F.close()
        self.ClinicalLabsLabBlood12L.close()
        self.ClinicalLabsLabBlood12F.close()
        self.ClinicalLabsLabBlood13L.close()
        self.ClinicalLabsLabBlood13F.close()
        self.ClinicalLabsLabBlood14L.close()
        self.ClinicalLabsLabBlood14F.close()
        self.ClinicalLabsLabBlood15L.close()
        self.ClinicalLabsLabBlood15F.close()
        self.ClinicalLabsLabBlood16L.close()
        self.ClinicalLabsLabBlood16F.close()
        self.ClinicalLabsLabBlood17L.close()
        self.ClinicalLabsLabBlood17F.close()
        self.ClinicalLabsLabBlood18L.close()
        self.ClinicalLabsLabBlood18F.close()
        self.ClinicalLabsLabBlood19L.close()
        self.ClinicalLabsLabBlood19F.close()
        self.ClinicalLabsLabBlood20L.close()
        self.ClinicalLabsLabBlood20F.close()
        self.ClinicalLabsLabBlood21L.close()
        self.ClinicalLabsLabBlood21F.close()
        self.ClinicalLabsLabBlood22L.close()
        self.ClinicalLabsLabBlood22F.close()
        self.ClinicalLabsLabBlood23L.close()
        self.ClinicalLabsLabBlood23F.close()
        self.ClinicalLabsLabBlood24L.close()
        self.ClinicalLabsLabBlood24F.close()
        self.ClinicalLabsLabBlood25L.close()
        self.ClinicalLabsLabBlood25F.close()
        self.ClinicalLabsLabBlood26L.close()
        self.ClinicalLabsLabBlood26F.close()
        self.ClinicalLabsLabBlood27L.close()
        self.ClinicalLabsLabBlood27F.close()
        self.ClinicalLabsLabBlood28L.close()
        self.ClinicalLabsLabBlood28F.close()
        self.ClinicalLabsLabBlood29L.close()
        self.ClinicalLabsLabBlood29F.close()
        self.ClinicalLabsLabBlood30L.close()
        self.ClinicalLabsLabBlood30F.close()
        self.ClinicalLabsLabBlood31L.close()
        self.ClinicalLabsLabBlood31F.close()
        self.ClinicalLabsLabBlood32L.close()
        self.ClinicalLabsLabBlood32F.close()
        self.ClinicalLabsLabBlood33L.close()
        self.ClinicalLabsLabBlood33F.close()
        self.ClinicalLabsLabBlood34L.close()
        self.ClinicalLabsLabBlood34F.close()
        self.ClinicalLabsLabBlood35L.close()
        self.ClinicalLabsLabBlood35F.close()
        self.ClinicalLabsLabBlood36L.close()
        self.ClinicalLabsLabBlood36F.close()
        self.ClinicalLabsLabBlood37L.close()
        self.ClinicalLabsLabBlood37F.close()
        self.ClinicalLabsLabBlood38L.close()
        self.ClinicalLabsLabBlood38F.close()
        self.ClinicalLabsLabBlood39L.close()
        self.ClinicalLabsLabBlood39F.close()
        self.ClinicalLabsLabBlood40L.close()
        self.ClinicalLabsLabBlood40F.close()
        self.ClinicalLabsLabBlood41L.close()
        self.ClinicalLabsLabBlood41F.close()
        self.ClinicalLabsLabBlood42L.close()
        self.ClinicalLabsLabBlood42F.close()
        self.ClinicalLabsLabBlood43L.close()
        self.ClinicalLabsLabBlood43F.close()
        self.ClinicalLabsLabBlood44L.close()
        self.ClinicalLabsLabBlood44F.close()
        self.ClinicalLabsLabBlood45L.close()
        self.ClinicalLabsLabBlood45F.close()
        self.ClinicalLabsLabBlood46L.close()
        self.ClinicalLabsLabBlood46F.close()
        self.ClinicalLabsLabBlood47L.close()
        self.ClinicalLabsLabBlood47F.close()
        self.ClinicalLabsLabBlood48L.close()
        self.ClinicalLabsLabBlood48F.close()
        self.ClinicalLabsLabBlood49L.close()
        self.ClinicalLabsLabBlood49F.close()
        self.ClinicalLabsLabBlood50L.close()
        self.ClinicalLabsLabBlood50F.close()
        self.ClinicalLabsEnteredL.close()
        self.ClinicalLabsEnteredF.close()
        self.ClinicalLabsCommentsL.close()
        self.ClinicalLabsCommentsF.close()
        self.ClinicalLabsSaveButton.close()

    def closedailyintake(self):
        self.DailyIntakeMRNumberL.close()
        self.DailyIntakeMRNumberF.close()
        self.DailyIntakeDateL.close()
        self.DailyIntakeDateF.close()
        self.DailyIntakeDayTypeL.close()
        self.DailyIntakeDayTypeF.close()
        self.DailyIntakePKTNUML.close()
        self.DailyIntakePKTNUMF.close()
        self.DailyIntakeDataQualityDietL.close()
        self.DailyIntakeDataQualityDietF.close()
        self.DailyIntakeDayQualityDietL.close()
        self.DailyIntakeDayQualityDietF.close()
        self.DailyIntakeEnteredL.close()
        self.DailyIntakeEnteredF.close()
        self.DailyIntakeCommentsL.close()
        self.DailyIntakeCommentsF.close()
        self.DailyIntakeSaveButton.close()

    def closedietrx(self):
        self.DietRXMRNumberL.close()
        self.DietRXMRNumberF.close()
        self.DietRXDateL.close()
        self.DietRXDateF.close()
        self.DietRXDayTypeL.close()
        self.DietRXDayTypeF.close()
        self.DietRXROFL.close()
        self.DietRXROFF.close()
        self.DietRXRFCDL.close()
        self.DietRXRFCDF.close()
        self.DietRXSnackCalL.close()
        self.DietRXSnackCalF.close()
        self.DietRXSnackRatioL.close()
        self.DietRXSnackRatioF.close()
        self.DietRXSnackNumberL.close()
        self.DietRXSnackNumberF.close()
        self.DietRXMealNumberL.close()
        self.DietRXMealNumberF.close()
        self.DietRXMealRatioL.close()
        self.DietRXMealRatioF.close()
        self.DietRXCalL.close()
        self.DietRXCalF.close()
        self.DietRXProL.close()
        self.DietRXProF.close()
        self.DietRXEnteredL.close()
        self.DietRXEnteredF.close()
        self.DietRXCommentsL.close()
        self.DietRXCommentsF.close()
        self.DietRXSaveButton.close()

    def closemeddata(self):
        self.MedDataMRNumberL.show()
        self.MedDataMRNumberF.show()
        self.MedDataDateL.show()
        self.MedDataDateF.show()
        self.MedDataDayTypeL.show()
        self.MedDataDayTypeF.show()
        self.MedDataNDIDL.show()
        self.MedDataNDIDF.show()
        self.MedDataMedIDL.show()
        self.MedDataMedIDF.show()
        self.MedDataRFCML.show()
        self.MedDataRFCMF.show()
        self.MedDataProdNameL.show()
        self.MedDataProdNameF.show()
        self.MedDataDailyDoseL.show()
        self.MedDataDailyDoseF.show()
        self.MedDataMedDosesL.show()
        self.MedDataMedDosesF.show()
        self.MedDataMedCommentsL.show()
        self.MedDataMedCommentsF.show()
        self.MedDataEnteredL.show()
        self.MedDataEnteredF.show()
        self.MedDataCommentsL.show()
        self.MedDataCommentsF.show()
        self.MedDataSaveButton.show()

    def closemenus(self):
        self.MenusMRNumberL.close()
        self.MenusMRNumberF.close()
        self.MenusDateL.close()
        self.MenusDateF.close()
        self.MenusCalPrcntL.close()
        self.MenusCalPrcntF.close()
        self.MenusProcntPrcntL.close()
        self.MenusProcntPrcntF.close()
        self.MenusRatioPrL .close()
        self.MenusRatioPrF.close()
        self.MenusRatioPrL.close()
        self.MenusRatioPrF.close()
        self.MenusMealNumberL.close()
        self.MenusMealNumberF.close()
        self.MenusSnackNumberL.close()
        self.MenusSnackNumberF.close()
        self.MenusRecipeNameL.close() 
        self.MenusRecipeNameF.close()
        self.MenusRecipeNumberL.close()
        self.MenusRecipeNumberF.close()
        self.MenusRecipeIngredientAmountL.close()
        self.MenusRecipeIngredientAmountF.close()
        self.MenusNDIDL.close()
        self.MenusNDIDF.close()
        self.MenusProdNameL.close()
        self.MenusProdNameF.close()
        self.MenusRecipeTypeL.close() 
        self.MenusRecipeTypeF.close()
        self.MenusEnteredL.close() 
        self.MenusEnteredF.close()
        self.MenusCommentsL.close()
        self.MenusCommentsF.close() 
        self.MenusSaveButton.close()

    def closeothermed(self):
        self.OtherMedMRNumberL.close()
        self.OtherMedMRNumberF.close()
        self.OtherMedDateL.close()
        self.OtherMedDateF.close()
        self.OtherMedNDIDL.close()
        self.OtherMedNDIDF.close()
        self.OtherMedProdNameL.close()
        self.OtherMedProdNameF.close()
        self.OtherMedMedAmountL.close()
        self.OtherMedMedAmountF.close()
        self.OtherMedMedUnitL.close()
        self.OtherMedMedUnitF.close()
        self.OtherMedEnteredL.close()
        self.OtherMedEnteredF.close()
        self.OtherMedCommentsL.close()
        self.OtherMedCommentsF.close()
        self.OtherMedSaveButton.close()  

    def closeseizuredata(self):
        self.SeizureDataMRNumberL.close()
        self.SeizureDataMRNumberF.close()
        self.SeizureDataDateL.close()
        self.SeizureDataDateF.close()
        self.SeizureDataDayTypeL.close()
        self.SeizureDataDayTypeF.close()
        self.SeizureDataDataQualityL.close()
        self.SeizureDataDataQualityF.close()
        self.SeizureDataSeizureSeverityL.close()
        self.SeizureDataSeizureSeverityF.close()
        self.SeizureDataSeizureLengthL.close()
        self.SeizureDataSeizureLengthF.close()
        self.SeizureDataSeizureTypeL.close()
        self.SeizureDataSeizureTypeF.close()
        self.SeizureDataSeizureVariableL.close()
        self.SeizureDataSeizureVariableF.close()
        self.SeizureDataSeizureNumberL.close()
        self.SeizureDataSeizureNumberF.close()
        self.SeizureDataSeizureClusterL.close()
        self.SeizureDataSeizureClusterF.close()
        self.SeizureDataEnteredL.close()
        self.SeizureDataEnteredF.close()
        self.SeizureDataCommentsL.close()
        self.SeizureDataCommentsF.close()
        self.SeizureDataSaveButton.close()

    def closeseizureranking(self):
        self.SeizureRankingMRNumberL.close()
        self.SeizureRankingMRNumberF.close()
        self.SeizureRankingSeizureParameterL.close()
        self.SeizureRankingSeizureParameterF.close()
        self.SeizureRankingSeizureEntryL.close()
        self.SeizureRankingSeizureEntryF.close()
        self.SeizureRankingSeizureRankingL.close()
        self.SeizureRankingSeizureRankingF.close()
        self.SeizureRankingEnteredL.close()
        self.SeizureRankingEnteredF.close()
        self.SeizureRankingCommentsL.close()
        self.SeizureRankingCommentsF.close()
        self.SeizureRankingSaveButton.close()

    def closeurinektsg(self):
        self.UrineKtSGMRNumberL.close()
        self.UrineKtSGMRNumberF.close()
        self.UrineKtSGDateL.close()
        self.UrineKtSGDateF.close()
        self.UrineKtSGDayTypeL.close()
        self.UrineKtSGDayTypeF.close()
        self.UrineKtSGUrineKtL.close()
        self.UrineKtSGUrineKtF.close()
        self.UrineKtSGUrineSGL.close()
        self.UrineKtSGUrineSGF.close()
        self.UrineKtSGEnteredL.close()
        self.UrineKtSGEnteredF.close()
        self.UrineKtSGCommentsL.close()
        self.UrineKtSGCommentsF.close()
        self.UrineKtSGSaveButton.close()

    def closevitals(self):
        self.VitalsMRNumberL.close()
        self.VitalsMRNumberF.close()
        self.VitalsDateL.close()
        self.VitalsDateF.close()
        self.VitalsDayTypeL.close()
        self.VitalsDayTypeF.close()
        self.VitalsSourceL.close()
        self.VitalsSourceF.close()
        self.VitalsBPSysL.close()
        self.VitalsBPSysF.close()
        self.VitalsBPDiaL.close()
        self.VitalsBPDiaF.close()
        self.VitalsTempL.close()
        self.VitalsTempF.close()
        self.VitalsRRL.close()
        self.VitalsRRF.close()
        self.VitalsHRL.close()
        self.VitalsHRF.close()
        self.VitalsEnteredL.close()
        self.VitalsEnteredF.close()
        self.VitalsCommentsL.close()
        self.VitalsCommentsF.close()
        self.VitalsSaveButton.close()

    def closevns(self):
        self.VNSMRNumberL.close()
        self.VNSMRNumberF.close()
        self.VNSDateL.close()
        self.VNSDateF.close()
        self.VNSDayTypeL.close()
        self.VNSDayTypeF.close()
        self.VNSMRMagActL.close()
        self.VNSMRMagActF.close()
        self.VNSOutputCurrL.close()
        self.VNSOutputCurrF.close()
        self.VNSVNSFrequencyL.close()
        self.VNSVNSFrequencyF.close()
        self.VNSPulseWidthL.close()
        self.VNSPulseWidthF.close()
        self.VNSSignalOnL.close()
        self.VNSSignalOnF.close()
        self.VNSSignalOffL.close()
        self.VNSSignalOffF.close()
        self.VNSMagnetCurrentL.close()
        self.VNSMagnetCurrentF.close()
        self.VNSMagnetOnL.close()
        self.VNSMagnetOnF.close()
        self.VNSMagnetPulseL.close()
        self.VNSMagnetPulseF.close()
        self.VNSLeadTestL.close()
        self.VNSLeadTestF.close()
        self.VNSEnteredL.close()
        self.VNSEnteredF.close()
        self.VNSCommentsL.close()
        self.VNSCommentsF.close()
        self.VNSSaveButton.close()
    

#################
    def openalertness(self):
        self.AlertnessMRNumberL.show()
        self.AlertnessMRNumberF.show()
        self.AlertnessDateL.show()
        self.AlertnessDateF.show()
        self.AlertnessDayTypeL.show()
        self.AlertnessDayTypeF.show()
        self.AlertnessL.show()
        self.AlertnessF.show()
        self.AlertnessActivityL.show()
        self.AlertnessActivityF.show()
        self.AlertnessDevelopmentL.show()
        self.AlertnessDevelopmentF.show()
        self.AlertnessEnteredL.show()
        self.AlertnessEnteredF.show()
        self.AlertnessCommentsL.show()
        self.AlertnessCommentsF.show()
        self.AlertnessSaveButton.show()

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
        self.AnthropometricsPAF2.show()
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

    def openclinicgi(self):
        self.ClinicGIMRNumberL.show()
        self.ClinicGIMRNumberF.show()   
        self.ClinicGIDateL.show()
        self.ClinicGIDateF.show()
        self.ClinicGIDayTypeL.show()
        self.ClinicGIDayTypeF.show()
        self.ClinicGIConstL.show()
        self.ClinicGIConstF.show()
        self.ClinicGIDiaL.show()
        self.ClinicGIDiaF.show()
        self.ClinicGIVomL.show()
        self.ClinicGIVomF.show()
        self.ClinicGINauseaL.show()
        self.ClinicGINauseaF.show()
        self.ClinicGIGagL.show()
        self.ClinicGIGagF.show()
        self.ClinicGINissenL.show()
        self.ClinicGINissenF.show()
        self.ClinicGIConstDesL.show()
        self.ClinicGIConstDesF.show()
        self.ClinicGIDiaDesL.show()
        self.ClinicGIDiaDesF.show()
        self.ClinicGIVomDesL.show()
        self.ClinicGIVomDesF.show()
        self.ClinicGINauseaDesL.show()
        self.ClinicGINauseaDesF.show()
        self.ClinicGIGagDesL.show()
        self.ClinicGIGagDesF.show()
        self.ClinicGIEnteredL.show()
        self.ClinicGIEnteredF.show()
        self.ClinicGICommentsL.show()
        self.ClinicGICommentsF.show()
        self.ClinicGISaveButton.show()

    def openclinicallabs(self):
        self.ClinicalLabsMRNumberL.show()
        self.ClinicalLabsMRNumberF.show()
        self.ClinicalLabsDateL.show()
        self.ClinicalLabsDateF.show()
        self.ClinicalLabsTimeL.show()
        self.ClinicalLabsTimeF.show()
        self.ClinicalLabsDayTypeL.show()
        self.ClinicalLabsDayTypeF.show()
        self.ClinicalLabsSourceL.show()
        self.ClinicalLabsSourceF.show()
        self.ClinicalLabsFastingL.show()
        self.ClinicalLabsFastingF.show()
        self.ClinicalLabsTGBloodL.show()
        self.ClinicalLabsTGBloodF.show()
        self.ClinicalLabsHDLBloodL.show()
        self.ClinicalLabsHDLBloodF.show()
        self.ClinicalLabsLDLBloodL.show()
        self.ClinicalLabsLDLBloodF.show()
        self.ClinicalLabsTCBloodL.show()
        self.ClinicalLabsTCBloodF.show()
        self.ClinicalLabsNABloodL.show()
        self.ClinicalLabsNABloodF.show()
        self.ClinicalLabsKBloodL.show()
        self.ClinicalLabsKBloodF.show()
        self.ClinicalLabsChlBloodL.show()
        self.ClinicalLabsChlBloodF.show()
        self.ClinicalLabsCO2BloodL.show()
        self.ClinicalLabsCO2BloodF.show()
        self.ClinicalLabsBUNBloodL.show()
        self.ClinicalLabsBUNBloodF.show()
        self.ClinicalLabsCrBloodL.show()
        self.ClinicalLabsCrBloodF.show()
        self.ClinicalLabsGlusBloodL.show()
        self.ClinicalLabsGlusBloodF.show()
        self.ClinicalLabsCaBloodL.show()
        self.ClinicalLabsCaBloodF.show()
        self.ClinicalLabsMagBloodL.show()
        self.ClinicalLabsMagBloodF.show()
        self.ClinicalLabsPhosBloodL.show()
        self.ClinicalLabsPhosBloodF.show()
        self.ClinicalLabsUricAcidBloodL.show()
        self.ClinicalLabsUricAcidBloodF.show()
        self.ClinicalLabsProBloodL.show()
        self.ClinicalLabsProBloodF.show()
        self.ClinicalLabsAlbBloodL.show()
        self.ClinicalLabsAlbBloodF.show()
        self.ClinicalLabsTBilBloodL.show()
        self.ClinicalLabsTBilBloodF.show()
        self.ClinicalLabsTotalBilirubinBloodL.show()
        self.ClinicalLabsTotalBilirubinBloodF.show()
        self.ClinicalLabsAstBloodL.show()
        self.ClinicalLabsAstBloodF.show()
        self.ClinicalLabsAltBloodL.show()
        self.ClinicalLabsAltBloodF.show()
        self.ClinicalLabsRBCBloodL.show()
        self.ClinicalLabsRBCBloodF.show()
        self.ClinicalLabsHgbBloodL.show()
        self.ClinicalLabsHgbBloodF.show()
        self.ClinicalLabsHctBloodL.show()
        self.ClinicalLabsHctBloodF.show()
        self.ClinicalLabsPlateletBloodL.show()
        self.ClinicalLabsPlateletBloodF.show()
        self.ClinicalLabsMCVBloodL.show()
        self.ClinicalLabsMCVBloodF.show()
        self.ClinicalLabsMCHBloodL.show()
        self.ClinicalLabsMCHBloodF.show()
        self.ClinicalLabsMCHCBloodL.show()
        self.ClinicalLabsMCHCBloodF.show()
        self.ClinicalLabsMPVBloodL.show()
        self.ClinicalLabsMPVBloodF.show()
        self.ClinicalLabsRDWBloodL.show()
        self.ClinicalLabsRDWBloodF.show()
        self.ClinicalLabsWBCBloodL.show()
        self.ClinicalLabsWBCBloodF.show()
        self.ClinicalLabsAmmoniaBloodL.show()
        self.ClinicalLabsAmmoniaBloodF.show()
        self.ClinicalLabsBHbBloodL.show()
        self.ClinicalLabsBHbBloodF.show()
        self.ClinicalLabsAcacBloodL.show()
        self.ClinicalLabsAcacBloodF.show()
        self.ClinicalLabsNeutrophilsBloodL.show()
        self.ClinicalLabsNeutrophilsBloodF.show()
        self.ClinicalLabsLymphocytesBloodL.show()
        self.ClinicalLabsLymphocytesBloodF.show()
        self.ClinicalLabsMonocytesBloodL.show()
        self.ClinicalLabsMonocytesBloodF.show()
        self.ClinicalLabsEosinophilsBloodL.show()
        self.ClinicalLabsEosinophilsBloodF.show()
        self.ClinicalLabsBasophilsBloodL.show()
        self.ClinicalLabsBasophilsBloodF.show()
        self.ClinicalLabsLargeUnstainedCellsBloodL.show()
        self.ClinicalLabsLargeUnstainedCellsBloodF.show()
        self.ClinicalLabsNeutrophilsAbsoluteBloodL.show()
        self.ClinicalLabsNeutrophilsAbsoluteBloodF.show()
        self.ClinicalLabsLymphocytesAbsoluteBloodL.show()
        self.ClinicalLabsLymphocytesAbsoluteBloodF.show()
        self.ClinicalLabsEosinophilsAbsoluteBloodL.show()
        self.ClinicalLabsEosinophilsAbsoluteBloodF.show()
        self.ClinicalLabsBasophilsAbsoluteBloodL.show()
        self.ClinicalLabsBasophilsAbsoluteBloodF.show()
        self.ClinicalLabsGlusBloodCRCL.show()
        self.ClinicalLabsGlusBloodCRCF.show()
        self.ClinicalLabsLactBloodCRCMmolL.show()
        self.ClinicalLabsLactBloodCRCMmolF.show()
        self.ClinicalLabsLabBlood1L.show()
        self.ClinicalLabsLabBlood1F.show()
        self.ClinicalLabsLabBlood2L.show()
        self.ClinicalLabsLabBlood2F.show()
        self.ClinicalLabsLabBlood3L.show()
        self.ClinicalLabsLabBlood3F.show()
        self.ClinicalLabsLabBlood4L.show()
        self.ClinicalLabsLabBlood4F.show()
        self.ClinicalLabsLabBlood5L.show()
        self.ClinicalLabsLabBlood5F.show()
        self.ClinicalLabsLabBlood6L.show()
        self.ClinicalLabsLabBlood6F.show()
        self.ClinicalLabsLabBlood7L.show()
        self.ClinicalLabsLabBlood7F.show()
        self.ClinicalLabsLabBlood8L.show()
        self.ClinicalLabsLabBlood8F.show()
        self.ClinicalLabsLabBlood9L.show()
        self.ClinicalLabsLabBlood9F.show()
        self.ClinicalLabsLabBlood10L.show()
        self.ClinicalLabsLabBlood10F.show()
        self.ClinicalLabsLabBlood11L.show()
        self.ClinicalLabsLabBlood11F.show()
        self.ClinicalLabsLabBlood12L.show()
        self.ClinicalLabsLabBlood12F.show()
        self.ClinicalLabsLabBlood13L.show()
        self.ClinicalLabsLabBlood13F.show()
        self.ClinicalLabsLabBlood14L.show()
        self.ClinicalLabsLabBlood14F.show()
        self.ClinicalLabsLabBlood15L.show()
        self.ClinicalLabsLabBlood15F.show()
        self.ClinicalLabsLabBlood16L.show()
        self.ClinicalLabsLabBlood16F.show()
        self.ClinicalLabsLabBlood17L.show()
        self.ClinicalLabsLabBlood17F.show()
        self.ClinicalLabsLabBlood18L.show()
        self.ClinicalLabsLabBlood18F.show()
        self.ClinicalLabsLabBlood19L.show()
        self.ClinicalLabsLabBlood19F.show()
        self.ClinicalLabsLabBlood20L.show()
        self.ClinicalLabsLabBlood20F.show()
        self.ClinicalLabsLabBlood21L.show()
        self.ClinicalLabsLabBlood21F.show()
        self.ClinicalLabsLabBlood22L.show()
        self.ClinicalLabsLabBlood22F.show()
        self.ClinicalLabsLabBlood23L.show()
        self.ClinicalLabsLabBlood23F.show()
        self.ClinicalLabsLabBlood24L.show()
        self.ClinicalLabsLabBlood24F.show()
        self.ClinicalLabsLabBlood25L.show()
        self.ClinicalLabsLabBlood25F.show()
        self.ClinicalLabsLabBlood26L.show()
        self.ClinicalLabsLabBlood26F.show()
        self.ClinicalLabsLabBlood27L.show()
        self.ClinicalLabsLabBlood27F.show()
        self.ClinicalLabsLabBlood28L.show()
        self.ClinicalLabsLabBlood28F.show()
        self.ClinicalLabsLabBlood29L.show()
        self.ClinicalLabsLabBlood29F.show()
        self.ClinicalLabsLabBlood30L.show()
        self.ClinicalLabsLabBlood30F.show()
        self.ClinicalLabsLabBlood31L.show()
        self.ClinicalLabsLabBlood31F.show()
        self.ClinicalLabsLabBlood32L.show()
        self.ClinicalLabsLabBlood32F.show()
        self.ClinicalLabsLabBlood33L.show()
        self.ClinicalLabsLabBlood33F.show()
        self.ClinicalLabsLabBlood34L.show()
        self.ClinicalLabsLabBlood34F.show()
        self.ClinicalLabsLabBlood35L.show()
        self.ClinicalLabsLabBlood35F.show()
        self.ClinicalLabsLabBlood36L.show()
        self.ClinicalLabsLabBlood36F.show()
        self.ClinicalLabsLabBlood37L.show()
        self.ClinicalLabsLabBlood37F.show()
        self.ClinicalLabsLabBlood38L.show()
        self.ClinicalLabsLabBlood38F.show()
        self.ClinicalLabsLabBlood39L.show()
        self.ClinicalLabsLabBlood39F.show()
        self.ClinicalLabsLabBlood40L.show()
        self.ClinicalLabsLabBlood40F.show()
        self.ClinicalLabsLabBlood41L.show()
        self.ClinicalLabsLabBlood41F.show()
        self.ClinicalLabsLabBlood42L.show()
        self.ClinicalLabsLabBlood42F.show()
        self.ClinicalLabsLabBlood43L.show()
        self.ClinicalLabsLabBlood43F.show()
        self.ClinicalLabsLabBlood44L.show()
        self.ClinicalLabsLabBlood44F.show()
        self.ClinicalLabsLabBlood45L.show()
        self.ClinicalLabsLabBlood45F.show()
        self.ClinicalLabsLabBlood46L.show()
        self.ClinicalLabsLabBlood46F.show()
        self.ClinicalLabsLabBlood47L.show()
        self.ClinicalLabsLabBlood47F.show()
        self.ClinicalLabsLabBlood48L.show()
        self.ClinicalLabsLabBlood48F.show()
        self.ClinicalLabsLabBlood49L.show()
        self.ClinicalLabsLabBlood49F.show()
        self.ClinicalLabsLabBlood50L.show()
        self.ClinicalLabsLabBlood50F.show()
        self.ClinicalLabsEnteredL.show()
        self.ClinicalLabsEnteredF.show()
        self.ClinicalLabsCommentsL.show()
        self.ClinicalLabsCommentsF.show()
        self.ClinicalLabsSaveButton.show()

    def opendailyintake(self):
        self.DailyIntakeMRNumberL.show()
        self.DailyIntakeMRNumberF.show()
        self.DailyIntakeDateL.show()
        self.DailyIntakeDateF.show()
        self.DailyIntakeDayTypeL.show()
        self.DailyIntakeDayTypeF.show()
        self.DailyIntakePKTNUML.show()
        self.DailyIntakePKTNUMF.show()
        self.DailyIntakeDataQualityDietL.show()
        self.DailyIntakeDataQualityDietF.show()
        self.DailyIntakeDayQualityDietL.show()
        self.DailyIntakeDayQualityDietF.show()
        self.DailyIntakeEnteredL.show()
        self.DailyIntakeEnteredF.show()
        self.DailyIntakeCommentsL.show()
        self.DailyIntakeCommentsF.show()
        self.DailyIntakeSaveButton.show()

    def opendietrx(self):
        self.DietRXMRNumberL.show()
        self.DietRXMRNumberF.show()
        self.DietRXDateL.show()
        self.DietRXDateF.show()
        self.DietRXDayTypeL.show()
        self.DietRXDayTypeF.show()
        self.DietRXROFL.show()
        self.DietRXROFF.show()
        self.DietRXRFCDL.show()
        self.DietRXRFCDF.show()
        self.DietRXSnackCalL.show()
        self.DietRXSnackCalF.show()
        self.DietRXSnackRatioL.show()
        self.DietRXSnackRatioF.show()
        self.DietRXSnackNumberL.show()
        self.DietRXSnackNumberF.show()
        self.DietRXMealNumberL.show()
        self.DietRXMealNumberF.show()
        self.DietRXMealRatioL.show()
        self.DietRXMealRatioF.show()
        self.DietRXCalL.show()
        self.DietRXCalF.show()
        self.DietRXProL.show()
        self.DietRXProF.show()
        self.DietRXEnteredL.show()
        self.DietRXEnteredF.show()
        self.DietRXCommentsL.show()
        self.DietRXCommentsF.show()
        self.DietRXSaveButton.show()    

    def openmeddata(self):
        self.MedDataMRNumberL.show()
        self.MedDataMRNumberF.show()
        self.MedDataDateL.show()
        self.MedDataDateF.show()
        self.MedDataDayTypeL.show()
        self.MedDataDayTypeF.show()
        self.MedDataNDIDL.show()
        self.MedDataNDIDF.show()
        self.MedDataMedIDL.show()
        self.MedDataMedIDF.show()
        self.MedDataRFCML.show()
        self.MedDataRFCMF.show()
        self.MedDataProdNameL.show()
        self.MedDataProdNameF.show()
        self.MedDataDailyDoseL.show()
        self.MedDataDailyDoseF.show()
        self.MedDataMedDosesL.show()
        self.MedDataMedDosesF.show()
        self.MedDataMedCommentsL.show()
        self.MedDataMedCommentsF.show()
        self.MedDataEnteredL.show()
        self.MedDataEnteredF.show()
        self.MedDataCommentsL.show()
        self.MedDataCommentsF.show()
        self.MedDataSaveButton.show()

    def openmenus(self):
        self.MenusMRNumberL.show()
        self.MenusMRNumberF.show()
        self.MenusDateL.show()
        self.MenusDateF.show()
        self.MenusCalPrcntL.show()
        self.MenusCalPrcntF.show()
        self.MenusProcntPrcntL.show()
        self.MenusProcntPrcntF.show()
        self.MenusRatioPrL .show()
        self.MenusRatioPrF.show()
        self.MenusRatioPrL.show()
        self.MenusRatioPrF.show()
        self.MenusMealNumberL.show()
        self.MenusMealNumberF.show()
        self.MenusSnackNumberL.show()
        self.MenusSnackNumberF.show()
        self.MenusRecipeNameL.show() 
        self.MenusRecipeNameF.show()
        self.MenusRecipeNumberL.show()
        self.MenusRecipeNumberF.show()
        self.MenusRecipeIngredientAmountL.show()
        self.MenusRecipeIngredientAmountF.show()
        self.MenusNDIDL.show()
        self.MenusNDIDF.show()
        self.MenusProdNameL.show()
        self.MenusProdNameF.show()
        self.MenusRecipeTypeL.show() 
        self.MenusRecipeTypeF.show()
        self.MenusEnteredL.show() 
        self.MenusEnteredF.show()
        self.MenusCommentsL.show()
        self.MenusCommentsF.show() 
        self.MenusSaveButton.show() 

    def openothermed(self):
        self.OtherMedMRNumberL.show()
        self.OtherMedMRNumberF.show()
        self.OtherMedDateL.show()
        self.OtherMedDateF.show()
        self.OtherMedNDIDL.show()
        self.OtherMedNDIDF.show()
        self.OtherMedProdNameL.show()
        self.OtherMedProdNameF.show()
        self.OtherMedMedAmountL.show()
        self.OtherMedMedAmountF.show()
        self.OtherMedMedUnitL.show()
        self.OtherMedMedUnitF.show()
        self.OtherMedEnteredL.show()
        self.OtherMedEnteredF.show()
        self.OtherMedCommentsL.show()
        self.OtherMedCommentsF.show()
        self.OtherMedSaveButton.show()

    def openseizuredata(self):
        self.SeizureDataMRNumberL.show()
        self.SeizureDataMRNumberF.show()
        self.SeizureDataDateL.show()
        self.SeizureDataDateF.show()
        self.SeizureDataDayTypeL.show()
        self.SeizureDataDayTypeF.show()
        self.SeizureDataDataQualityL.show()
        self.SeizureDataDataQualityF.show()
        self.SeizureDataSeizureSeverityL.show()
        self.SeizureDataSeizureSeverityF.show()
        self.SeizureDataSeizureLengthL.show()
        self.SeizureDataSeizureLengthF.show()
        self.SeizureDataSeizureTypeL.show()
        self.SeizureDataSeizureTypeF.show()
        self.SeizureDataSeizureVariableL.show()
        self.SeizureDataSeizureVariableF.show()
        self.SeizureDataSeizureNumberL.show()
        self.SeizureDataSeizureNumberF.show()
        self.SeizureDataSeizureClusterL.show()
        self.SeizureDataSeizureClusterF.show()
        self.SeizureDataEnteredL.show()
        self.SeizureDataEnteredF.show()
        self.SeizureDataCommentsL.show()
        self.SeizureDataCommentsF.show()
        self.SeizureDataSaveButton.show() 

    def openseizureranking(self):
        self.SeizureRankingMRNumberL.show()
        self.SeizureRankingMRNumberF.show()
        self.SeizureRankingSeizureParameterL.show()
        self.SeizureRankingSeizureParameterF.show()
        self.SeizureRankingSeizureEntryL.show()
        self.SeizureRankingSeizureEntryF.show()
        self.SeizureRankingSeizureRankingL.show()
        self.SeizureRankingSeizureRankingF.show()
        self.SeizureRankingEnteredL.show()
        self.SeizureRankingEnteredF.show()
        self.SeizureRankingCommentsL.show()
        self.SeizureRankingCommentsF.show()
        self.SeizureRankingSaveButton.show()

    def openurinektsg(self):
        self.UrineKtSGMRNumberL.show()
        self.UrineKtSGMRNumberF.show()
        self.UrineKtSGDateL.show()
        self.UrineKtSGDateF.show()
        self.UrineKtSGDayTypeL.show()
        self.UrineKtSGDayTypeF.show()
        self.UrineKtSGUrineKtL.show()
        self.UrineKtSGUrineKtF.show()
        self.UrineKtSGUrineSGL.show()
        self.UrineKtSGUrineSGF.show()
        self.UrineKtSGEnteredL.show()
        self.UrineKtSGEnteredF.show()
        self.UrineKtSGCommentsL.show()
        self.UrineKtSGCommentsF.show()
        self.UrineKtSGSaveButton.show()

    def openvitals(self):
        self.VitalsMRNumberL.show()
        self.VitalsMRNumberF.show()
        self.VitalsDateL.show()
        self.VitalsDateF.show()
        self.VitalsDayTypeL.show()
        self.VitalsDayTypeF.show()
        self.VitalsSourceL.show()
        self.VitalsSourceF.show()
        self.VitalsBPSysL.show()
        self.VitalsBPSysF.show()
        self.VitalsBPDiaL.show()
        self.VitalsBPDiaF.show()
        self.VitalsTempL.show()
        self.VitalsTempF.show()
        self.VitalsRRL.show()
        self.VitalsRRF.show()
        self.VitalsHRL.show()
        self.VitalsHRF.show()
        self.VitalsEnteredL.show()
        self.VitalsEnteredF.show()
        self.VitalsCommentsL.show()
        self.VitalsCommentsF.show()
        self.VitalsSaveButton.show()

    def openvns(self):
        self.VNSMRNumberL.show()
        self.VNSMRNumberF.show()
        self.VNSDateL.show()
        self.VNSDateF.show()
        self.VNSDayTypeL.show()
        self.VNSDayTypeF.show()
        self.VNSMRMagActL.show()
        self.VNSMRMagActF.show()
        self.VNSOutputCurrL.show()
        self.VNSOutputCurrF.show()
        self.VNSVNSFrequencyL.show()
        self.VNSVNSFrequencyF.show()
        self.VNSPulseWidthL.show()
        self.VNSPulseWidthF.show()
        self.VNSSignalOnL.show()
        self.VNSSignalOnF.show()
        self.VNSSignalOffL.show()
        self.VNSSignalOffF.show()
        self.VNSMagnetCurrentL.show()
        self.VNSMagnetCurrentF.show()
        self.VNSMagnetOnL.show()
        self.VNSMagnetOnF.show()
        self.VNSMagnetPulseL.show()
        self.VNSMagnetPulseF.show()
        self.VNSLeadTestL.show()
        self.VNSLeadTestF.show()
        self.VNSEnteredL.show()
        self.VNSEnteredF.show()
        self.VNSCommentsL.show()
        self.VNSCommentsF.show()
        self.VNSSaveButton.show()

    

    def resetinputs(self):

        self.AlertnessMRNumberF.setText(""),
        self.AlertnessDateF.setDate(datetime.date(datetime.now())),
        self.AlertnessDayTypeF.setCurrentIndex(0),
        self.AlertnessF.setText(""),
        self.AlertnessActivityF.setText(""),
        self.AlertnessDevelopmentF.setText(""),
        self.AlertnessEnteredF.setText(""),
        self.AlertnessCommentsF.setText(""),


        self.AnthropometricsMRNumberF.setText(""),
        self.AnthropometricsDateF.setDate(datetime.date(datetime.now())),
        self.AnthropometricsDayTypeF.setCurrentIndex(0),
        self.AnthropometricsSoruceF.setCurrentIndex(0),
        self.AnthropometricsCPF.setCurrentIndex(0),
        self.AnthropometricsPAF.setCurrentIndex(0),
        self.AnthropometricsPAF2.setCurrentIndex(0),
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


        self.ClinicGIMRNumberF.setText(""),   
        self.ClinicGIDateF.setDate(datetime.date(datetime.now())),
        self.ClinicGIDayTypeF.setCurrentIndex(0),
        self.ClinicGIConstF.setCurrentIndex(0),
        self.ClinicGIDiaF.setCurrentIndex(0),
        self.ClinicGIVomF.setCurrentIndex(0),
        self.ClinicGINauseaF.setCurrentIndex(0),
        self.ClinicGIGagF.setCurrentIndex(0),
        self.ClinicGINissenF.setCurrentIndex(0),
        self.ClinicGIConstDesF.setText(""),
        self.ClinicGIDiaDesF.setText(""),
        self.ClinicGIVomDesF.setText(""),
        self.ClinicGINauseaDesF.setText(""),
        self.ClinicGIGagDesF.setText(""),
        self.ClinicGIEnteredF.setText(""),
        self.ClinicGICommentsF.setText(""),


        self.ClinicalLabsMRNumberF.setText(""),
        self.ClinicalLabsDateF.setDate(datetime.date(datetime.now())),
        self.ClinicalLabsTimeF.setText(""),
        self.ClinicalLabsDayTypeF.setCurrentIndex(0),
        self.ClinicalLabsSourceF.setCurrentIndex(0),
        self.ClinicalLabsFastingF.setCurrentIndex(0),
        self.ClinicalLabsTGBloodF.setText(""),
        self.ClinicalLabsHDLBloodF.setText(""),
        self.ClinicalLabsLDLBloodF.setText(""),
        self.ClinicalLabsTCBloodF.setText(""),
        self.ClinicalLabsNABloodF.setText(""),
        self.ClinicalLabsKBloodF.setText(""),
        self.ClinicalLabsChlBloodF.setText(""),
        self.ClinicalLabsCO2BloodF.setText(""),
        self.ClinicalLabsBUNBloodF.setText(""),
        self.ClinicalLabsCrBloodF.setText(""),
        self.ClinicalLabsGlusBloodF.setText(""),
        self.ClinicalLabsCaBloodF.setText(""),
        self.ClinicalLabsMagBloodF.setText(""),
        self.ClinicalLabsPhosBloodF.setText(""),
        self.ClinicalLabsUricAcidBloodF.setText(""),
        self.ClinicalLabsProBloodF.setText(""),
        self.ClinicalLabsAlbBloodF.setText(""),
        self.ClinicalLabsTBilBloodF.setText(""),
        self.ClinicalLabsTotalBilirubinBloodF.setText(""),
        self.ClinicalLabsAstBloodF.setText(""),
        self.ClinicalLabsAltBloodF.setText(""),
        self.ClinicalLabsRBCBloodF.setText(""),
        self.ClinicalLabsHgbBloodF.setText(""),
        self.ClinicalLabsHctBloodF.setText(""),
        self.ClinicalLabsPlateletBloodF.setText(""),
        self.ClinicalLabsMCVBloodF.setText(""),
        self.ClinicalLabsMCHBloodF.setText(""),
        self.ClinicalLabsMCHCBloodF.setText(""),
        self.ClinicalLabsMPVBloodF.setText(""),
        self.ClinicalLabsRDWBloodF.setText(""),
        self.ClinicalLabsWBCBloodF.setText(""),
        self.ClinicalLabsAmmoniaBloodF.setText(""),
        self.ClinicalLabsBHbBloodF.setText(""),
        self.ClinicalLabsAcacBloodF.setText(""),
        self.ClinicalLabsNeutrophilsBloodF.setText(""),
        self.ClinicalLabsLymphocytesBloodF.setText(""),
        self.ClinicalLabsMonocytesBloodF.setText(""),
        self.ClinicalLabsEosinophilsBloodF.setText(""),
        self.ClinicalLabsBasophilsBloodF.setText(""),
        self.ClinicalLabsLargeUnstainedCellsBloodF.setText(""),
        self.ClinicalLabsNeutrophilsAbsoluteBloodF.setText(""),
        self.ClinicalLabsLymphocytesAbsoluteBloodF.setText(""),
        self.ClinicalLabsEosinophilsAbsoluteBloodF.setText(""),
        self.ClinicalLabsBasophilsAbsoluteBloodF.setText(""),
        self.ClinicalLabsGlusBloodCRCF.setText(""),
        self.ClinicalLabsLactBloodCRCMmolF.setText(""),
        self.ClinicalLabsLabBlood1F.setText(""),
        self.ClinicalLabsLabBlood2F.setText(""),
        self.ClinicalLabsLabBlood3F.setText(""),
        self.ClinicalLabsLabBlood4F.setText(""),
        self.ClinicalLabsLabBlood5F.setText(""),
        self.ClinicalLabsLabBlood6F.setText(""),
        self.ClinicalLabsLabBlood7F.setText(""),
        self.ClinicalLabsLabBlood8F.setText(""),
        self.ClinicalLabsLabBlood9F.setText(""),
        self.ClinicalLabsLabBlood10F.setText(""),
        self.ClinicalLabsLabBlood11F.setText(""),
        self.ClinicalLabsLabBlood12F.setText(""),
        self.ClinicalLabsLabBlood13F.setText(""),
        self.ClinicalLabsLabBlood14F.setText(""),
        self.ClinicalLabsLabBlood15F.setText(""),
        self.ClinicalLabsLabBlood16F.setText(""),
        self.ClinicalLabsLabBlood17F.setText(""),
        self.ClinicalLabsLabBlood18F.setText(""),
        self.ClinicalLabsLabBlood19F.setText(""),
        self.ClinicalLabsLabBlood20F.setText(""),
        self.ClinicalLabsLabBlood21F.setText(""),
        self.ClinicalLabsLabBlood22F.setText(""),
        self.ClinicalLabsLabBlood23F.setText(""),
        self.ClinicalLabsLabBlood24F.setText(""),
        self.ClinicalLabsLabBlood25F.setText(""),
        self.ClinicalLabsLabBlood26F.setText(""),
        self.ClinicalLabsLabBlood27F.setText(""),
        self.ClinicalLabsLabBlood28F.setText(""),
        self.ClinicalLabsLabBlood29F.setText(""),
        self.ClinicalLabsLabBlood30F.setText(""),
        self.ClinicalLabsLabBlood31F.setText(""),
        self.ClinicalLabsLabBlood32F.setText(""),
        self.ClinicalLabsLabBlood33F.setText(""),
        self.ClinicalLabsLabBlood34F.setText(""),
        self.ClinicalLabsLabBlood35F.setText(""),
        self.ClinicalLabsLabBlood36F.setText(""),
        self.ClinicalLabsLabBlood37F.setText(""),
        self.ClinicalLabsLabBlood38F.setText(""),
        self.ClinicalLabsLabBlood39F.setText(""),
        self.ClinicalLabsLabBlood40F.setText(""),
        self.ClinicalLabsLabBlood41F.setText(""),
        self.ClinicalLabsLabBlood42F.setText(""),
        self.ClinicalLabsLabBlood43F.setText(""),
        self.ClinicalLabsLabBlood44F.setText(""),
        self.ClinicalLabsLabBlood45F.setText(""),
        self.ClinicalLabsLabBlood46F.setText(""),
        self.ClinicalLabsLabBlood47F.setText(""),
        self.ClinicalLabsLabBlood48F.setText(""),
        self.ClinicalLabsLabBlood49F.setText(""),
        self.ClinicalLabsLabBlood50F.setText(""),
        self.ClinicalLabsEnteredF.setText(""),
        self.ClinicalLabsCommentsF.setText(""),

        self.DailyIntakeMRNumberF.setText(""),
        self.DailyIntakeDateF.setDate(datetime.date(datetime.now())),
        self.DailyIntakeDayTypeF.setCurrentIndex(0),
        self.DailyIntakePKTNUMF.setText(""),
        self.DailyIntakeDataQualityDietF.setCurrentIndex(0),
        self.DailyIntakeDayQualityDietF.setCurrentIndex(0),
        self.DailyIntakeEnteredF.setText(""),
        self.DailyIntakeCommentsF.setText(""),

        self.DietRXMRNumberF.setText(""),
        self.DietRXDateF.setDate(datetime.date(datetime.now())),
        self.DietRXDayTypeF.setCurrentIndex(0),
        self.DietRXROFF.setCurrentIndex(0),
        self.DietRXRFCDF.setCurrentIndex(0),
        self.DietRXSnackCalF.setText(""),
        self.DietRXSnackRatioF.setText(""),
        self.DietRXSnackNumberF.setText(""),
        self.DietRXMealNumberF.setText(""),
        self.DietRXMealRatioF.setText(""),
        self.DietRXCalF.setText(""),
        self.DietRXProF.setText(""),
        self.DietRXEnteredF.setText(""),
        self.DietRXCommentsF.setText(""),

        self.MedDataMRNumberF.setText(""),
        self.MedDataDateF.setDate(datetime.date(datetime.now())),
        self.MedDataDayTypeF.setCurrentIndex(0),
        self.MedDataNDIDF.setText(""),
        self.MedDataMedIDF.setText(""),
        self.MedDataRFCMF.setCurrentIndex(0),
        self.MedDataProdNameF.setText(""),
        self.MedDataDailyDoseF.setText(""),
        self.MedDataMedDosesF.setText(""),
        self.MedDataMedCommentsF.setText(""),
        self.MedDataEnteredF.setText(""),
        self.MedDataCommentsF.setText(""),

        self.MenusMRNumberF.setText(""),
        self.MenusDateF.setDate(datetime.date(datetime.now())),
        self.MenusCalPrcntF.setText(""),
        self.MenusProcntPrcntF.setText(""),
        self.MenusRatioPrF.setText(""),
        self.MenusMealNumberF.setText(""),
        self.MenusSnackNumberF.setText(""),
        self.MenusRecipeNameF.setText(""),
        self.MenusRecipeNumberF.setText(""),
        self.MenusRecipeIngredientAmountF.setText(""),
        self.MenusNDIDF.setText(""),
        self.MenusProdNameF.setText(""),
        self.MenusRecipeTypeF.setCurrentIndex(0),
        self.MenusEnteredF.setText(""),
        self.MenusCommentsF.setText(""),


        self.OtherMedMRNumberF.setText(""),
        self.OtherMedDateF.setDate(datetime.date(datetime.now())),
        self.OtherMedNDIDF.setText(""),
        self.OtherMedProdNameF.setText(""),
        self.OtherMedMedAmountF.setText(""),
        self.OtherMedMedUnitF.setText(""),
        self.OtherMedEnteredF.setText(""),
        self.OtherMedCommentsF.setText(""),

        self.SeizureDataMRNumberF.setText(""),
        self.SeizureDataDateF.setDate(datetime.date(datetime.now())),
        self.SeizureDataDayTypeF.setCurrentIndex(0),
        self.SeizureDataDataQualityF.setCurrentIndex(0),
        self.SeizureDataSeizureSeverityF.setText(""),
        self.SeizureDataSeizureLengthF.setText(""),
        self.SeizureDataSeizureTypeF.setText(""),
        self.SeizureDataSeizureVariableF.setText(""),
        self.SeizureDataSeizureNumberF.setText(""),
        self.SeizureDataSeizureClusterF.setText(""),
        self.SeizureDataEnteredF.setText(""),
        self.SeizureDataCommentsF.setText(""),

        self.SeizureRankingMRNumberF.setText(""),
        self.SeizureRankingSeizureParameterF.setText(""),
        self.SeizureRankingSeizureEntryF.setText(""),
        self.SeizureRankingSeizureRankingF.setText(""),
        self.SeizureRankingEnteredF.setText(""),
        self.SeizureRankingCommentsF.setText(""),


        self.UrineKtSGMRNumberF.setText(""),
        self.UrineKtSGDateF.setDate(datetime.date(datetime.now())),
        self.UrineKtSGDayTypeF.setCurrentIndex(0),
        self.UrineKtSGUrineKtF.setText(""),
        self.UrineKtSGUrineSGF.setText(""),
        self.UrineKtSGEnteredF.setText(""),
        self.UrineKtSGCommentsF.setText(""),

        self.VitalsMRNumberF.setText(""),
        self.VitalsDateF.setDate(datetime.date(datetime.now())),
        self.VitalsDayTypeF.setCurrentIndex(0),
        self.VitalsSourceF.setCurrentIndex(0),
        self.VitalsBPSysF.setText(""),
        self.VitalsBPDiaF.setText(""),
        self.VitalsTempF.setText(""),
        self.VitalsRRF.setText(""),
        self.VitalsHRF.setText(""),
        self.VitalsEnteredF.setText(""),
        self.VitalsCommentsF.setText(""),

        self.VNSMRNumberF.setText(""),
        self.VNSDateF.setDate(datetime.date(datetime.now())),
        self.VNSDayTypeF.setCurrentIndex(0),
        self.VNSMRMagActF.setText(""),
        self.VNSOutputCurrF.setText(""),
        self.VNSVNSFrequencyF.setText(""),
        self.VNSPulseWidthF.setText(""),
        self.VNSSignalOnF.setText(""),
        self.VNSSignalOffF.setText(""),
        self.VNSMagnetCurrentF.setText(""),
        self.VNSMagnetOnF.setText(""),
        self.VNSMagnetPulseF.setText(""),
        self.VNSLeadTestF.setText(""),
        self.VNSEnteredF.setText(""),
        self.VNSCommentsF.setText("")






######################## Sending Input To The Back End ##########################
    def submitAlertness(self,event):

        try:
            saveAlertness(
            self.currentpatient,    
            self.AlertnessMRNumberF.text(),
            self.AlertnessDateF.date().toString("MM/dd/yyyy"),
            self.AlertnessDayTypeF.currentText()[:1],
            self.AlertnessF.toPlainText(),
            self.AlertnessActivityF.toPlainText(),
            self.AlertnessDevelopmentF.toPlainText(),
            self.AlertnessEnteredF.text(),
            self.AlertnessCommentsF.toPlainText()
            )

            self.alertnesspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()

        except ValueError:
            print("There is a value error, placeholder for now WIP")


    def submitAnthropometrics(self,event):
       
        print(self.AnthropometricsPAF2.currentText()[:4])
        print(type(self.AnthropometricsDateF.date()))

        print(str(self.AnthropometricsDateF.date()))
        
        try:
            saveAnthropometrics(
                self.currentpatient,
                int(self.AnthropometricsMRNumberF.text()),
                self.AnthropometricsDateF.date().toString("MM/dd/yyyy"),
                int(self.AnthropometricsDayTypeF.currentText()[:1]),
                int(self.AnthropometricsSoruceF.currentText()[:1]),
                float(self.AnthropometricsCPF.currentText()[:2]),
                float(self.AnthropometricsPAF2.currentText()[:4]),
                float(self.AnthropometricsHtF.text()),
                float(self.AnthropometricsWtF.text()),
                float(self.AnthropometricsHCF.text()),
                float(self.AnthropometricsUACF.text()), 
                float(self.AnthropometricsTSFF.text()),
                float(self.AnthropometricsSSFF.text()),
                float(self.AnthropometricsUSFF.text()),
                float(self.AnthropometricsSISFF.text()),
                float(self.AnthropometricsMBSFF.text()),
                float(self.AnthropometricsUCF.text()),
                self.AnthropometricsEnteredF.text(),
                self.AnthropometricsCommentsF.toPlainText() 
                )
            
            self.anthropometricspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            
            print("Data Entered Successfully")
            self.resetinputs()
            self.loadgraphnames()
        except ValueError: 
            
            self.anthropometricspopupfail = QMessageBox.question(self,"Incorrect Entry","One or more of the values that you entered are incorrect. \n\nPlease ensure that every entry is a number except for the Date, Entered, and Comments fields. ", QMessageBox.Retry)
            if self.anthropometricspopupfail==QMessageBox.Retry:
                print("Data Entered Failed")

    def submitClinicGI(self,event):
        try:
            saveClinicGI(
            self.currentpatient,
            self.ClinicGIMRNumberF.text(),   
            self.ClinicGIDateF.date().toString("MM/dd/yyyy"),
            self.ClinicGIDayTypeF.currentText()[:1],
            self.ClinicGIConstF.currentText(),
            self.ClinicGIDiaF.currentText(),
            self.ClinicGIVomF.currentText(),
            self.ClinicGINauseaF.currentText(),
            self.ClinicGIGagF.currentText(),
            self.ClinicGINissenF.currentText(),
            self.ClinicGIConstDesF.toPlainText(),
            self.ClinicGIDiaDesF.toPlainText(),
            self.ClinicGIVomDesF.toPlainText(),
            self.ClinicGINauseaDesF.toPlainText(),
            self.ClinicGIGagDesF.toPlainText(),
            self.ClinicGIEnteredF.text(),
            self.ClinicGICommentsF.toPlainText()
            )

            self.clinicgipopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()

        except ValueError:
            print("There is a value error, placeholder for now WIP")
       

    def submitClinicalLabs(self,event):
        try:
            saveClinicalLabs(
                self.currentpatient,
                self.ClinicalLabsMRNumberF.text(),
                self.ClinicalLabsDateF.date().toString("MM/dd/yyyy"),
                self.ClinicalLabsTimeF.text(),
                self.ClinicalLabsDayTypeF.currentText()[:1],
                self.ClinicalLabsSourceF.currentText()[:1],
                self.ClinicalLabsFastingF.currentText()[:1],
                self.ClinicalLabsTGBloodF.text(),
                self.ClinicalLabsHDLBloodF.text(),
                self.ClinicalLabsLDLBloodF.text(),
                self.ClinicalLabsTCBloodF.text(),
                self.ClinicalLabsNABloodF.text(),
                self.ClinicalLabsKBloodF.text(),
                self.ClinicalLabsChlBloodF.text(),
                self.ClinicalLabsCO2BloodF.text(),
                self.ClinicalLabsBUNBloodF.text(),
                self.ClinicalLabsCrBloodF.text(),
                self.ClinicalLabsGlusBloodF.text(),
                self.ClinicalLabsCaBloodF.text(),
                self.ClinicalLabsMagBloodF.text(),
                self.ClinicalLabsPhosBloodF.text(),
                self.ClinicalLabsUricAcidBloodF.text(),
                self.ClinicalLabsProBloodF.text(),
                self.ClinicalLabsAlbBloodF.text(),
                self.ClinicalLabsTBilBloodF.text(),
                self.ClinicalLabsTotalBilirubinBloodF.text(), #This should be changed to alp_blood
                self.ClinicalLabsAstBloodF.text(),
                self.ClinicalLabsAltBloodF.text(),
                self.ClinicalLabsRBCBloodF.text(),
                self.ClinicalLabsHgbBloodF.text(),
                self.ClinicalLabsHctBloodF.text(),
                self.ClinicalLabsPlateletBloodF.text(),
                self.ClinicalLabsMCVBloodF.text(),
                self.ClinicalLabsMCHBloodF.text(),
                self.ClinicalLabsMCHCBloodF.text(),
                self.ClinicalLabsMPVBloodF.text(),
                self.ClinicalLabsRDWBloodF.text(),
                self.ClinicalLabsWBCBloodF.text(),
                self.ClinicalLabsAmmoniaBloodF.text(),
                self.ClinicalLabsBHbBloodF.text(),
                self.ClinicalLabsAcacBloodF.text(),
                self.ClinicalLabsNeutrophilsBloodF.text(),
                self.ClinicalLabsLymphocytesBloodF.text(),
                self.ClinicalLabsMonocytesBloodF.text(),
                self.ClinicalLabsEosinophilsBloodF.text(),
                self.ClinicalLabsBasophilsBloodF.text(),
                self.ClinicalLabsLargeUnstainedCellsBloodF.text(),
                self.ClinicalLabsNeutrophilsAbsoluteBloodF.text(),
                "This is Monocutes Absolute Blood",
                self.ClinicalLabsLymphocytesAbsoluteBloodF.text(),
                self.ClinicalLabsEosinophilsAbsoluteBloodF.text(),
                self.ClinicalLabsBasophilsAbsoluteBloodF.text(),
                self.ClinicalLabsGlusBloodCRCF.text(),
                self.ClinicalLabsLactBloodCRCMmolF.text(),
                self.ClinicalLabsLabBlood1F.text(),
                self.ClinicalLabsLabBlood2F.text(),
                self.ClinicalLabsLabBlood3F.text(),
                self.ClinicalLabsLabBlood4F.text(),
                self.ClinicalLabsLabBlood5F.text(),
                self.ClinicalLabsLabBlood6F.text(),
                self.ClinicalLabsLabBlood7F.text(),
                self.ClinicalLabsLabBlood8F.text(),
                self.ClinicalLabsLabBlood9F.text(),
                self.ClinicalLabsLabBlood10F.text(),
                self.ClinicalLabsLabBlood11F.text(),
                self.ClinicalLabsLabBlood12F.text(),
                self.ClinicalLabsLabBlood13F.text(),
                self.ClinicalLabsLabBlood14F.text(),
                self.ClinicalLabsLabBlood15F.text(),
                self.ClinicalLabsLabBlood16F.text(),
                self.ClinicalLabsLabBlood17F.text(),
                self.ClinicalLabsLabBlood18F.text(),
                self.ClinicalLabsLabBlood19F.text(),
                self.ClinicalLabsLabBlood20F.text(),
                self.ClinicalLabsLabBlood21F.text(),
                self.ClinicalLabsLabBlood22F.text(),
                self.ClinicalLabsLabBlood23F.text(),
                self.ClinicalLabsLabBlood24F.text(),
                self.ClinicalLabsLabBlood25F.text(),
                self.ClinicalLabsLabBlood26F.text(),
                self.ClinicalLabsLabBlood27F.text(),
                self.ClinicalLabsLabBlood28F.text(),
                self.ClinicalLabsLabBlood29F.text(),
                self.ClinicalLabsLabBlood30F.text(),
                self.ClinicalLabsLabBlood31F.text(),
                self.ClinicalLabsLabBlood32F.text(),
                self.ClinicalLabsLabBlood33F.text(),
                self.ClinicalLabsLabBlood34F.text(),
                self.ClinicalLabsLabBlood35F.text(),
                self.ClinicalLabsLabBlood36F.text(),
                self.ClinicalLabsLabBlood37F.text(),
                self.ClinicalLabsLabBlood38F.text(),
                self.ClinicalLabsLabBlood39F.text(),
                self.ClinicalLabsLabBlood40F.text(),
                self.ClinicalLabsLabBlood41F.text(),
                self.ClinicalLabsLabBlood42F.text(),
                self.ClinicalLabsLabBlood43F.text(),
                self.ClinicalLabsLabBlood44F.text(),
                self.ClinicalLabsLabBlood45F.text(),
                self.ClinicalLabsLabBlood46F.text(),
                self.ClinicalLabsLabBlood47F.text(),
                self.ClinicalLabsLabBlood48F.text(),
                self.ClinicalLabsLabBlood49F.text(),
                self.ClinicalLabsLabBlood50F.text(),
                self.ClinicalLabsEnteredF.text(),
                self.ClinicalLabsCommentsF.toPlainText()
            )

        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitDailyIntake(self,event):

        try:
            saveDailyIntake(
            self.currentpatient,
            self.DailyIntakeMRNumberF.text(),
            self.DailyIntakeDateF.date().toString("MM/dd/yyyy"),
            self.DailyIntakeDayTypeF.currentText()[:1],
            self.DailyIntakePKTNUMF.text(),
            self.DailyIntakeDataQualityDietF.currentText()[:1],
            self.DailyIntakeDayQualityDietF.currentText()[:1],
            self.DailyIntakeEnteredF.text(),
            self.DailyIntakeCommentsF.toPlainText()
            )
           
            self.dailyintakepopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitDietRX(self,event):
        
        try:
            saveDietRX(
            self.currentpatient,
            self.DietRXMRNumberF.text(),
            self.DietRXDateF.date().toString("MM/dd/yyyy"),
            self.DietRXDayTypeF.currentText()[:1],
            self.DietRXROFF.currentText().split()[0],
            self.DietRXRFCDF.currentText().split()[0],
            self.DietRXSnackCalF.text(),
            self.DietRXSnackRatioF.text(),
            self.DietRXSnackNumberF.text(),
            self.DietRXMealNumberF.text(),
            self.DietRXMealRatioF.text(),
            self.DietRXCalF.text(),
            self.DietRXProF.text(),
            self.DietRXEnteredF.text(),
            self.DietRXCommentsF.toPlainText()
            )

            self.dietrxpopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitMedData(self,event):

        try:
            saveMedData(
            self.currentpatient,
            self.MedDataMRNumberF.text(),
            self.MedDataDateF.date().toString("MM/dd/yyyy"),
            self.MedDataDayTypeF.currentText()[:1],
            self.MedDataNDIDF.text(),
            self.MedDataMedIDF.text(),
            self.MedDataRFCMF.currentText().split()[0],
            self.MedDataProdNameF.text(),
            self.MedDataDailyDoseF.text(),
            self.MedDataMedDosesF.text(),
            self.MedDataMedCommentsF.toPlainText(),
            self.MedDataEnteredF.text(),
            self.MedDataCommentsF.toPlainText()
            )

            self.meddatapopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")
        

    def submitMenus(self,event):
        try:
            saveMenus(
            self.currentpatient,
            self.MenusMRNumberF.text(),
            self.MenusDateF.date().toString("MM/dd/yyyy"),
            self.MenusCalPrcntF.text(),
            self.MenusProcntPrcntF.text(),
            self.MenusRatioPrF.text(),
            self.MenusMealNumberF.text(),
            self.MenusSnackNumberF.text(),
            self.MenusRecipeNameF.text(),
            self.MenusRecipeNumberF.text(),
            self.MenusRecipeIngredientAmountF.text(),
            self.MenusNDIDF.text(),
            self.MenusProdNameF.text(),
            self.MenusRecipeTypeF.currentText()[:1],
            self.MenusEnteredF.text(),
            self.MenusCommentsF.toPlainText()
            )

            self.menuspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")
        

    def submitOtherMed(self,event):
        
        try:
            saveOtherMed(
            self.currentpatient,
            self.OtherMedMRNumberF.text(),
            self.OtherMedDateF.date().toString("MM/dd/yyyy"),
            self.OtherMedNDIDF.text(),
            self.OtherMedProdNameF.text(),
            self.OtherMedMedAmountF.text(),
            self.OtherMedMedUnitF.text(),
            self.OtherMedEnteredF.text(),
            self.OtherMedCommentsF.toPlainText()
            )

            self.othermedpopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitSeizureData(self,event):

        try:
            saveSeizureData(
            self.currentpatient,
            self.SeizureDataMRNumberF.text(),
            self.SeizureDataDateF.date().toString("MM/dd/yyyy"),
            self.SeizureDataDayTypeF.currentText()[:1],
            self.SeizureDataDataQualityF.currentText()[:1],
            self.SeizureDataSeizureSeverityF.text(),
            self.SeizureDataSeizureLengthF.text(),
            self.SeizureDataSeizureTypeF.text(),
            self.SeizureDataSeizureVariableF.text(),
            self.SeizureDataSeizureNumberF.text(),
            self.SeizureDataSeizureClusterF.text(),
            self.SeizureDataEnteredF.text(),
            self.SeizureDataCommentsF.toPlainText()
            )

            self.seizuredatapopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitSeizureRanking(self,event):
        
        try:
            saveSeizureRanking(
            self.currentpatient,
            self.SeizureRankingMRNumberF.text(),
            self.SeizureRankingSeizureParameterF.text(),
            self.SeizureRankingSeizureEntryF.text(),
            self.SeizureRankingSeizureRankingF.text(),
            self.SeizureRankingEnteredF.text(),
            self.SeizureRankingCommentsF.toPlainText()
            )

            self.seizurerankingpopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitUrineKtSG(self,event):
        
        try:
            saveUrineKtSG(
            self.currentpatient,
            self.UrineKtSGMRNumberF.text(),
            self.UrineKtSGDateF.date().toString("MM/dd/yyyy"),
            self.UrineKtSGDayTypeF.currentText()[:1],
            self.UrineKtSGUrineKtF.text(),
            self.UrineKtSGUrineSGF.text(),
            self.UrineKtSGEnteredF.text(),
            self.UrineKtSGCommentsF.toPlainText()
            )

            self.urinektsgpopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitVitals(self,event):
        
        try:
            saveVitals(
            self.currentpatient,
            self.VitalsMRNumberF.text(),
            self.VitalsDateF.date().toString("MM/dd/yyyy"),
            self.VitalsDayTypeF.currentText()[:1],
            self.VitalsSourceF.currentText()[:1],
            self.VitalsBPSysF.text(),
            self.VitalsBPDiaF.text(),
            self.VitalsTempF.text(),
            self.VitalsRRF.text(),
            self.VitalsHRF.text(),
            self.VitalsEnteredF.text(),
            self.VitalsCommentsF.toPlainText()
            )

            self.vitalspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitVNS(self,event):
        try:
            saveVNS(
            currentpatient,
            self.VNSMRNumberF.text(),
            self.VNSDateF.date().toString("MM/dd/yyyy"),
            self.VNSDayTypeF.currentText()[:1],
            self.VNSMRMagActF.text(),
            self.VNSOutputCurrF.text(),
            self.VNSVNSFrequencyF.text(),
            self.VNSPulseWidthF.text(),
            self.VNSSignalOnF.text(),
            self.VNSSignalOffF.text(),
            self.VNSMagnetCurrentF.text(),
            self.VNSMagnetOnF.text(),
            self.VNSMagnetPulseF.text(),
            self.VNSLeadTestF.text(),
            self.VNSEnteredF.text(),
            self.VNSCommentsF.toPlainText()
            )

            self.vnspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            self.resetinputs()
            self.loadgraphnames()
        except ValueError:
            print("There is a value error, placeholder for now WIP")

def main():
    app = QApplication(sys.argv)
    
    # loginwindow = Login()
    # loginwindow.show()

    
    test = Test()
    test.show()
    app.exec_()


if __name__ == "__main__":
    main()
