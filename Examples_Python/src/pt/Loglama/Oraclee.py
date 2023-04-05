'''
Created on Mar 30, 2023

@author: hamit
'''
from pt.Loglama.Ilog_kayit_Interface import LogKayitInterface



class LG_Oracle(LogKayitInterface):
    def connect(self,mesaj):
        print('Connecting to Loglama kayit Oracle Database...' + mesaj)
    def disconnect(self):
        print('Disconnecting to Loglama Oracle Database...')