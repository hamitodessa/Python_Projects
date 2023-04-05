'''
Created on Apr 5, 2023

@author: hamit
'''


from pt.Loglama.Ilog_kayit_Interface import LogKayitInterface


class lg_kayitMssql(LogKayitInterface):
    def connect(self,mesaj):
        print('Connecting to Loglama Kayit Mssql Database...' + mesaj)
    def disconnect(self):
        print('Disconnecting to Loglama Kayit Mssql Database....')