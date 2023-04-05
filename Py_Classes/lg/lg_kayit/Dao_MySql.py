'''
Created on Apr 1, 2023

@author: hamit
'''
from lg.lg_kayit.ILog_Kayit import ILogKayitInterface

class Dao_MySql(ILogKayitInterface):
    def logla(self,mesaj):
        print('Connecting to Log MySql Database...')
    def log_rapor(self):
        print('Connecting to MySql Database...')
    