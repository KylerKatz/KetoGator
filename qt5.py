import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QFont
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

        self.AnthropometricsWtL = QLabel("Weight - kg")
        self.AnthropometricsWtL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsWtL.setToolTip("Measure of ponderal growth. It is collected in one of 2 ways for patients: 1) patient standing on a scale; 2) patient is weighed with wheelchair and wheelchair weight is subtracted from first weight.")
        self.AnthropometricsWtF = QLineEdit()

        self.AnthropometricsHCL = QLabel("Head Circumference - cm")
        self.AnthropometricsHCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsHCL.setToolTip("Measurement of the head around its largest area. It measures the distance from above the eyebrows and ears and around the back of the head. The average of 3 readings is recorded.")
        self.AnthropometricsHCF = QLineEdit()

        self.AnthropometricsUACL = QLabel("Upper Arm Circumference - cm")
        self.AnthropometricsUACL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUACL.setToolTip("The circumference of the upper right arm. Measured at the mid-point between the tip of the shoulder and the tip of the elbow (olecranon process and the acromium). \nPatient's elbow should be flexed to 90 degrees with the palm facing superiorly. The average of 3 readings is recorded.")
        self.AnthropometricsUACF = QLineEdit()

        self.AnthropometricsTSFL = QLabel("Triceps Skinfold - mm")
        self.AnthropometricsTSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsTSFL.setToolTip("Triceps skinfold thickness measured with a skinfold caliper. Measured at the back of the midpoint of the upper right arm. \nPatient should stand or lie down with right arm hanging loosely by the side. The average of 3 readings is recorded.")
        self.AnthropometricsTSFF = QLineEdit()

        self.AnthropometricsSSFL = QLabel("Subscapular Skinfold - mm")
        self.AnthropometricsSSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSSFL.setToolTip("Subscapular skinfold thickness measured with a skinfold caliper. Measured 1 cm below the inferior angle of the right scapula (shoulder blade). The average of 3 readings is recorded.")
        self.AnthropometricsSSFF = QLineEdit()

        self.AnthropometricsUSFL = QLabel("Umbilicus Skinfold - mm")
        self.AnthropometricsUSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUSFL.setToolTip("Umbilicus skinfold thickness measured with a skinfold caliper. The vertical umbilicus skinfold is measured by pinching the abdominal fat fold vertically \nabout 2.5 cm to the right of the patient’s umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsUSFF = QLineEdit()

        self.AnthropometricsSISFL = QLabel("Suprailiac Skinfold - mm")
        self.AnthropometricsSISFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsSISFL.setToolTip("Suprailiac skinfold thickness measured with a skinfold caliper. The vertical supra iliac skinfolds are measured by pinching the side fatfolds vertically \nat the mid-axilary line and at the level of the umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsSISFF = QLineEdit()

        self.AnthropometricsMBSFL = QLabel("Midback Skinfold - mm")
        self.AnthropometricsMBSFL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsMBSFL.setToolTip("Mid back skinfold thickness measured with a skinfold caliper. The vertical mid-back skinfold is measured by pinching the back fat fold about 2.5 cm to the \nright of the spinal column at the level of the umbilicus. The average of 3 readings is recorded.")
        self.AnthropometricsMBSFF = QLineEdit()

        self.AnthropometricsUCL = QLabel("Umbilical Circumference - cm")
        self.AnthropometricsUCL.setFont(QtGui.QFont("Ariel", 13))
        self.AnthropometricsUCL.setToolTip("Circumference of the mid-section of the body at the umbilicus (belly button), perpendicular to the long axis of the body. The average of 3 readings is recorded.")
        self.AnthropometricsUCF = QLineEdit()

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
        self.DietRXSnackCalF.setMaxLength(4)

        self.DietRXSnackRatioL = QLabel("Snack Ratio Prescribed - (2 Decimals)")
        self.DietRXSnackRatioL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXSnackRatioL.setToolTip("Snack PKT ratio precribed per day")
        self.DietRXSnackRatioF = QLineEdit()
        self.DietRXSnackRatioF.setMaxLength(3)

        self.DietRXSnackNumberL = QLabel("Snack Number Prescribed")
        self.DietRXSnackNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXSnackNumberL.setToolTip("Total number of snacks precribed per day")
        self.DietRXSnackNumberF = QLineEdit()
        self.DietRXSnackNumberF.setMaxLength(2)

        self.DietRXMealNumberL = QLabel("Meal Number Prescribed")
        self.DietRXMealNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXMealNumberL.setToolTip("Total number of meals prescribed per day")
        self.DietRXMealNumberF = QLineEdit()
        self.DietRXMealNumberF.setMaxLength(2)
        self.DietRXMealNumberF.setPlaceholderText("Required")

        self.DietRXMealRatioL = QLabel("Meal Ratio Prescribed - (2 Decimals)")
        self.DietRXMealRatioL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXMealRatioL.setToolTip("Meal PKT ratio of amount of fat per amount of carbohydrate plus amount of protein prescribed per day")
        self.DietRXMealRatioF = QLineEdit()
        self.DietRXMealRatioF.setMaxLength(3)
        self.DietRXMealRatioF.setPlaceholderText("Required")
        
        self.DietRXCalL = QLabel("Calories Prescribed - (2 Decimals)")
        self.DietRXCalL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXCalL.setToolTip("Total calories prescribed per day")
        self.DietRXCalF = QLineEdit()
        self.DietRXCalF.setMaxLength(6)
        self.DietRXCalF.setPlaceholderText("Required")

        self.DietRXProL = QLabel("Protein Prescribed - (2 Decimals)")
        self.DietRXProL.setFont(QtGui.QFont("Ariel", 13))
        self.DietRXProL.setToolTip("Perecent of intake versus recommended intake for proline")
        self.DietRXProF = QLineEdit()
        self.DietRXProF.setMaxLength(4)
        self.DietRXProF.setPlaceholderText("Required")

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

        self.MedDataMedDosesL = QLabel("Med Doses")
        self.MedDataMedDosesL.setFont(QtGui.QFont("Ariel", 13))
        self.MedDataMedDosesL.setToolTip("Total number of doses AED per day either presribed or consumed")
        self.MedDataMedDosesF = QLineEdit()
        self.MedDataMedDosesF.setMaxLength(2)

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

        self.MenusProcntPrcntL = QLabel("Protein Prescribed - (g)")
        self.MenusProcntPrcntL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusProcntPrcntL.setToolTip("Percent of intake versus recommended intake for proline")
        self.MenusProcntPrcntF = QLineEdit()
        self.MenusProcntPrcntF.setMaxLength(4)
        self.MenusProcntPrcntF.setPlaceholderText("Required")

        self.MenusRatioPrL = QLabel("Ratio Prescribed")
        self.MenusRatioPrL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRatioPrL.setToolTip("Meal PKT ratio precribed of amount of fat per amount of carbohydrates plus amount of protein")
        self.MenusRatioPrF = QLineEdit()
        self.MenusRatioPrF.setMaxLength(3)
        self.MenusRatioPrF.setPlaceholderText("Required")

        self.MenusRatioPrL = QLabel("Ratio Prescribed")
        self.MenusRatioPrL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusRatioPrL.setToolTip("Meal PKT ratio precribed of amount of fat per amount of carbohydrates plus amount of protein")
        self.MenusRatioPrF = QLineEdit()
        self.MenusRatioPrF.setMaxLength(3)
        self.MenusRatioPrF.setPlaceholderText("Required")

        self.MenusMealNumberL = QLabel("Meal Number Prescribed")
        self.MenusMealNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusMealNumberL.setToolTip("Total number of meals prescribed per day")
        self.MenusMealNumberF = QLineEdit()
        self.MenusMealNumberF.setMaxLength(2)
        self.MenusMealNumberF.setPlaceholderText("Required")
        
        self.MenusSnackNumberL = QLabel("Snack Number Prescribed")
        self.MenusSnackNumberL.setFont(QtGui.QFont("Ariel", 13))
        self.MenusSnackNumberL.setToolTip("Total number of snacks precribed per day")
        self.MenusSnackNumberF = QLineEdit()
        self.MenusSnackNumberF.setMaxLength(2)
        self.MenusSnackNumberF.setPlaceholderText("Cell can be blank if the patient does not receive a snack. Otherwise it is required")

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
        self.MenusRecipeIngredientAmountF.setMaxLength(5)
        
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
        
        self.MenusRecipeTypeL = QLabel("Product Name")
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
        self.graphinputformdailyintake = QGridLayout()
        self.graphinputformdietrx = QGridLayout()
        self.graphinputformmeddata = QGridLayout()
        self.graphinputformmenus = QGridLayout()




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
        self.graphinputformmenus.addWidget(self.MenusRatioPrL,5,0)
        self.graphinputformmenus.addWidget(self.MenusRatioPrF,5,1)
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
        
        
     
        
        # Set Up Scroll Boxes 

        self.alertnessbox = QGroupBox()
        self.alertnessbox.setLayout(self.graphinputformalertness)
        self.alertnessformscroll = QScrollArea()

        self.alertnessformscroll.setWidget(self.alertnessbox)
        self.alertnessformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.alertnessformscroll)
###############################

        self.anthropometricsbox = QGroupBox()
        self.anthropometricsbox.setLayout(self.graphinputformalertness)
        self.anthropometricsformscroll = QScrollArea()

        self.anthropometricsformscroll.setWidget(self.anthropometricsbox)
        self.anthropometricsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.anthropometricsformscroll)
