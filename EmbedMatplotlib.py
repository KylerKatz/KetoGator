from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from SpreadSheetAccess import *

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         title = "Matplotlib Embedding in PyQt5"
#         top = 400
#         left = 400
#         width = 900
#         height = 500

#         self.setWindowTitle(title)
#         self.setGeometry(top, left, width, height)

#         self.MyUI()

#     def MyUI(self):

#         canvas = Canvas("TeSt2", self)
#         canvas.move(0,0)

class Canvas(FigureCanvas):
    def __init__(self, patient, parent = None, width = 15, height = 10, dpi = 100, plot=""):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        if plot == "Anthropometrics":
            self.plot(patient)
        elif plot == "Med Load":
            self.medloadplot(patient)

    def plot(self, patient):
        try:
            ht_z = []
            wt_z = []
            bmi_z = []
            age = []
            data = getAnthropometricsDataFrame(patient)

            date_arr = pd.to_datetime(data["Date"])
            height = np.array(data["Ht"])
            height = height[~np.isnan(height)]
            mean_h = np.mean(height)
            weight = np.array(data["Wt"])
            weight = weight[~np.isnan(weight)]
            mean_w = np.mean(weight)

            age.append(0)
            firstdate = date_arr[0]
            d0 = date(firstdate.year, firstdate.month, firstdate.day)

            for x in date_arr[1:]:
                d1 = date(x.year, x.month, x.day)
                datedif = d1 - d0
                age.append(round(datedif.days/365, 1))
            
            data["Age"] = age

            L_CDC_HT = ((np.random.rand(len(age), 1) * 3) - 1)
            M_CDC_HT = ((np.random.rand(len(age), 1) * 127) + 50)
            S_CDC_HT = ((np.random.rand(len(age), 1) * 0.02) + 0.03)

            L_CDC_WT = ((np.random.rand(len(age), 1) * 3) - 1)
            M_CDC_WT = ((np.random.rand(len(age), 1) * 68) + 3)
            S_CDC_WT = ((np.random.rand(len(age), 1) * 0.3) - 0.1)

            L_CDC_BMI = ((np.random.rand(len(age), 1) * -3) - 1)
            M_CDC_BMI = ((np.random.rand(len(age), 1) * 7) + 15)
            S_CDC_BMI = ((np.random.rand(len(age), 1) * 0.06) + 0.07)

            L_WHO_HT = 1
            M_WHO_HT = ((np.random.rand(len(age), 1) * 55) + 110)
            S_WHO_HT = ((np.random.rand(len(age), 1) * 0.01) + 0.04)

            L_WHO_WT = ((np.random.rand(len(age), 1) * -0.55) - 0.15)
            M_WHO_WT = ((np.random.rand(len(age), 1) * 14) + 18)
            S_WHO_WT = ((np.random.rand(len(age), 1) * 0.04) + 0.13)

            L_WHO_BMI = ((np.random.rand(len(age), 1) * 2.6) - .6)

            MEAN_NHANES_HT = ((np.random.rand(len(age), 1) * 94) + 82)
            SD_NHANES_HT = ((np.random.rand(len(age), 1) * 3) + 4)

            MEAN_NHANES_WT = ((np.random.rand(len(age), 1) * 70) + 10)
            SD_NHANES_WT = ((np.random.rand(len(age), 1) * 21) + 1)

            MEAN_NHANES_BMI = ((np.random.rand(len(age), 1) * 10) + 17)
            SD_NHANES_BMI = ((np.random.rand(len(age), 1) * 6) + 1)

            data["L_CDC_HT"] = L_CDC_HT
            data["M_CDC_HT"] = M_CDC_HT
            data["S_CDC_HT"] = S_CDC_HT

            data["L_CDC_WT"] = L_CDC_WT
            data["M_CDC_WT"] = M_CDC_WT
            data["S_CDC_WT"] = S_CDC_WT

            data["L_CDC_BMI"] = L_CDC_BMI
            data["M_CDC_BMI"] = M_CDC_BMI
            data["S_CDC_BMI"] = S_CDC_BMI

            data["M_WHO_HT"] = M_WHO_HT
            data["S_WHO_HT"] = S_WHO_HT

            data["L_WHO_WT"] = L_WHO_WT
            data["M_WHO_WT"] = M_WHO_WT
            data["S_WHO_WT"] = S_WHO_WT

            data["L_WHO_BMI"] = L_WHO_BMI
            data["M_WHO_BMI"] = M_CDC_BMI
            data["S_WHO_BMI"] = S_CDC_BMI

            data["MEAN_NHANES_HT"] = MEAN_NHANES_HT
            data["SD_NHANES_HT"] = SD_NHANES_HT

            data["MEAN_NHANES_WT"] = MEAN_NHANES_WT
            data["SD_NHANES_WT"] = SD_NHANES_WT

            data["MEAN_NHANES_BMI"] = MEAN_NHANES_BMI
            data["SD_NHANES_BMI"] = SD_NHANES_BMI

            for index, row in data.iterrows():
                if(pd.isna(row["Ht"]) == False and pd.isna(row["Wt"]) == False):
                    if(row["Age"] >= 2 and row["Age"] <= 20):
                        ht_z.append((((row["Ht"]/row["M_CDC_HT"])**row["L_CDC_HT"])-1)/(row["L_CDC_HT"]*row["S_CDC_HT"]))
                        wt_z.append((((row["Wt"]/row["M_CDC_WT"])**row["L_CDC_WT"])-1)/(row["L_CDC_WT"]*row["S_CDC_WT"]))
                        bmi_z.append(((((row["Wt"]/((row["Ht"]/100)**2))/row["M_CDC_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    elif(row["Age"] < 2):
                        ht_z.append((((row["Ht"]/row["M_WHO_HT"])**L_WHO_HT)-1)/(L_WHO_HT*row["S_WHO_HT"]))
                        wt_z.append((((row["Wt"]/row["M_WHO_WT"])**row["L_WHO_WT"])-1)/(row["L_WHO_WT"]*row["S_WHO_WT"]))
                        bmi_z.append(((((row["Wt"]/((row["Ht"]/100)**2))/row["M_WHO_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    else:
                        ht_z.append((row["Ht"]-row["MEAN_NHANES_HT"])/row["SD_NHANES_HT"])
                        wt_z.append((row["Wt"]-row["MEAN_NHANES_WT"])/row["SD_NHANES_WT"])
                        bmi_z.append(((row["Wt"]/((row["Ht"]/100)**2))-row["MEAN_NHANES_BMI"])/row["SD_NHANES_BMI"])
                elif(pd.isna(row["Ht"]) == True and pd.isna(row["Wt"]) == False):
                    if(row["Age"] >= 2 and row["Age"] <= 20):
                        ht_z.append((((mean_h/row["M_CDC_HT"])**row["L_CDC_HT"])-1)/(row["L_CDC_HT"]*row["S_CDC_HT"]))
                        wt_z.append((((row["Wt"]/row["M_CDC_WT"])**row["L_CDC_WT"])-1)/(row["L_CDC_WT"]*row["S_CDC_WT"]))
                        bmi_z.append(((((row["Wt"]/((mean_h/100)**2))/row["M_CDC_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    elif(row["Age"] < 2):
                        ht_z.append((((mean_h/row["M_WHO_HT"])**L_WHO_HT)-1)/(L_WHO_HT*row["S_WHO_HT"]))
                        wt_z.append((((row["Wt"]/row["M_WHO_WT"])**row["L_WHO_WT"])-1)/(row["L_WHO_WT"]*row["S_WHO_WT"]))
                        bmi_z.append(((((row["Wt"]/((mean_h/100)**2))/row["M_WHO_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    else:
                        ht_z.append((mean_h-row["MEAN_NHANES_HT"])/row["SD_NHANES_HT"])
                        wt_z.append((row["Wt"]-row["MEAN_NHANES_WT"])/row["SD_NHANES_WT"])
                        bmi_z.append(((row["Wt"]/((mean_h/100)**2))-row["MEAN_NHANES_BMI"])/row["SD_NHANES_BMI"])
                else:
                    if(row["Age"] >= 2 and row["Age"] <= 20):
                        ht_z.append((((row["Ht"]/row["M_CDC_HT"])**row["L_CDC_HT"])-1)/(row["L_CDC_HT"]*row["S_CDC_HT"]))
                        wt_z.append((((mean_w/row["M_CDC_WT"])**row["L_CDC_WT"])-1)/(row["L_CDC_WT"]*row["S_CDC_WT"]))
                        bmi_z.append(((((mean_w/((row["Ht"]/100)**2))/row["M_CDC_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    elif(row["Age"] < 2):
                        ht_z.append((((row["Ht"]/row["M_WHO_HT"])**L_WHO_HT)-1)/(L_WHO_HT*row["S_WHO_HT"]))
                        wt_z.append((((mean_w/row["M_WHO_WT"])**row["L_WHO_WT"])-1)/(row["L_WHO_WT"]*row["S_WHO_WT"]))
                        bmi_z.append(((((mean_w/((row["Ht"]/100)**2))/row["M_WHO_BMI"])**row["L_CDC_BMI"])-1)/(row["L_CDC_BMI"]*row["S_CDC_BMI"]))
                    else:
                        ht_z.append((row["Ht"]-row["MEAN_NHANES_HT"])/row["SD_NHANES_HT"])
                        wt_z.append((mean_w-row["MEAN_NHANES_WT"])/row["SD_NHANES_WT"])
                        bmi_z.append(((mean_w/((row["Ht"]/100)**2))-row["MEAN_NHANES_BMI"])/row["SD_NHANES_BMI"])

            new_data = {'Date':date_arr, 'Age':age, 'HtZ':ht_z, 'WtZ':wt_z, 'BmiZ':bmi_z}
            newdf = pd.DataFrame(new_data)

            newdf = newdf.dropna()

            ax = self.figure.add_subplot(111)
            ax.grid(axis='y')
            #ax.plot(date, age)
            ax.plot('Date', 'HtZ', data=newdf, marker='D', markerfacecolor='orange', markersize=14, color='orange', linewidth=6)
            ax.plot('Date', 'WtZ', data=newdf, marker='s', markerfacecolor='purple', markersize=14, color='purple', linewidth=6)
            ax.plot('Date', 'BmiZ', data=newdf, marker='^',  markerfacecolor='green', markersize=14, color='green', linewidth=6)
            ax.legend()
            ax.set_title(patient + " | Anthropometric Z-Scores")
            ax.set_xlabel("Date")
            ax.set_ylabel("Z-score")
            ax.set_facecolor('#f0f0f0')
            
            ax.xaxis.pane.fill = False
            ax.xaxis.pane.set_edgecolor('#f0f0f0')
            
            # ax.set_axis_bgcolor('#f0f0f0')
        except:
            pass

    # Plots Med Load
    def medloadplot(self, patient):
        try:
            # Get appropriate Data
            anthro = getAnthropometricsDataFrame(patient)
            medData = getMedDataDataFrame(patient)

            # Remove Day Type of 3
            anthro = anthro[anthro.Day_Type != 3]
            medData = medData[medData.Day_Type != 3]

            # Create table with necessary information
            anthroTable = anthro[["Date", "Wt"]].copy()
            medTable = medData[["Date", "Med_ID", "Prod_Name", "Daily_Med_Dose_Mg"]].copy()
        
            # Get Med Ranking
            medRankings = pandas.read_excel("MED_RANKING_SOURCE.xlsx")

            # Save med names
            temp = medRankings[["MED_ID","MED_GENERIC_NAME"]].drop_duplicates()

            # Separate MED_ID and MED_MIN_DOSE to remoce duplicates
            medRankings = medRankings[["MED_ID", "MED_MIN_DOSE"]]

            # Remove duplicate MED_IDs, then merge temp, which was holding the name of each med
            medRankings = medRankings.groupby('MED_ID').mean().reset_index()
            medRankings = pd.merge(medRankings, temp, on="MED_ID", how="inner")

            # set column to datetime and add column containing dates with only month and year
            medTable["Date"] = pd.to_datetime(medTable["Date"])
            medTable["MonthDate"] = medTable["Date"].dt.to_period("M")

            # set column to datetime and add column containing dates with only month and year
            anthroTable["Date"] = pd.to_datetime(anthroTable["Date"])
            anthroTable["MonthDate"] = anthroTable["Date"].dt.to_period("M")

            # Remove regular date column, leaving only month and year
            del anthroTable["Date"]

            # Merge based on MonthDate
            medTable = pd.merge(medTable, anthroTable, on="MonthDate", how="outer")

            # Fill any NaN values on Wt
            medTable["Wt"] = medTable["Wt"].fillna(method="ffill")
            medTable["Wt"] = medTable["Wt"].fillna(method="bfill")

            # Calculate med intake
            medTable["Med_Intake"] = medTable["Daily_Med_Dose_Mg"] / medTable["Wt"]

            # Rename column for compatability
            medRankings = medRankings.rename(columns={"MED_ID" : "Med_ID"})

            # Merge and calculate med load
            medTable = pd.merge(medTable, medRankings, on="Med_ID")
            medTable["MED_LOAD_PER_MED"] = medTable["Med_Intake"] / medTable["MED_MIN_DOSE"]

            # Add different med loads in one day to get the total med load
            total = medTable.groupby("Date").agg(sum).reset_index()

            ax = self.figure.add_subplot(111)

            #add total plot
            ax.plot("Date", "MED_LOAD_PER_MED", data=total, marker = 's', markersize = 14, label = "Total", linewidth = 6)

            # Add each Med's med load, while ensuring there are no duplicates
            items = []
            for x in medTable["Med_ID"]:
                if(not x in items):
                    ax.plot("Date", "MED_LOAD_PER_MED", data=medTable.loc[medTable['Med_ID'] == x], marker='D', markersize = 14, label = (medRankings.loc[medRankings['Med_ID'] == x])["MED_GENERIC_NAME"].values[0], linewidth = 6)
                    items.append(x)

            # Add lables
            ax.set_xlabel("Date - (YYYY-MM)")
            ax.set_ylabel("Medication Load")
            ax.legend()
            ax.set_title(patient + " | Med Load")
            ax.set_facecolor('#f0f0f0')
            ax.grid(axis="y")
        except:
            pass
