'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt



class Ms_Sql(IFihristt):
    def connect(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mssql Database...')