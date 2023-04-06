'''
Created on Apr 6, 2023

@author: hamit
'''

from Server_Baglan.IConnection import IConnection
import pypyodbc 


class Obs_Ortak_MsSql(IConnection):
    def Server_kontrol_L(self,inst, kull, sifre,  port):
        try:
            print( inst)
            #connSqlServer = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=192.106.0.102\instance1;DATABASE=master;UID=sql2008;PWD=password123')
            #pyodbc.connect()
            instt = "\\" + inst
            conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';Trust_Connection =True')
            print(conn)
            if conn :
                return True
            else:
                return False
        except:
            return False
    def Server_kontrol_S(self,server, inst, kull,  sifre, port):
        try:
            #connSqlServer = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=192.106.0.102,1443;DATABASE=master;UID=sql2008;PWD=password123')
            pypyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';instanceName=' + inst +';UID='+ kull+';PWD=' + sifre)
            return True
        except:
            return False
    def Dosyakontrol_L(self, db, kull, sifre,  inst ,  port):
        return self.ICn.Server_kontrol_L(self,  db, kull, sifre,  inst ,  port)
    def Dosyakontrol_S(self,server, inst, kull,sifre, prog , port):
        return self.ICn.Server_kontrol_L(self,  server, inst, kull,sifre, prog , port)