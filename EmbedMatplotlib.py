from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from datetime import datetime
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
            data = getAnthropometricsClinicalDataFrame(patient)

            date = pd.to_datetime(data["DATE"])
            age = data["AGE"]

            for index, row in data.iterrows():
                if(row["AGE"] >= 2 and row["AGE"] <= 20):
                    if(pd.isna(row["CDC_HT_Z"]) == False):
                        ht_z.append(row["CDC_HT_Z"])
                    else:
                        ht_z.append(row["CDC_HT_Z_DAY"])
                    
                    if(pd.isna(row["CDC_WT_Z"]) == False):
                        wt_z.append(row["CDC_WT_Z"])
                    else:
                        wt_z.append(row["CDC_WT_Z_DAY"])
                    
                    if(pd.isna(row["CDC_BMI_Z"]) == False):
                        bmi_z.append(row["CDC_BMI_Z"])
                    else:
                        bmi_z.append(row["CDC_BMI_Z_DAY"])
                elif(row["AGE"] < 2):
                    if(pd.isna(row["WHO_HT_Z"]) == False):
                        ht_z.append(row["WHO_HT_Z"])
                    else:
                        ht_z.append(row["WHO_HT_Z_DAY"])
                    
                    if(pd.isna(row["WHO_WT_Z"]) == False):
                        wt_z.append(row["WHO_WT_Z"])
                    else:
                        wt_z.append(row["WHO_WT_Z_DAY"])
                    
                    if(pd.isna(row["WHO_BMI_Z"]) == False):
                        bmi_z.append(row["WHO_BMI_Z"])
                    else:
                        bmi_z.append(row["WHO_BMI_Z_DAY"])
                else:
                    if(pd.isna(row["NHANES_HT_Z"]) == False):
                        ht_z.append(row["NHANES_HT_Z"])
                    else:
                        ht_z.append(row["NHANES_HT_Z_DAY"])
                    
                    if(pd.isna(row["NHANES_WT_Z"]) == False):
                        wt_z.append(row["NHANES_WT_Z"])
                    else:
                        wt_z.append(row["NHANES_WT_Z_DAY"])
                    
                    if(pd.isna(row["NHANES_BMI_Z"]) == False):
                        bmi_z.append(row["NHANES_BMI_Z"])
                    else:
                        bmi_z.append(row["NHANES_BMI_Z_DAY"])

            new_data = {'Date':date, 'Age':age, 'HtZ':ht_z, 'WtZ':wt_z, 'BmiZ':bmi_z}
            newdf = pd.DataFrame(new_data)
            print(newdf)

            newdf = newdf.dropna()
            print(newdf)

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
        medTable["Date"] = pd.to_datetime(medTable["Date"], format="%m/%d/%y")
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
