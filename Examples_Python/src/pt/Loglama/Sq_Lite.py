'''
Created on Apr 5, 2023

@author: hamit
'''

from pt.Loglama.Ilog_kayit_Interface import LogKayitInterface



class sq_lite(LogKayitInterface):
   def connect(self):
       print('Connecting to sq liteDatabase...')
   def disconnect(self):
       print('Disconnecting to sq lite Database....')