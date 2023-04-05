'''
Created on Apr 5, 2023

@author: hamit
'''
from DBInterfacee import DBInterface



class Dosya_yaz(DBInterface):
    def __init__(self, LG_Interface):
        self.listee= LG_Interface
    def connect(self,aa,mesaj):
        for qwe in self.listee:
            qwe.connect(self,mesaj)
    def disconnect(self):
        pass        
