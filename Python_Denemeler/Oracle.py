'''
Created on Mar 30, 2023

@author: hamit
'''

import DBInterface as myModule
k = myModule.DBInterface()




class Oracle(k):
   def connect(self):
       print('Connecting to Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Oracle Database...')