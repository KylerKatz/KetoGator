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

def saveClinicalLabs(patient,MRNumber,Date,Time,DayType,Source,Fasting,TGBlood,HDLBlood,LDLBlood,TCBlood,NABlood,KBlood,ChlBlood,CO2Blood,BUNBlood,CrBlood,GlusBlood,CaBlood,MagBlood,PhosBlood,UricAcidBlood,ProBlood,
AlbBlood,TBilBlood,TotalBilirubinBlood,AstBlood,AltBlood,RBCBlood,HgbBlood,HctBlood,PlateletBlood,MCVBlood,MCHBlood,MCHCBlood,MPVBlood,RDWBlood,WBCBlood,AmmoniaBlood,BHbBlood,AcacBlood, 
NeutrophilsBlood,LymphocytesBlood,MonocytesBlood,EosinophilsBlood,BasophilsBlood,LargeUnstainedCellsBlood,NeutrophilsAbsoluteBlood,LymphocytesAbsoluteBlood,EosinophilsAbsoluteBlood,BasophilsAbsoluteBlood,
GlusBloodCRC,LactBloodCRCMmol,LabBlood1,LabBlood2,LabBlood3,LabBlood4,LabBlood5,LabBlood6,LabBlood7,LabBlood8,LabBlood9,LabBlood10,LabBlood11,LabBlood12,LabBlood13,LabBlood14,LabBlood15,LabBlood16,LabBlood17,
LabBlood18,LabBlood19,LabBlood20,LabBlood21,LabBlood22,LabBlood23,LabBlood24,LabBlood25,LabBlood26,LabBlood27,LabBlood28,LabBlood29,LabBlood30,LabBlood31,LabBlood32,LabBlood33,LabBlood34,LabBlood35,LabBlood36,
LabBlood37,LabBlood38,LabBlood39,LabBlood40,LabBlood41,LabBlood42,LabBlood43,LabBlood44,LabBlood45,LabBlood46,LabBlood47,LabBlood48,LabBlood49,LabBlood50,Entered,Comments):
    pass

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


def saveMedData(patient,MrNumber,Date,DayType,NDID,MedID,RFCM,ProdName,DailyDose,MedDose,MedComments,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Med_Data_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","NDID","Med_ID","Reason_For_Change_Med", "Prod_Name", "Daily_Med_Dose_Mg", "Med_Doses", "Med_Comments", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,NDID,MedID,RFCM,ProdName,DailyDose,MedDose,MedComments,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveMenus(patient,MrNumber,Date,CalPrcnt,ProcntPrcnt,RatioPr,MealNumber,SnackNumber,RecipeName,RecipeNumber,RecipeIngredientAmount,NDID,ProdName,RecipeType,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Menus_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Menus"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Menus"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Cal_Prcnt","Procnt_Prcnt","Ratio_Pr","Meal_Number_Pr", "Snack_Number_Pr", "PKT_Recipe_Name", "PKT_Recipe_Number", "PKT_Recipe_Ingredient_Amount", "NDID", "Prod_Name", "Recipe_Type", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,CalPrcnt,ProcntPrcnt,RatioPr,MealNumber,SnackNumber,RecipeName,RecipeNumber,RecipeIngredientAmount,NDID,ProdName,RecipeType,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveOtherMed(patient,MrNumber,Date,NDID,ProdName,MedAmount,MedUnit,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Other_Med_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Menus"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Menus"

        # Create appropriate columns
        ws.append(["MrNumber","Date","NDID","Prod_Name","Med_Amount","Med_Unit", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,NDID,ProdName,MedAmount,MedUnit,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveSeizureData(patient,MrNumber,Date,DayType,DataQuality,SeizureSeverity,SeizureLength,SeizureType,SeizureVariable,SeizureNumber,SeizureCluster,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Seizure_Data_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Data_Quality_S","Seizure_Severity","Seizure_Length", "Seizure_Type", "Seizure_Variable", "Seizure_Number", "Seizure_Cluster", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,DataQuality,SeizureSeverity,SeizureLength,SeizureType,SeizureVariable,SeizureNumber,SeizureCluster,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveSeizureRanking(patient,MrNumber,SeizureParameter,SeizureEntry,SeizureRanking,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Seizure_Ranking_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Seizure_Parameter","Seizure_Entry","Seizure_Ranking", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,SeizureParameter,SeizureEntry,SeizureRanking,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveUrineKtSG(patient,MrNumber,Date,DayType,UrineKt,UrineSG,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Urine_Kt_SG_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Urine_Kt","Urine_SG", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,UrineKt,UrineSG,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveVitals(patient,MrNumber,Date,DayType,Source,BPSys,BPDia,Temp,RR,HR,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Vitals_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Day_Type","Source","BP_Sys", "BP_Dia", "T", "RR", "HR", "Entered", "Audited", "Comments"])

    # Add data
    ws.append([MrNumber,Date,DayType,Source,BPSys,BPDia,Temp,RR,HR,Entered,"",Comments])

    #Save modified workbook
    wb.save(path)

def saveVNS(patient,MrNumber,Date,DayType,MRMagAct,OutPutCurr,VNSFrequency,PluseWidth,SignalOn,SingnalOff,MagnetCurrent,MagnetOn,MagnetPulse,LeadTest,Entered,Comments):
    path = r"Current Patients\\" + patient + r"\\DataBases\\Data\\" + patient + r"_Clinic_VNS_Source.xlsx"
    
    # Tries to load workbook
    try:
        wb = load_workbook(path)
        ws = wb["Sheet1"]
    # On failure ensures they have the right directories using setNewPatient
    except FileNotFoundError:
        setNewPatient(patient)

        # Create new workbook and name sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Create appropriate columns
        ws.append(["MrNumber","Date","Mag_Act","Output_Curr","VNS_Frequency", "Pulse_Width", "Signal_On", "Signal_Off", "Magnet_Current", "Magnet_On", "Magnet_Pulse", "Lead_Test" "Entered", "Audited", "Comments"])

    # Add data
    ws.append([patient,MrNumber,Date,DayType,MRMagAct,OutPutCurr,VNSFrequency,PluseWidth,SignalOn,SingnalOff,MagnetCurrent,MagnetOn,MagnetPulse,LeadTest,Entered,"",Comments])

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
