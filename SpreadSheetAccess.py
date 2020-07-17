import xlrd # used to read from excel document
from openpyxl import *
import os
import pandas

# Returns sheet that has the specified patients anthropometric sheet
def getPatientAnthropometrics(patient):
    try:
        path = r"Current Patients\\" + patient + r"\DataBases\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_name('Anthropometrics')
        return workbook
    except FileNotFoundError:
        exit("This Patient Doesn't Exist. Please Review Your Spelling")

# Returns list of all patients
def getAllPatients():
    print("Path is")
    
    cwd = os.getcwd() + "\Current Patients"
    return(os.listdir(cwd))

def getPatientGraphs(patient):
    return (os.listdir("./Current Patients/"+patient+"/DataBases/Data/"))


def saveAlertness(patient,MrNumber,Date,DayType,Alertness,Activity,Development,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Alertness_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb['Sheet1']
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Alertness","Activity","Development", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,Alertness,Activity,Development,Entered, "", Comments])

    #Save modified workbook
    wb.save(path)
 
def saveAnthropometrics(patient, MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb['Anthropometrics']
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Anthropometrics"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Source","CP","PA","Ht","Wt","HC","UAC","TSF","SSF","USF","SIS","MBSF","UC", "R", "X", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC, '', '', Entered, '', Comments])

    #Save modified workbook
    wb.save(path)

def saveClinicGI(patient,MrNumber,Date,DayType,Const,Dia,Vom,Nausea,Gag,Nissen,ConstDes,DiaDes,VomDes,NauseaDes,GagDes,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Clinic_GI_Issues_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb['Sheet1']
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Clinic_Const","Clinic_Dia","Clinic_Vom", "Clinic_Nausea", "Clinic_Gag_Retch", "Clinic_Nissen", "Clinic_Descr_Const", "Clinic_Descr_Dia", "Clinic_Descr_Vom", "Clinic_Descr_Nausea", "Clinic_Descr_Gag_Retch", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,Const,Dia,Vom,Nausea,Gag,Nissen,ConstDes,DiaDes,VomDes,NauseaDes,GagDes,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveDailyIntake(patient,MrNumber,Date,DayType,PKTNUM,DataQuality,DayQuality,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Daily_Intake_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Daily_Intake"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Daily_Intake"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","PKT_Recipe_Number","Data_Quality_D","Day_Quality_D", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,PKTNUM,DataQuality,DayQuality,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveDietRX(patient,MrNumber,Date,DayType,ROF,RFCD,SnackCal,SnackRatio,SnackNumber,MealNumber,MealRatio,TotalCal,Protein,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Diet_RX_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Diet_Rx"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Diet_Rx"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","ROF_Pr","Reason_For_Change_Diet","Snack_Cal_Pr", "Snack_Ratio_Pr", "Snack_Number_Pr", "Meal_Number_Pr", "Ratio_Pr", "Cal_Pr", "Pro_Pr", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,ROF,RFCD,SnackCal,SnackRatio,SnackNumber,MealNumber,MealRatio,TotalCal,Protein,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

# Returns dataframe containing data inside the excel sheet
def getAnthropometricsDataFrame(patient):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
    dataframe = pandas.read_excel(path)
    return dataframe

# Creates appropriate directories for new patient or existing patient who doesn't have them
def setNewPatient(MrNum):
    path = r"Current Patients\\" + MrNum + r"\\DataBases\\Data\\"

    # If path doesn't exist, the function executes, otherwise nothing happens
    if not os.path.isdir(path):
        
        # Used to make appropriate directories
        switch = {
            0: MrNum,
            1: "\DataBases",
            2: "\Data",
        }
        dir = "Current Patients\\"

        # Create necessary directories
        for i in range(3):
            dir = dir + switch.get(i)
            os.mkdir(dir)
