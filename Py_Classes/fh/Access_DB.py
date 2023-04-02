'''
Created on Apr 1, 2023

@author: hamit
'''

class Fihrist_Access():
    def __init__(self, IFihrist,ILoger):
        self._IFihrist = IFihrist
        self.x=self._IFihrist()
        self.listee= ILoger
    def baglan(self,mesaj):
        self.x.connect()
        for qwe in self.listee:
            qwe.logla(self,mesaj)
