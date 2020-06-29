import xlrd # used to read from excel document
from openpyxl import *
import os

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
    return(os.listdir("./Current Patients"))

def getPatientGraphs(patient):
    return (os.listdir("./Current Patients/"+patient+"/DataBases/Data/"))

def saveAnthropometrics(patient, MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
    wb = load_workbook(path)
    ws = wb['Anthropometrics']

    ws.append([MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC, '', '', Entered, '', Comments])

    wb.save(path)