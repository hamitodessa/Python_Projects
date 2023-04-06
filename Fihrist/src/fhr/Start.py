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

#glb._Fihrist = [glb.Ms_Sql,glb.MySql]
#glb._IFihrist_Loger = [glb.Maill,glb.Dao_MsSql,glb.Dao_MySql,glb.Dao_SqLite,glb.Dao_Txt]
#fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
#fih.baglan("Deneme mesaji")



def dizin_kontrol():
    import os
    isExist =os.path.isfile(glb.SURUCU + glb.OBS_FIHRIST_DOSYA)
    if isExist:
        #Dosya var
        bAGLAN.cONNECT("hamit")
        bAGLAN_LOG.cONNECT()
        if bAGLAN.fihDizin.kULLANICI == "":
            loglama_kapat()
            btnAyarlar()
        else:
            pass
            #print ("kull1=" +bAGLAN.fihDizin.kULLANICI)
            #print ("kull2=" +bAGLAN.cariDizin.kOD)
            #print ("kull3=" +bAGLAN.cariDizin.sERVER)
            #print ("kull4=" +bAGLAN_LOG.cariLogDizin.cONN_STR)
            #print ("kull5=" +bAGLAN_LOG.cariLogDizin.mODULADI)
    else:
        glb.fih_surucu_kontrol()

def server_kontrol():
    try:
        conn_aktar()
        
        if ui.chckBox_Lokal.isChecked() :
            if not ui.txtInstance.text():
                return
            if not ui.txtKullanici.text():
                return
            if not ui.txtSifre.text():
                return
            if not ui.txtServer.text():
                return
            from Server_Baglan.Connect import Connect
            conn = Connect(glb._IConn)
            
            sonuc =  conn.Server_kontrol_L(ui.txtInstance.text(), ui.txtKullanici.text(),  ui.txtSifre.text(), ui.txtServer.text())
            print(sonuc)
            if  sonuc :
                print("Baglandi")
            else:
                from tkinter import messagebox
                messagebox.showwarning("Server Baglanti", "Baglanti Saglanamadi........")
                #btnNewButton_1.setEnabled(false);
              
        else: # Server Control
            pass
    except Exception as e:
    # Just print(e) is cleaner and more likely what you want,
    # but if you insist on printing message specifically whenever possible...
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
def conn_aktar():
    hangi = ui.comboBox.currentText()
    from  Server_Baglan.OBS_Ortak_MsSql import Obs_Ortak_MsSql
    from  Server_Baglan.OBS_Ortak_MySql import Obs_Ortak_MySql
    from  Server_Baglan.OBS_Ortak_SqLite import Obs_Ortak_SqLite
    if hangi == "Ms Sql":
        glb._IConn = Obs_Ortak_MsSql
    elif hangi == "My Sql":
        glb._IConn = Obs_Ortak_MySql
    elif hangi == "Sq Lite":
        glb._IConn = Obs_Ortak_SqLite
   
def btnAyarlar():
    #print(ui.tabKontrol.currentIndex())
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
        loglama_kapat()
def loglama_kapat():
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
ui.btnBaglan.clicked.connect(server_kontrol)

penAna.show()


sys.exit(Uygulama.exec_())




