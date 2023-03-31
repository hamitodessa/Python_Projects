'''
Created on Mar 30, 2023

@author: hamit
'''

import DBInterface as myModule
k = myModule.DBInterface()

class Sybase(k):
   def connect(self):
       print('Connecting to Sybase Database...')
   def disconnect(self):
       print('Disconnecting to Sybase Database...')   