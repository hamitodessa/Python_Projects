'''
Created on Apr 1, 2023

@author: hamit
'''

class Fihrist_Access():
    def __init__(self, IFihrist,ILoger):
        self._IFihrist = IFihrist
        self.IDb=self._IFihrist()
        self.log_liste= ILoger
    def baglan(self,mesaj):
        self.IDb.connect()
        for qwe in self.log_liste:
            qwe.logla(self,mesaj)
