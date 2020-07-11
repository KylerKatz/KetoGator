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
