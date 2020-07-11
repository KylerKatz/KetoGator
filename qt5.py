import sys
import os
from PyQt5 import QtWidgets, uic, QtSql, QtCore, QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
from datetime import datetime


from EmbedMatplotlib import *
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure



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
        self.AlertnessDayTypeF.addItems(['','1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

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
        self.AnthropometricsDayTypeF.addItems(['','1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

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
        self.ClinicGIDayTypeF.addItems(['','1 = Use this as baseline for analysis', '2 = On PKT', '3 = Before or after first/last day on PKT', '4 = Other baseline but not for analysis'])

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

        self.ClinicGICommentsL = QLabel("Comments")
        self.ClinicGICommentsL.setFont(QtGui.QFont("Ariel", 13))
        self.ClinicGICommentsL.setToolTip("Additional comments pertaining to the date and data")
        self.ClinicGICommentsF = QTextEdit()

        self.ClinicGISaveButton = QPushButton("Save")
        


        

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
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstL,2,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstF,2,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaL,3,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaF,3,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomL,4,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomF,4,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaL,5,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaF,5,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagL,6,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagF,6,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINissenL,7,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINissenF,7,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstDesL,8,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIConstDesF,8,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaDesL,9,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIDiaDesF,9,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomDesL,10,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIVomDesF,10,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaDesL,11,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGINauseaDesF,11,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagDesL,12,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIGagDesF,12,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGIEnteredL,13,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGIEnteredF,13,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGICommentsL,14,0)
        self.graphinputformclinicGI.addWidget(self.ClinicGICommentsF,14,1)
        self.graphinputformclinicGI.addWidget(self.ClinicGISaveButton,15,1)
    

        
        # Set Up Scroll Boxes 

        self.alertnessbox = QGroupBox()
        self.alertnessbox.setLayout(self.graphinputformalertness)
        self.alertnessformscroll = QScrollArea()

        self.alertnessformscroll.setWidget(self.alertnessbox)
        self.alertnessformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.alertnessformscroll)


        self.anthropometricsbox = QGroupBox()
        self.anthropometricsbox.setLayout(self.graphinputformalertness)
        self.anthropometricsformscroll = QScrollArea()

        self.anthropometricsformscroll.setWidget(self.anthropometricsbox)
        self.anthropometricsformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.anthropometricsformscroll)

        self.clinicGIbox = QGroupBox()
        self.clinicGIbox.setLayout(self.graphinputformclinicGI)
        
        self.clinicGIformscroll = QScrollArea()
        self.clinicGIformscroll.setWidget(self.clinicGIbox)
        self.clinicGIformscroll.setWidgetResizable(True)

        self.middle.addWidget(self.clinicGIformscroll)


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

        self.AnthropometricsSaveButton.mousePressEvent = self.submitAnthropometrics

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

            self.graphinputformalertness.setContentsMargins(200,0,200,0)
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

            self.graphinputformanthropometrics.setContentsMargins(200,0,200,0)
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

            self.graphinputformclinicGI.setContentsMargins(200,0,200,0)
            self.openclinicgi()
               

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

        self.alertnessbox.close()
        self.alertnessformscroll.close()

        self.anthropometricsbox.close()
        self.anthropometricsformscroll.close()   

        self.clinicGIbox.close()
        self.clinicGIformscroll.close() 

    def removeallforms(self):
        # self.middle.removeItem(self.graphinputformalertness)
        self.middle.removeWidget(self.alertnessformscroll)

        # self.middle.removeItem(self.graphinputformanthropometrics)
        self.middle.removeWidget(self.anthropometricsformscroll)

        # self.middle.removeItem(self.graphinputformclinicGI)
        self.middle.removeWidget(self.clinicGIformscroll)


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
                self.AnthropometricsCommentsF.toPlainText(), 
                )
            
            self.anthropometricspopupsucess = QMessageBox.question(self,"Success","The data has been added.", QMessageBox.Ok)
            
            print("Data Entered Successfully")
            self.resetinputs()
            self.loadgraphnames()
        except ValueError: 
            
            self.anthropometricspopupfail = QMessageBox.question(self,"Incorrect Entry","One or more of the values that you entered are incorrect. \n\nPlease ensure that every entry is a number except for the Date, Entered, and Comments fields. ", QMessageBox.Retry)
            if self.anthropometricspopupfail==QMessageBox.Retry:
                print("Data Entered Failed")
            

        

def main():
    app = QApplication(sys.argv)
    
    # loginwindow = Login()
    # loginwindow.show()

    
    test = Test()
    test.show()
    app.exec_()


if __name__ == "__main__":
    main()
