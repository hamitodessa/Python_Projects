'''
Created on Apr 6, 2023

@author: hamit
'''

from Server_Baglan.IConnection import IConnection
import pypyodbc 


class Obs_Ortak_MsSql(IConnection):
    def Server_kontrol_L(self,inst, kull, sifre,  port):
        try:
            #connSqlServer = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=192.106.0.102\instance1;DATABASE=master;UID=sql2008;PWD=password123')
            #pyodbc.connect()
            instt = "\\" + inst
            pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';Trust_Connection =True')
            return True
        except:
            return False
    def Server_kontrol_S(self,server, inst, kull,  sifre, port):
        try:
            pypyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';instanceName=' + inst +';UID='+ kull+';PWD=' + sifre +';Trust_Connection =True')
            return True
        except:
            return False
    def Dosyakontrol_L(self, db, kull, sifre,  inst ,  port):
        return self.ICn.Server_kontrol_L(self,  db, kull, sifre,  inst ,  port)
    def Dosyakontrol_S(self,server, inst, kull,sifre, prog , port):
        return self.ICn.Server_kontrol_L(self,  server, inst, kull,sifre, prog , port)