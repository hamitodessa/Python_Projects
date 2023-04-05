'''
Created on Apr 1, 2023

@author: hamit
'''

class Fihrist_Access():
    def __init__(self, IFihrist,ILoger):
        self.IDb= IFihrist
        self.log_liste= ILoger
    def baglan(self,mesaj):
        for qwe in self.IDb:
            qwe.connect(self)
        for qwe in self.log_liste:
            qwe.logla(self,mesaj)
