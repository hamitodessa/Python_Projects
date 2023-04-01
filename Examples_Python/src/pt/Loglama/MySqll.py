'''
Created on Apr 1, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class LG_MySql(DBInterface):
   def connect(self):
       print('Connecting to MySql Database...')
   def disconnect(self):
       print('Disconnecting to MySql Database...')