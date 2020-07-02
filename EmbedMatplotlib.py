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
            data = getAnthropometricsDataFrame(patient)

            weight = data["Wt"]
            date = pd.to_datetime(data["Date"])

            print("------------------")
            print("The Dates Are ...")
            for d in date:
                print(str(d) + " - type - " + str(type(d)))

            print("------------------")
            print("The Weights Are ...")
            for w in weight:
                print(str(w) + " - type - " + str(type(w)))



            ax = self.figure.add_subplot(111)
            ax.plot(date, weight)
            ax.set_title(patient + " | Anthropometrics (Weight vs Time)")
            ax.set_xlabel("Date - (MM/DD/YYYY)")
            ax.set_ylabel("Weight - (KG)")
            # ax.set_facecolor('#f0f0f0')
            # ax.set_axis_bgcolor('#f0f0f0')
            
            

        except:
            print("Can't create graph, most likely the types aren't correct or the data is invalid")

# app = QApplication(sys.argv)
# window = Window()
# window.show()
# app.exec()