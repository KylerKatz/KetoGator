import xlrd # used to read from excel document
import xlwt # used to write to excel document
import os

# Returns sheet that has the specified patients anthropometric sheet
def getPatientAnthropometrics(patient):
    try:
        workbook = xlrd.open_workbook(r"Current Patients\\" + patient + "\DataBases\Data\\" + patient + "_Anthropometrics_Source.xlsx")
        worksheet = workbook.sheet_by_name('Anthropometrics')
        return worksheet
    except FileNotFoundError:
        exit("This Patient Doesn't Exist. Please Review Your Spelling")

# Returns list of all patients
def getAllPatients():
    return(os.listdir("./Current Patients"))

