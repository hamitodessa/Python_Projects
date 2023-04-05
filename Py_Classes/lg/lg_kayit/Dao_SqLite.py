'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface

class Dao_SqLite(ILogKayitInterface):
    def logla(self,mesaj):
        print('Connecting to Log SqLite Database...'+ mesaj)
    def log_rapor(self):
        print('Connecting to SqLite Database...')
    