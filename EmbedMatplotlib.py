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
    def __init__(self, patient, parent = None, width = 15, height = 10, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot(patient=patient)

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
            # ax.set_facecolor('#f0f0f0')
            # ax.set_axis_bgcolor('#f0f0f0')
        except:
            print("Can't create graph, most likely the types aren't correct or the data is invalid")
        
        #try:
        #    data2 = getDemographics(1)
        #   print (data2)
        #except:
        #    print("error with demo")
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# app.exec()