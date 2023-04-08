'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface
from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI

class Dao_MsSql(ILogKayitInterface):
    def logla(self, mesaj, evrak, DIZIN_BILGILERI):
        print('Connecting to Log MsSql Log Kayite...' + DIZIN_BILGILERI.kULLANICI)
        print('Connecting to Log MsSql Log Kayite...' +mesaj)
    def log_rapor(self):
        print('Connecting to MsSql Log Kayite...' )
    