'''
Created on Apr 1, 2023

@author: hamit
'''

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from tkinter import messagebox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from Global import Global  as glb
from User_Islemleri import User_Islemler as uisl
from fh.Access_DB import Fihrist_Access 

from fhr.UI_Files.Anapencere import *
import Cal_Dizini.Baglan as bAGLAN
import Cal_Dizini.Baglan_Log as bAGLAN_LOG

from Server_Baglan.Connect import Connect

Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui= Ui_MainWindow()
ui.setupUi(penAna)


#import pdb;pdb.set_trace()



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
        QApplication.setOverrideCursor(Qt.WaitCursor)
        if not ui.txtInstance.text():
            return
        if not ui.txtKullanici.text():
            return
        if not ui.txtSifre.text():
            return
        conn_aktar()
        if ui.chckBox_Lokal.isChecked() :
            conn = Connect(glb._IConn)
            sonuc =  conn.Server_kontrol_L(ui.txtInstance.text(), ui.txtKullanici.text(),  ui.txtSifre.text(), ui.txtServer.text())
            if  sonuc :
                ui.btnVeritabani.setEnabled(True)
                QApplication.restoreOverrideCursor()
            else:
                messagebox.showwarning("Server Baglanti", "Baglanti Saglanamadi........")
                ui.btnVeritabani.setEnabled(False)
        else: # Server Control
            if not ui.txtServer.text():
                QApplication.restoreOverrideCursor()
                return
            conn = Connect(glb._IConn)
            sonuc =  conn.Server_kontrol_S(ui.txtServer.text(),ui.txtInstance.text(), ui.txtKullanici.text(),  ui.txtSifre.text(), ui.txtServer.text())
            if  sonuc :
                ui.btnVeritabani.setEnabled(True)
                QApplication.restoreOverrideCursor()
            else:
                QApplication.restoreOverrideCursor()
                messagebox.showwarning("Server Baglanti", "Baglanti Saglanamadi........")
                ui.btnVeritabani.setEnabled(False)
    except Exception as e:
        QApplication.restoreOverrideCursor()
        if hasattr(e, 'message'):
            messagebox.showwarning("Server Baglanti", e.message)
        else:
            messagebox.showwarning("Server Baglanti", e)
def dosya_kontrol():
    try:
        QApplication.setOverrideCursor(Qt.WaitCursor)
        conn_aktar()
        if ui.chckBox_Lokal.isChecked() :
            conn = Connect(glb._IConn)
            sonuc =  conn.Dosyakontrol_L("OK_Fih" + ui.txtKod.text(), ui.txtKullanici.text(),  ui.txtSifre.text(), ui.txtInstance.text() ,ui.txtServer.text())
            if  sonuc :
                QApplication.restoreOverrideCursor()
                
                messagebox.showinfo("Veritabani Kontrol", "Baglanti Saglandi........")
                calisma_dizini_yaz()
            else:
                QApplication.restoreOverrideCursor()
                messagebox.showwarning("Veritabani Kontrol", "Baglanti Saglanamadi........")
                ui.btnVeritabani.setEnabled(False)
        else: # Server Control
            if not ui.txtServer.text():
                QApplication.restoreOverrideCursor()
                return
            conn = Connect(glb._IConn)
            sonuc =  conn.Dosyakontrol_S(ui.txtServer.text(),ui.txtInstance.text(), ui.txtKullanici.text(),  ui.txtSifre.text(),"OK_Fih" +  ui.txtKod.text()  ,ui.txtServer.text())
            if  sonuc :
                calisma_dizini_yaz()
                messagebox.showinfo("Veritabani Kontrol", "Baglanti Saglandi........")
                QApplication.restoreOverrideCursor()
            else:
                messagebox.showwarning("Veritabani Kontrol", "Baglanti Saglanamadi........")
                ui.btnVeritabani.setEnabled(False)
    except Exception as e:
        QApplication.restoreOverrideCursor()
        if hasattr(e, 'message'):
            messagebox.showwarning("Veritabani Kontrol", e.message)
        else:
            messagebox.showwarning("Veritabani Kontrol", e)
def calisma_dizini_yaz():
    uisl.calisanmi_degis("fffff", "Fihrist")
    from User_Islemleri.User_Details import user_detail 
    udtl = user_detail ()
    udtl.USER_PROG_KODU = ui.txtKod.text() 
    udtl.USER_NAME = "fffff"
    udtl.USER_SERVER = ui.txtKullanici.text()
    udtl.USER_PWD_SERVER = ui.txtSifre.text()
    udtl.USER_INSTANCE_OBS = ui.txtInstance.text()
    udtl.USER_IP_OBS = ui.txtServer.text()
    udtl.USER_PROG_OBS = "Fihrist"
    udtl.DIZIN = ""
    if ui.chckBox_Lokal.isChecked() :
        udtl.YER = "L"
    else:
        udtl.YER = "S"
    udtl.DIZIN_CINS = "D"
    udtl.IZINLI_MI="E"
    udtl.CALISAN_MI = "E"
    udtl.HANGI_SQL = ui.comboBox.currentText()
    udtl.CDID = ui.txtcdid.text()
    udtl.LOG = ui.chckBox_Loglama.checkState()
    vt = "False"
    sq = "False"
    tx = "False"
    em = "False"
    if ui.chckBox_Veritabani.isChecked():
        vt = "True"
    if ui.chckBox_SQLite.isChecked():
        sq = "True"
    if ui.chckBox_Text.isChecked():
        tx = "True"
    if ui.chckBox_Mail.isChecked():
        em = "True"
    udtl.LOG_YERI = vt + "," + sq +"," + tx +"," + em
    uisl.details_yaz(udtl)
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
    ui.btnVeritabani.setEnabled(False)
    ui.tabKontrol.setCurrentWidget(ui.tabKontrol.findChild(QWidget, "tab_Ayarlar"))
def btnKisiler():
    ui.tabKontrol.tabBar().close()
    ui.tabKontrol.setCurrentWidget(ui.tabKontrol.findChild(QWidget, "tab_Kisiler"))    
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
        
  
#-----------------BUTTONLAR------------------------------------*
ui.btnAyarlar.clicked.connect(btnAyarlar)
ui.btnKisiler.clicked.connect(btnKisiler)
ui.chckBox_Lokal.stateChanged.connect(chckBox_Lokal_Checked)
ui.chckBox_Server.stateChanged.connect(chckBox_Server_Checked)
ui.chckBox_Loglama.stateChanged.connect(chckBox_Loglama_Checked)
ui.btnBaglan.clicked.connect(server_kontrol)
ui.btnVeritabani.clicked.connect(dosya_kontrol)

ui.tabKontrol.tabBar().close()
ui.txtcdid.setVisible(False)
#*************************** Kontrol ***********************
dizin_kontrol()
#***********************************************************

penAna.show()


sys.exit(Uygulama.exec_())




