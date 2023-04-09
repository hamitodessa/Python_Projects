'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface
from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI
from Global import Global  as glb
import sqlite3
import datetime
from PyQt5.QtWidgets import *

class Dao_SqLite(ILogKayitInterface):
    def logla(self, mesaj, evrak, DIZIN_BILGILERI):
        conn =  sqlite3.connect( glb.LOG_SURUCU +  DIZIN_BILGILERI.mODUL )
        curs = conn.cursor()
        curs.execute('INSERT INTO LOGLAMA (TARIH,EVRAK,MESAJ,[USER_NAME]) \
                 VALUES (?,?,?,?)',(datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), evrak,mesaj,glb.KULL_ADI ))
        conn.commit()
        conn.close()
    def log_rapor(self):
        print('Connecting to SqLite Database...')
    
