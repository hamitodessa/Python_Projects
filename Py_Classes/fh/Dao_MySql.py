'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt



class MySql(IFihristt):
    def connect(self):
        print('Connecting to Mysql Database...')
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mysql Database...')