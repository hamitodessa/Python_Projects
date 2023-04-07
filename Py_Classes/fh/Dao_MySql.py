'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt



class MySql(IFihristt):
    def baglan(self,mesaj):
        print('Connecting to Mysql Database...' + mesaj)
    def fih__sifirdan_L(self,mesaj):
        pass
    def fih__sifirdan_S(self,mesaj):
        pass
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mysql Database...')