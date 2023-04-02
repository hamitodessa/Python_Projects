'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.ILoger import ILogerr

class Dao_MsSql(ILogerr):
    def logla(self,mesaj):
        print('Connecting to MsSql Log Kayite...' + mesaj)
    def log_rapor(self):
        print('Connecting to MsSql Log Kayite...' )
    