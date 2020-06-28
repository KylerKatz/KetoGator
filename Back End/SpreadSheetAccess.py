import xlrd # used to read from excel document
import xlwt # used to write to excel document
import os

# Returns sheet that has the specified patients anthropometric sheet
def getPatientAnthropometrics(patient):
    try:
        workbook = xlrd.open_workbook(r"Back End\Current Patients\\" + patient + "\DataBases\Data\\" + patient + "_Anthropometrics_Source.xlsx")
        worksheet = workbook.sheet_by_name('Anthropometrics')
        return worksheet
    except FileNotFoundError:
        exit("This Patient Doesn't Exist. Please Review Your Spelling")

# Returns list of all patients
def getAllPatients():
    return os.listdir("Back End\\Current Patients\\")

def main():
    print("List of Patient IDs")
    print("-------------------")

    i = 1
    patientList = getAllPatients()

    # Print list of patients
    for x in patientList:
        print("{}. {}".format(i,x))
        i += 1

    # Get anthropometric list of specified patient
    patient = input("\nType the ID of the patient whose tables you would like to see: ") 
    worksheet = getPatientAnthropometrics(patient)
    # format to get value from specific cell: worksheet.cell(x,y).value)
    # x represents the row
    # y represents the column

main()