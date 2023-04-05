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
import Cal_Dizini.Baglan as bAGLAN
import Cal_Dizini.Baglan_Log as bAGLAN_LOG

Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui= Ui_MainWindow()
ui.setupUi(penAna)






#glb.obs_dosya_olustur()

glb._Fihrist = [glb.Ms_Sql]
glb._IFihrist_Loger = [glb.Maill,glb.Dao_MsSql,glb.Dao_MySql,glb.Dao_SqLite,glb.Dao_Txt]
fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
fih.baglan("Deneme mesaji")



def dizin_kontrol():
    import os
    isExist =os.path.isfile(glb.SURUCU + glb.OBS_DOSYA)
    if isExist:
        #Dosya var
        print("dos var")
        bAGLAN.cONNECT("hamit")
        bAGLAN_LOG.cONNECT()
        print ("kull1=" +bAGLAN.cariDizin.kULLANICI)
        print ("kull2=" +bAGLAN.cariDizin.kOD)
        print ("kull3=" +bAGLAN.cariDizin.sERVER)
        print ("kull4=" +bAGLAN_LOG.cariLogDizin.cONN_STR)
        print ("kull5=" +bAGLAN_LOG.cariLogDizin.mODULADI)
    else:
        glb.surucu_kontrol()
    
def btnAyarlar():
    print(ui.tabKontrol.currentIndex())
    #ui.tabKontrol.setCurrentIndex(1)
    ui.tabKontrol.tabBar().close()
    ui.tabKontrol.setCurrentWidget(ui.tabKontrol.findChild(QWidget, "tab_Ayarlar"))
def chckBox_Lokal_Checked():
    if ui.chckBox_Lokal.isChecked() :
        ui.chckBox_Server.setChecked(False)
        ui.txtServer.setEnabled(False)
    else:
        ui.chckBox_Server.setChecked(True)
def chckBox_Server_Checked():
    if ui.chckBox_Server.isChecked() :
        ui.chckBox_Lokal.setChecked(False)
        ui.txtServer.setEnabled(True)
    else:
        ui.chckBox_Lokal.setChecked(True)
def chckBox_Loglama_Checked():
    if ui.chckBox_Loglama.isChecked() :
        ui.chckBox_Veritabani.setVisible(True)
        ui.chckBox_SQLite.setVisible(True)
        ui.chckBox_Text.setVisible(True)
        ui.chckBox_Mail.setVisible(True)
    else:
        ui.chckBox_Veritabani.setVisible(False)
        ui.chckBox_SQLite.setVisible(False)
        ui.chckBox_Text.setVisible(False)
        ui.chckBox_Mail.setVisible(False)

        
    

#*************************** Kontrol ***********************
dizin_kontrol()
#***********************************************************
  
#-----------------BUTTONLAR------------------------------------*
ui.pushBtnAyarlar.clicked.connect(btnAyarlar)
ui.chckBox_Lokal.stateChanged.connect(chckBox_Lokal_Checked)
ui.chckBox_Server.stateChanged.connect(chckBox_Server_Checked)
ui.chckBox_Loglama.stateChanged.connect(chckBox_Loglama_Checked)


penAna.show()


sys.exit(Uygulama.exec_())




