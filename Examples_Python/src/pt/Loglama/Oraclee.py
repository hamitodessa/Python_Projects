'''
Created on Mar 30, 2023

@author: hamit
'''
from pt.Loglama.Loglama_Interfacee import LoglamaInterface



class LG_Oracle(LoglamaInterface):
   def connect(self):
       print('Connecting to Loglama Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Loglama Oracle Database...')