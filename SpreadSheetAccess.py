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
    return(os.listdir("./Current Patients"))

def getPatientGraphs(patient):
    return (os.listdir("./Current Patients/"+patient+"/DataBases/Data/"))

def saveAnthropometrics(patient, MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC,Entered,Comments):
    
    # Do a check to see if the Patient has an Anthropoemtics tabel 

    # If not, create one with the naming scheme MrNumber_Anthropometrics_Source.xlsx

    # Add the columns at the top 

    # Then input the data

    # If so, this is fine 
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
    wb = load_workbook(path)
    ws = wb['Anthropometrics']

    ws.append([MrNumber,Date,DayType,Source,CP,PA,Ht,Wt,HC,UAC,TSF,SSF,USF,SIS,MBSF,UC, '', '', Entered, '', Comments])

    wb.save(path)

def getAnthropometricsDataFrame(patient):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Anthropometrics_Source.xlsx"
    dataframe = pandas.read_excel(path)

    return dataframe

def setNewPatient(MrNum):
    # Create a new Folder for this patient 

    # Create the DataBases and Data Folders 
