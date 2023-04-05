'''
Created on Apr 5, 2023

@author: hamit
'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from fhr.UI_Files.login import *


Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui= Ui_Login()
ui.setupUi(penAna)


penAna.show()


sys.exit(Uygulama.exec_())
