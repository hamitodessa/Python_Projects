'''
Created on Mar 30, 2023

@author: hamit
'''

from DBInterfacee import DBInterface

class Sybase(DBInterface):
    def connect(self,mesaj,mesaj2):
        print('Connecting to Sybase Database...')
    def disconnect(self):
        print('Disconnecting to Sybase Database...')   