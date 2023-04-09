'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface
from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI
from Global import Global  as glb
import pypyodbc 
import datetime

class Dao_MsSql(ILogKayitInterface):
    def logla(self, mesaj, evrak, DIZIN_BILGILERI):
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=' + DIZIN_BILGILERI.cONN_STR) 
        sql = 'INSERT INTO LOGLAMA (TARIH,EVRAK,MESAJ,[USER_NAME]) \
                 VALUES (?,?,?,?)'
        curs = conn.cursor()
        curs.execute(sql,(datetime.datetime.now() , evrak,mesaj,glb.KULL_ADI ))
        curs.commit()
        conn.close()
    def log_rapor(self):
        print('Connecting to MsSql Log Kayit...' )
    