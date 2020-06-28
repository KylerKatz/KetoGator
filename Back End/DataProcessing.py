from os import listdir
from os.path import isfile, join
import os
import pandas as pd



#  This function loads the names of all of the files for a given patient, then stores them in a list

def getpatientfiles(patient):
    
    try:
        mypath = os.path.abspath("C://Users//Owner//University of Florida//FSHN Borum Lab Clinical Data - KetoPatients//D18//Clinic//Patient Folders//Current Patients//"+patient+"//Databases//Data//")
        files = []
        stage1files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for file in stage1files:
            if file.endswith('.xlsx'):
                files.append(file)
        return files
    except FileNotFoundError:
        exit("This Patient Doesn't Exist. Please Review Your Spelling")

# This function loads each of the excel files in as a dataframe. This is meant to allow for de identifying. However, currently to do this, it downloads the files to the computer. 
# Still trying to figure out how to make changes to it without saving it locally. Currently, this is commented out and only prints the names  

def loadcsv(patient, files):
    mypath = os.path.abspath("C://Users//Owner//University of Florida//FSHN Borum Lab Clinical Data - KetoPatients//D18//Clinic//Patient Folders//Current Patients//"+patient+"//Databases//Data//")

    for file in files:
        # dataframe = pd.ExcelFile(mypath+"//"+file)
        # dataframe.head(10)
        print(mypath+file)



def main():
    patient = input("Type the ID of the patient whose tables you would like to see: ")
    files = getpatientfiles(patient)
    print(files)
    loadcsv(patient,files)
main()