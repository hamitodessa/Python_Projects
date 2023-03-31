'''
Created on Mar 30, 2023

@author: hamit
'''
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from untitled import *


Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

sys.exit(Uygulama.exec_())
