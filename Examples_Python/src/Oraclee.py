'''
Created on Mar 30, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class Oracle(DBInterface):
    def connect(self,mesaj,mesaj2):
        
        print('Connecting to Oracle Database...' + mesaj + "===" + mesaj2)
    def disconnect(self):
        print('Disconnecting to Oracle Database...')