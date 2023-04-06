'''
Created on Apr 6, 2023

@author: hamit
'''

from Server_Baglan.IConnection import IConnection
import pypyodbc


class Obs_Ortak_MsSql(IConnection):
    def Server_kontrol_L(self,inst, kull, sifre,  port):
        try:
            pypyodbc.connect('DRIVER={SQL Server};SERVER=localhost;instanceName=' + inst +';')
            return True
        except:
            return False
    def Server_kontrol_S(self,server, inst, kull,  sifre, port):
        try:
            pypyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';instanceName=' + inst +';UID='+ kull+';PWD=' + sifre)
            return True
        except:
            return False
    def Dosyakontrol_L(self, db, kull, sifre,  inst ,  port):
        return self.ICn.Server_kontrol_L(self,  db, kull, sifre,  inst ,  port)
    def Dosyakontrol_S(self,server, inst, kull,sifre, prog , port):
        return self.ICn.Server_kontrol_L(self,  server, inst, kull,sifre, prog , port)