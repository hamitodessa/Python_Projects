'''
Created on Apr 1, 2023

@author: hamit
'''

class Fihrist_Access():
    def __init__(self, IFihrist,ILoger):
        self._IFihrist = IFihrist
        self.x=self._ICari()
        self.listee= ILoger
    def logla(self,mesaj):
        print(mesaj)
        self.x.connect()
        for qwe in self.listee:
            qwe.connect(self)