###############################

        self.clinicGIbox = QGroupBox()
        self.clinicGIbox.setLayout(self.graphinputformclinicGI)
        
        self.clinicGIformscroll = QScrollArea()
        self.clinicGIformscroll.setWidget(self.clinicGIbox)
        self.clinicGIformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.clinicGIformscroll)
###############################
        self.dailyIntakebox = QGroupBox()
        self.dailyIntakebox.setLayout(self.graphinputformdailyintake)
        
        self.dailyIntakeformscroll = QScrollArea()
        self.dailyIntakeformscroll.setWidget(self.dailyIntakebox)
        self.dailyIntakeformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.dailyIntakeformscroll)

###############################

        self.dietrxbox = QGroupBox()
        self.dietrxbox.setLayout(self.graphinputformdietrx)
        
        self.dietrxformscroll = QScrollArea()
        self.dietrxformscroll.setWidget(self.dietrxbox)
        self.dietrxformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.dietrxformscroll)

###############################

        self.meddatabox = QGroupBox()
        self.meddatabox.setLayout(self.graphinputformmeddata)
        
        self.meddataformscroll = QScrollArea()
        self.meddataformscroll.setWidget(self.meddatabox)
        self.meddataformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.meddataformscroll)
###############################

        self.menusbox = QGroupBox()
        self.menusbox.setLayout(self.graphinputformmenus)
        
        self.menusformscroll = QScrollArea()
        self.menusformscroll.setWidget(self.menusbox)
        self.menusformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.menusformscroll)



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
        self.DailyIntakeSaveButton.mousePressEvent = self.submitDailyIntake
        self.DietRXSaveButton.mousePressEvent = self.submitDietRX

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
        print("Logo Clicked")
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
            print("No Graph to delete")
    


        
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


        print(item.text())

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
        
        if(selection == "Menus"):
            self.closeallfroms()
            self.removeallforms()

            self.menusbox = QGroupBox()
            self.menusbox.setLayout(self.graphinputformmenus)
            
            self.menusformscroll = QScrollArea()
            self.menusformscroll.setWidget(self.menusbox)
            self.menusformscroll.setWidgetResizable(True)

            self.middle.addWidget(self.menusformscroll)

            self.openmenus()
               

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
        print(newlist)
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
      
        self.currentpatient = self.sender().text()[12:]
        print(self.currentpatient)         
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
        self.closedailyintake()
        self.closedietrx()
        self.closemenus()

        self.alertnessbox.close()
        self.alertnessformscroll.close()

        self.anthropometricsbox.close()
        self.anthropometricsformscroll.close()   

        self.clinicGIbox.close()
        self.clinicGIformscroll.close() 

        self.dailyIntakebox.close()
        self.dailyIntakeformscroll.close()

        self.dietrxbox.close()
        self.dietrxformscroll.close()

        self.meddatabox.close()
        self.meddataformscroll.close()

        self.menusbox.close()
        self.menusformscroll.close()

    def removeallforms(self):
        # self.middle.removeItem(self.graphinputformalertness)
        self.middle.removeWidget(self.alertnessformscroll)

        # self.middle.removeItem(self.graphinputformanthropometrics)
        self.middle.removeWidget(self.anthropometricsformscroll)

        # self.middle.removeItem(self.graphinputformclinicGI)
        self.middle.removeWidget(self.clinicGIformscroll)

        self.middle.removeWidget(self.dailyIntakeformscroll)

        self.middle.removeWidget(self.dietrxformscroll)

        self.middle.removeWidget(self.meddataformscroll)

        self.middle.removeWidget(self.menusformscroll)


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


    

    def resetinputs(self):
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

