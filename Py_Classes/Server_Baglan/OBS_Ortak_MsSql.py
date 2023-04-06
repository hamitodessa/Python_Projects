'''
Created on Apr 6, 2023

@author: hamit
'''

from Server_Baglan.IConnection import IConnection
import pypyodbc


class Obs_Ortak_MsSql(IConnection):
    def Server_kontrol_L(self,inst, kull, sifre,  port):
        try:
            print("inst=" + inst)
            pypyodbc.connect('DRIVER={SQL Server};SERVER=localhost;instanceName=' + inst +';UID='+ kull+';PWD=' + sifre)
            return True
        except:
            print("hata")
            return False