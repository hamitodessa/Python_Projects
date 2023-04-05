'''
Created on Apr 1, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class LG_MySql(DBInterface):
    def connect(self,mesaj):
        print('Connecting to Loglama MySql Database...' + mesaj)
    def disconnect(self):
        print('Disconnecting to LoglamaMySql Database...')