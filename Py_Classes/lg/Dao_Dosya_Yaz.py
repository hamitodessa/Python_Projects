'''
Created on Apr 5, 2023

@author: hamit
'''

from lg.ILoger import ILogerr



class Dosya_Yaz(ILogerr):
    def __init__(self, ILogerr,mesaj):
        self.mesaj = mesaj
        self.listee= ILogerr
    def logla(self):
        for qwe in self.listee:
            qwe.logla(self,self.mesaj)
