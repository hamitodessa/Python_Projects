'''
Created on Apr 6, 2023

@author: hamit
'''

from Server_Baglan.IConnection import IConnection
import pypyodbc 


class Obs_Ortak_MsSql(IConnection):
    def Server_kontrol_L(self,inst, kull, sifre,  port):
        try:
            instt = "\\" + inst
            pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';UID='+ kull+';PWD=' + sifre +';Trust_Connection =True')
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
        try:
            instt = "\\" + inst
            conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';UID='+ kull+';PWD=' + sifre +';Trust_Connection =True')
            sql = "SELECT * FROM sys.databases where name = '" + db + "'"
            curs = conn.cursor()
            curs.execute(sql) 
            result = curs.fetchall()
            if len(result) > 0:
                return True
            else:
                return False
        except:
            return False
    def Dosyakontrol_S(self,server, inst, kull,sifre, prog , port):
        return self.ICn.Server_kontrol_L(self,  server, inst, kull,sifre, prog , port)