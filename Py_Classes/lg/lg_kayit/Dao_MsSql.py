'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface

class Dao_MsSql(ILogKayitInterface):
    def logla(self,mesaj):
        print('Connecting to Log MsSql Log Kayite...' + mesaj)
    def log_rapor(self):
        print('Connecting to MsSql Log Kayite...' )
    