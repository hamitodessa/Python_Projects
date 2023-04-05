'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface

class Dao_Txt(ILogKayitInterface):
    def logla(self,mesaj):
        print('Connecting to Log Txt Database...')
    def log_rapor(self):
        print('Connecting to Txt Database...')
    