'''
Created on Apr 1, 2023

@author: hamit
'''

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


from Global import Global  as glb
from fh.Access_DB import Fihrist_Access 

from fhr.UI_Files.Anapencere import *

Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui= Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

#
import Cal_Dizini.Baglan as bAGLAN
import Cal_Dizini.Baglan_Log as bAGLAN_LOG
bAGLAN.cONNECT("hamit")
bAGLAN_LOG.cONNECT()

print ("kull1=" +bAGLAN.cariDizin.kULLANICI)
print ("kull2=" +bAGLAN.cariDizin.kOD)
print ("kull3=" +bAGLAN.cariDizin.sERVER)
print ("kull4=" +bAGLAN_LOG.cariLogDizin.cONN_STR)
print ("kull5=" +bAGLAN_LOG.cariLogDizin.lOGLAMA_YERI)
#



#glb.obs_dosya_olustur()

glb._Fihrist = glb.Ms_Sql
glb._IFihrist_Loger = [glb.Maill,glb.Dao_MsSql,glb.Dao_MySql,glb.Dao_SqLite,glb.Dao_Txt]
fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
fih.baglan("Deneme mesaji")
sys.exit(Uygulama.exec_())