######################## Sending Input To The Back End ##########################
    def submitAlertness(self,event):

        try:
            saveAlertness(
            self.currentpatient,    
            self.AlertnessMRNumberF.text(),
            self.AlertnessDateF.date(),
            self.AlertnessDayTypeF.currentText()[:1],
            self.AlertnessF.toPlainText(),
            self.AlertnessActivityF.toPlainText(),
            self.AlertnessDevelopmentF.toPlainText(),
            self.AlertnessEnteredF.text(),
            self.AlertnessCommentsF.toPlainText()
            )

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
                self.AnthropometricsDateF.date(),
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
            self.ClinicGIDateF.date(),
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

        except ValueError:
            print("There is a value error, placeholder for now WIP")
       
            
    def submitDailyIntake(self,event):

        try:
            saveDailyIntake(
            self.currentpatient,
            self.DailyIntakeMRNumberF.text(),
            self.DailyIntakeDateF.date(),
            self.DailyIntakeDayTypeF.currentText()[:1],
            self.DailyIntakePKTNUMF.text(),
            self.DailyIntakeDataQualityDietF.currentText()[:1],
            self.DailyIntakeDayQualityDietF.currentText()[:1],
            self.DailyIntakeEnteredF.text(),
            self.DailyIntakeCommentsF.toPlainText()
            )
           
        except ValueError:
            print("There is a value error, placeholder for now WIP")

    def submitDietRX(self,event):
        
        try:
            saveDietRX(
            self.currentpatient,
            self.DietRXMRNumberF.text(),
            self.DietRXDateF.date(),
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
