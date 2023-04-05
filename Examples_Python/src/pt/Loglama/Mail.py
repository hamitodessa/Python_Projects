'''
Created on Apr 6, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class LG_Mail(DBInterface):
    def connect(self,mesaj):
        print('Connecting to Loglama Mail...' + mesaj )
    def disconnect(self):
        print('Disconnecting to LoglamaMySql Database...')