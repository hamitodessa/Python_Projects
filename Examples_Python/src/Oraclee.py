'''
Created on Mar 30, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle Database...')
    def disconnect(self):
        print('Disconnecting to Oracle Database...')