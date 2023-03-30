#Imports
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QProcess
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import constructed_gui

import os
import sys

#Directry change
current_file_path = os.path.realpath(__file__)
script_directory = os.path.dirname(current_file_path)
os.chdir(script_directory)

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = constructed_gui.Ui_MainWindow()
        self.ui.setupUi(self)

        #Icon
        icon = QIcon('img/calc.ico')
        self.setWindowIcon(icon)

        #Buttons
        self.ui.Remainder_calc.clicked.connect(self.remainder_calc)
        
        #Intended BED
        self.ui.n_slider_intended.valueChanged.connect(self.update_n_inteded)
        self.ui.d_slider_intended.valueChanged.connect(self.update_d_inteded)
        self.ui.ab_slider_intended.valueChanged.connect(self.update_ab_inteded)

        #Delivered BED
        self.ui.n_slider_delivered.valueChanged.connect(self.update_n_delivered)
        self.ui.d_slider_delivered.valueChanged.connect(self.update_d_delivered)
        self.ui.ab_slider_delivered.valueChanged.connect(self.update_ab_delivered)

        #Menu items      
        self.ui.actionAbout.triggered.connect(self.menu_about)
        self.ui.actionRestart.triggered.connect(self.restart)
        self.ui.actionExit.triggered.connect(self.exit)

    #Functions
    def intended_BED(self):
        try:
            n = self.ui.n_slider_intended.value()
            d = self.ui.d_slider_intended.value()
            alpha_beta = self.ui.ab_slider_intended.value()
            TD = n * d
            BED_1  = round(TD * (1 + d/(alpha_beta)), 2)
            
            return BED_1
        except:
            QMessageBox.warning(self, "Error!", "Please pick values first and then press calculate.")

    def delivered_BED(self):
        try:
            n = self.ui.n_slider_delivered.value()
            d = self.ui.d_slider_delivered.value()
            alpha_beta = self.ui.ab_slider_delivered.value()
            TD = n * d
            BED_2 = round(TD * (1 + d/(alpha_beta)), 2)

            return BED_2
        except:
            QMessageBox.warning(self, "Error", "Please pick values first and then press calculate.")

    def remainder_calc(self):
        try:
            x = self.intended_BED()
            y = self.delivered_BED()

            remainder = round(x - y,2)

            self.ui.iBED.setText(f'{str(x)} Gy')
            self.ui.dBED.setText(f'{str(y)} Gy')

            self.ui.Remainder_subtitle.setText('Remains to be delivered:')
            self.ui.Remainder_result.setText(f'{str(remainder)} Gy')

            return remainder
        except:
            QMessageBox.warning(self, "Error", "Something went wrong, please try again.")

    def update_n_inteded(self, value):
        self.ui.n_slider.setText(str(value))

    def update_n_delivered(self, value):
        self.ui.n_slider_2.setText(str(value))
    
    def update_d_inteded(self, value):
        self.ui.d_slider.setText(str(value))

    def update_d_delivered(self, value):
        self.ui.d_slider_2.setText(str(value))

    def update_ab_inteded(self, value):
        self.ui.ab_slider.setText(str(value))

    def update_ab_delivered(self, value):
        self.ui.ab_slider_2.setText(str(value))






    def menu_about(self):
        QMessageBox.information(self,  "About this app", "This app was developed to assist medical physics team in (re)calculating BED if the break in the treatment occurs.\n\nDesigned and coded by MSc Mladen Babić",)
   
    def restart(self):
        # restart function
        QApplication.quit()
        QProcess.startDetached(sys.executable, sys.argv)

    def exit(self):
        # exit function
        QApplication.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()