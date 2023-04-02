'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt



class MySql(IFihristt):
   def connect(self):
       print('Connecting to Mysql Database...')
   def disconnect(self):
       print('Disconnecting to Mysql Database...')