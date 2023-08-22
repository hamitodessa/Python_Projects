'''
Created on Apr 1, 2023

@author: hamit
'''

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from tkinter import messagebox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication ,QMainWindow,QWidget,QInputDialog

from Global import Global  as glb
from User_Islemleri import User_Islemler as uisl
from fh.Access_DB import Fihrist_Access 


import Cal_Dizini.Baglan as bAGLAN
import Cal_Dizini.Baglan_Log as bAGLAN_LOG
from fhr.UI_Files.Anapencere import *
from Server_Baglan.Connect import Connect

class Start(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Start,self).__init__(parent)
        self.setupUi(self)
    




#import pdb;pdb.set_trace()

#glb.obs_dosya_olustur()

#glb._Fihrist = [glb.Ms_Sql,glb.My_Sql]
#glb._IFihrist_Loger = [glb.Maill,glb.Dao_MsSql,glb.Dao_MySql,glb.Dao_SqLite,glb.Dao_Txt]
#fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
#fih.baglan("Deneme mesaji")



def dizin_kontrol():
    import os
    isExist =os.path.isfile(glb.SURUCU + glb.OBS_FIHRIST_DOSYA)
    if isExist:
        #Dosya var
        bAGLAN.cONNECT(glb.KULL_ADI)
        bAGLAN_LOG.cONNECT()
        if bAGLAN.fihDizin.kULLANICI == "":
            loglama_kapat()
            btnAyarlar()
        else:
            ui.txtKod.setText(bAGLAN.fihDizin.kOD)
            ui.txtInstance.setText(bAGLAN.fihDizin.iNSTANCE)
            ui.txtServer.setText(bAGLAN.fihDizin.sERVER)
            ui.txtKullanici.setText(bAGLAN.fihDizin.kULLANICI)
            ui.txtSifre.setText(bAGLAN.fihDizin.sIFRESI)
            ui.txtcdid.setText(str(bAGLAN.fihDizin.cDID))
            if bAGLAN.fihDizin.yER == "L":
                ui.chckBox_Lokal.setChecked(True)
                ui.chckBox_Server.setChecked(False)
            else:
                ui.chckBox_Server.setChecked(True)
                ui.chckBox_Lokal.setChecked(False)
            ui.chckBox_Loglama.setChecked(bAGLAN.fihDizin.lOG)
            if not ui.chckBox_Loglama.isChecked():
                loglama_kapat()
            ui.comboBox.setCurrentText(bAGLAN.fihDizin.hAN_SQL)
            if bAGLAN.fihDizin.hAN_SQL == "Ms Sql" :
                glb._Fihrist = [glb.Ms_Sql]
            elif bAGLAN.fihDizin.hAN_SQL == "My Sql" :
                glb._Fihrist = [glb.My_Sql]
            logl = bAGLAN.fihDizin.lOGLAMA_YERI.split(',')
            Liste = []
            if logl[0] == "True" :
                ui.chckBox_Veritabani.setChecked(True)
                if bAGLAN.fihDizin.hAN_SQL == "Ms Sql" :
                    Liste.append(glb.Dao_MsSql)
                elif bAGLAN.fihDizin.hAN_SQL == "My Sql" :
                    Liste.append(glb.Dao_MySql)
            else:
                ui.chckBox_Veritabani.setChecked(False)
            if logl[1] == "True" :
                Liste.append(glb.Dao_SqLite)
                ui.chckBox_SQLite.setChecked(True)
            else:
                ui.chckBox_SQLite.setChecked(False)
            if logl[2] == "True" :
                Liste.append(glb.Dao_Txt)
                ui.chckBox_Text.setChecked(True)
            else:
                ui.chckBox_Text.setChecked(False)
            if logl[3] == "True" :
                Liste.append(glb.Maill)
                ui.chckBox_Mail.setChecked(True)
            else:
                ui.chckBox_Mail.setChecked(False)
            glb._IFihrist_Loger = Liste
            btnKisiler()
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
                QApplication.restoreOverrideCursor()
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
                dosya_olustur_L()
                
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
def dosya_olustur_L():
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Yeni Dosya Olusturulsunmu.?")
    msg.setWindowTitle("Dosya Olusturma")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.No)
    msg.setDefaultButton(QMessageBox.No)
    buttonReply = msg.exec_()  
    if buttonReply == QMessageBox.No:
        return
    #else:
    #    print('Yes clicked.')
            
    text, ok = QInputDialog().getText(None, "Dosya Olusturma" ,"Firma Adini Giriniz.?")
    if not ok:
        return
     
    hangi = ui.comboBox.currentText()
    if hangi == "Ms Sql":
        glb._Fihrist = [glb.Ms_Sql]
    elif hangi == "My Sql":
        glb._Fihrist = [glb.My_Sql]
    glb._IFihrist_Loger = [glb.Dao_MsSql]
    fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
   
    #******************************************
    bAGLAN.fihDizin.kULLANICI = ui.txtKullanici.text()
    bAGLAN.fihDizin.sIFRESI = ui.txtSifre.text()
    bAGLAN.fihDizin.hAN_SQL = ui.comboBox.currentText()
    bAGLAN.fihDizin.sERVER = ui.txtSifre.text()
    bAGLAN.fihDizin.kOD = ui.txtKod.text() 
    bAGLAN.fihDizin.yER = "L";
    bAGLAN.fihDizin.iNSTANCE =ui.txtInstance.text()
    bAGLAN_LOG.cONNECT()
    #******************************************
    if ui.chckBox_Lokal.isChecked() :
        from User_Islemleri.User_Details import user_detail 
        udtl = user_detail ()
        udtl.USER_PROG_KODU = ui.txtKod.text() 
        udtl.DIZIN = ""
        udtl.DIZIN_CINS = ""
        udtl.USER_INSTANCE_OBS = ui.txtInstance.text()
        udtl.USER_SERVER = ui.txtKullanici.text()
        udtl.USER_PWD_SERVER = ui.txtSifre.text()
        udtl.FIRMA_ADI = text
        fih.fih__sifirdan_L(udtl)
    else:
        fih.fih__sifirdan_S("dddd")
    
    calisma_dizini_yaz()
def calisma_dizini_yaz():
    uisl.calisanmi_degis(glb.KULL_ADI, "Fihrist")
    from User_Islemleri.User_Details import user_detail 
    udtl = user_detail ()
    udtl.USER_PROG_KODU = ui.txtKod.text() 
    udtl.USER_NAME = glb.KULL_ADI
    udtl.USER_SERVER = ui.txtKullanici.text()
    udtl.USER_PWD_SERVER = ui.txtSifre.text()
    udtl.USER_INSTANCE_OBS = ui.txtInstance.text()
    
    udtl.USER_PROG_OBS = "Fihrist"
    udtl.DIZIN = ""
    if ui.chckBox_Lokal.isChecked() :
        udtl.YER = "L"
        udtl.USER_IP_OBS = ""
    else:
        udtl.YER = "S"
        udtl.USER_IP_OBS = ui.txtServer.text()
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
    if ui.chckBox_Loglama.isChecked():
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
    
    #glb._Fihrist = [glb.Ms_Sql]
    #glb._IFihrist_Loger = []
    fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)
    fih.baglan("Deneme mesaji","12345", bAGLAN_LOG.fihLogDizin)  
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
        

#***********************************************************
Uygulama= QApplication(sys.argv)
penAna = QMainWindow()
ui= Ui_MainWindow()
ui.setupUi(penAna)
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




